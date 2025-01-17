from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example-pyspark-hdfs")\
.config("spark.master", "spark://LAPTOP-F85RETIP.localdomain:7077")\
.getOrCreate()

sc = spark.sparkContext

df1 = spark.read.option("multiline", "True").json("/user/will/people.json")
df1.show()
df2=spark.read.format("csv").option("sep","\t").load("/user/will/people.txt")
df2.show()
df3 = spark.read.csv("/user/will/people.csv")
df3.show()
df1.printSchema()

df1.select(df1["name"]).show()
df1.select(df1["age"] +1).show()
df = sc.parallelize([(4, "blah", 2),(2, "", 3),(56, "foo", 3),(100, None, 5)]).toDF(["A", "B", "C"])
df.show()

from pyspark.sql.functions import when

newDf = df.withColumn("D", when(df["B"].isNull(),0).when(df["B"] == "", 0).otherwise(1))

df4 = spark.createDataFrame(data=[(1,2)], schema=["x","y"])
#or better

from pyspark.sql.types import StructType,StructField, IntegerType
Schema= StructType([StructField("x",IntegerType(),True),StructField("y",IntegerType(),True)])
df4 = spark.createDataFrame(data=[(1,2)], schema=Schema)
df4.printSchema()


import pyspark.sql.functions as pysf

myExpression = "x+y"
df4.withColumn("z",pysf.expr(myExpression)).show()


data=[("James","Bond"),("Jason","Bourne")]
df5=spark.createDataFrame(data).toDF("col1","col2")
df5.withColumn("Name",pysf.expr(" col1 ||','|| col2")).show()


df6 = spark.createDataFrame(data=[
	("steak", 1, 1, 150),
	("steak", 2, 2, 180),
	("fish", 3, 3, 100)
	]).toDF("C1", "C2", "C3", "C4")

df6.withColumn("C5", pysf.expr("C2/(C3 + C4)")).show()


#Spark column string replace when present in other column (row)

df7 = spark.createDataFrame([
  ("Hi I heard about Spark", "Spark"),
  ("I wish Java could use case classes", "Java"),
  ("Logistic regression models are neat", "models")
]).toDF("sentence", "label")


replace = pysf.udf(lambda data, rep : data.replace(rep, ""))
res = df7.withColumn("sentence_without_label", replace("sentence" , "label"))
res.show(truncate=False)


#Drop duplicates

data = sc.parallelize([("Foo",41,"US",3),
	("Foo",39,"UK",1),
	("Bar",57,"CA",2),
	("Bar",72,"CA",2),
	("Baz",22,"US",6),
("Baz",36,"US",6)]).toDF(["x","y","z","count"])

data.dropDuplicates(["x","count"]).show()

dataset = spark.createDataFrame([(0, "hello"), (1, "world")]).toDF("id", "text")
upper= lambda String: String.upper()

upperUDF = pysf.udf(upper)
dataset.withColumn("upper", upperUDF("text")).show()

dataFrame = spark.createDataFrame([("10.023", "75.0125", "00650"),
	("12.0246", "76.4586", "00650"),
	("10.023", "75.0125", "00651")]).toDF("lat","lng", "zip")
dataFrame.printSchema()
dataFrame.select(["*"]).where(dataFrame["zip"] == "00650").show()

#or
dataFrame.select("*").where(dataFrame.zip== "00650").show()

#Join Operations in spark
emp = [(1,"Smith",-1,"2018","10","M",3000),
	(2,"Rose",1,"2010","20","M",4000),
 	(3,"Williams",1,"2010","10","M",1000),
	(4,"Jones",2,"2005","10","F",2000),
	(5,"Brown",2,"2010","40","",-1),
	(6,"Brown",2,"2010","50","",-1)
	]
empColumns = ["emp_id","name","superior_emp_id","year_joined",
	"emp_dept_id","gender","salary"]

empDF = spark.createDataFrame(data = emp, schema=empColumns)
empDF.show()
empDF.printSchema()

dept = [("Finance",10),
	("Marketing",20),
	("Sales",30),
	("IT",40)
	]

deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema=deptColumns)
deptDF.show()

empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"inner").show()
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"outer").show()
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"full").show()
empDF.join(deptDF,empDF.emp_dept_id ==  deptDF.dept_id,"fullouter").show()


#Spark aggregate

simpleData = [("James","Sales","NY",90000,34,10000),
	("Michael","Sales","NY",86000,56,20000),
	("Robert","Sales","CA",81000,30,23000),
	("Maria","Finance","CA",90000,24,23000),
	("Raman","Finance","CA",99000,40,24000),
	("Scott","Finance","NY",83000,36,19000),
	("Jen","Finance","NY",79000,53,15000),
	("Jeff","Marketing","CA",80000,25,18000),
	("Kumar","Marketing","NY",91000,50,21000)
]
df = spark.createDataFrame(simpleData).toDF(*["employee_name","department","state","salary","age","bonus"])
df.show()

df.groupBy("department").count().show()
df.groupBy("department").avg("salary").show()
df.groupBy("department").sum("salary").show()
df.groupBy("department").min("salary").show()
df.groupBy("department").max("salary").show()
df.groupBy("department").mean("salary").show()

df.groupBy("department","state").sum("salary","bonus").show()
df.groupBy("department","state").avg("salary","bonus").show()
df.groupBy("department","state").max("salary","bonus").show()
df.groupBy("department","state").min("salary","bonus").show()
df.groupBy("department","state").mean("salary","bonus").show()
df.groupBy("department","state").sum("salary","bonus").show()

from pyspark.sql.functions import *

df.groupBy("department").agg(sum("salary").alias("sum_salary"),avg("salary").alias("avg_salary"),sum("bonus").alias("sum_bonus"),max("bonus").alias("max_bonus")).show()
df.groupBy("department").agg(sum("salary").alias("sum_salary"),avg("salary").alias("avg_salary"),sum("bonus").alias("sum_bonus"),stddev("bonus").alias("stddev_bonus")).where(col("sum_bonus") > 50000).show()

spark.stop()
