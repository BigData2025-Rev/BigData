# Spark Review Notes


## 1. Creating RDDs and DataFrames

### RDDs (Resilient Distributed Datasets):
- **From a Collection:**
  ```
  rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
  # or
  rdd = sc.parallelize([1, 2, 3, 4])
  ```
- **From a File:**
  ```
  rdd = sc.textFile("path/to/file.txt")
  ```

### DataFrames:
- **From a Collection:**
  ```
  from pyspark.sql import Row
  data = [('Alice', 30), ('Bob', 25)]
  df = spark.createDataFrame(data, ["Name", "Age"])
  ```
- **From a File:**
  ```
  df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
  # or
  df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("path/to/file.csv")
  ```

## 2. Saving DataFrames to File

### Syntax:
- **CSV:**
  ```python
  df.write.csv("path/to/output.csv", header=True)
  ```
- **JSON:**
  ```python
  df.write.json("path/to/output.json")
  ```
- **Parquet:**
  ```python
  df.write.parquet("path/to/output.parquet")
  ```
- **ORC:**
  ```python
  df.write.orc("path/to/output.orc")
  ```

### Options:
- **Write modes**
```
.mode("append")
.mode("overwrite")
.mode("error") # Throw exception if data already exists
.mode("ignore") # silently ignore operation if data already exists
```
## 3. Shared Variables

### Broadcast Variables:
- Used to efficiently share large, read-only data across all nodes.
- **Usage:**
  ```
  broadcast_var = spark.sparkContext.broadcast([1, 2, 3])
  rdd = spark.sparkContext.parallelize([1, 2, 3])
  rdd.map(lambda x: x * broadcast_var.value[0]).collect()
  ```

### Accumulators:
- Used to accumulate values across tasks (e.g., counters or sums).
- **Usage:**
  ```
  accumulator = spark.sparkContext.accumulator(0)
  def add_to_accumulator(x):
      global accumulator
      accumulator.add(x)
  
  rdd = spark.sparkContext.parallelize([1, 2, 3])
  rdd.foreach(lambda x: add_to_accumulator(x))
  print(accumulator.value)
  ```

## 4. Partitioning/Bucketing

### Partitioning:
- **Creating partitions:**
  ```
  df.repartition(4)
  ```
- **Specifying partition columns:**
  ```
  df.repartition(4, "column_name")
  ```

**Bucketing:**
- Useful for optimizing joins and queries.
- **Creating bucketed tables:**
  ```
  df.write.bucketBy(4, "bucket_column").saveAsTable("bucketed_table")
  ```

## 5. Persistence and Storage Levels

### Persistence:
- **Syntax:**
  ```
  rdd.persist()  # Default is MEMORY_AND_DISK
  ```

### Storage Levels:
- **MEMORY_ONLY:** Store RDD as deserialized objects.
- **MEMORY_AND_DISK:** Store RDD in memory; spill to disk if needed.
- **DISK_ONLY:** Store RDD only on disk.
- **MEMORY_ONLY_SER:** Store RDD as serialized objects (more space-efficient).
- **MEMORY_AND_DISK_SER:** Store RDD as serialized objects; spill to disk if needed.

**Example:**
  ```
  df.persist(storageLevel=StorageLevel.MEMORY_AND_DISK)
  ```

## 6. File Types

### CSV:
- Text files with comma-separated values.
- Supports header and schema inference.

### JSON:
- JavaScript Object Notation, a lightweight data-interchange format.

### Parquet:
- Columnar storage format optimized for queries and compression. Prefered for Hadoop.

### ORC:
- Optimized Row Columnar format, optimized for both compression and query performance.

## 7. DataFrame Transformations

### Joins:
- **Inner Join:**
  ```python
  df1.join(df2, df1['col'] == df2['col'], "inner")
  ```
- **Types of Joins**
 ```
    inner
    outer
    left [outer]
    right [outer]
 ```

### Adding/Renaming Columns:
- **Add Column:**
  ```python
  df = df.withColumn("new_column", df["existing_column"] * 2)
  ```
- **Rename Column:**
  ```python
  df = df.withColumnRenamed("old_name", "new_name")
  ```

## 8. Overview of AWS Services

### S3 (Simple Storage Service):
- Object storage service used for storing and retrieving any amount of data.

### EC2 (Elastic Compute Cloud):
- Virtual servers for running applications. Spark can run on EC2 instances, either standalone or in a cluster setup. EMR will use EC2 to create nodes.

### EMR (Elastic MapReduce):
- Managed cluster platform for running big data frameworks like Spark.
- **Cluster Mode:**
  - **Cluster Mode:** Launch a cluster of EC2 instances where Spark runs in a distributed manner. Suitable for larger jobs.
  - **Step Execution:** Define and run jobs as steps within a cluster. This mode allows you to submit Spark jobs and other tasks without managing the cluster lifecycle.
