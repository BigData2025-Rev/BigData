# Spark Streaming Instructions

## Set up a data server

Open a terminal and run the following command:

```
nc -lk 9999
```

This is where you will send data.

## Structured Streaming with Dataframes

Open pyspark shell, then run the following:

```
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

# Split the lines into words
words = lines.select(explode(split(lines.value, " ")).alias("word"))

# Generate running word count
wordCounts = words.groupBy("word").count()

query = wordCounts.writeStream.outputMode("complete").format("console").start()
```

When you type in the first terminal, your output should appear in the pyspark shell.