from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructType, StructField

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
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()

