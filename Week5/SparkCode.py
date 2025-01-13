from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example-rdds")\
        .config("spark.master","local[*]")\
        .getOrCreate()

sc = spark.sparkContext

df2 = spark.read.format("csv").option("sep","\t").load("/user/will/people.txt")
print(df2.show())

rdd1 = sc.parallelize(["jan","feb"])
type(rdd1)
rdd1.collect()

words = sc.parallelize(["ja","feb","kiojh"])
wordpair = words.map(lambda w: (w[0], w))
print(wordpair.collect())

a = sc.parallelize(["dog","almon"])
a.getNumPartitions()
a1=a.repartition(2)
a1.getNumPartitions()
a2 = a1.coalesce(1)
a2.getNumPartitions()
b = a1.map(lambda x: len(x))
print(b.collect())
c = a1.zip(b)
print(c.collect())


spark.stop()
