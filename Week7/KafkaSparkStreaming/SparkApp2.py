from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField

#Use 'spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 SparkApp2.py'

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.master", "local[*]")\
    .getOrCreate()

print("spark session created")
# Define schema for incoming Kafka messages
schema = StructType([
    StructField("id", StringType(), True),
    StructField("value", StringType(), True)
])

# Read stream from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "test-topic") \
    .option("startingOffsets", "earliest")\
    .load()

print("hello")
# Deserialize Kafka message value (JSON)
messages = df.selectExpr("CAST(value AS STRING)") \
    .selectExpr("value as json_string") \
    .selectExpr("CAST(json_string as STRING)")

# Write processed stream to console
query = messages.writeStream \
    .outputMode("append") \
    .format("memory") \
    .queryName("kafka_stream") \
    .option("truncate", "false") \
    .start()

query.awaitTermination(timeout=10)  # Waits 10 seconds for stream to process data
query.stop()  # Stops the stream after processing

# Retrieve the data from the in-memory table
result = spark.sql("SELECT * FROM kafka_stream")
result.show(truncate=False)  # Print the DataFrame content to the terminal



