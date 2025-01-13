from pyspark.sql import SparkSession
from pyspark.sql import *
from os.path import abspath

warehouse_location = 'hdfs://localhost:9000/user/hive/warehouse'
my_jars='/home/will/apache-hive-3.1.3-bin/lib/mysql-connector-java-8.0.30.jar'


#.config("spark.master", "spark://LAPTOP-F85RETIP.localdomain:7077")
spark = SparkSession.builder.appName("example-pyspark-hdfs")\
.config("spark.master", "local[*]")\
.config("spark.sql.warehouse.dir", warehouse_location)\
.config("javax.jdo.option.ConnectionDriverName", "com.mysql.cj.jdbc.Driver")\
.config("spark.driver.extraClassPath", "/home/will/apache-hive-3.1.3-bin/lib/mysql-connector-java-8.0.30.jar") \
.config("spark.executor.extraClassPath", "/home/will/apache-hive-3.1.3-bin/lib/mysql-connector-java-8.0.30.jar") \
.enableHiveSupport().getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("created Spark Session")
print(spark.sparkContext.getConf().getAll())

#spark.sparkContext.setLogLevel("ERROR")
spark.sql("DROP table IF EXISTS BevA")
spark.sql("create table IF NOT EXISTS BevA(Beverage String,BranchID String) row format delimited fields terminated by ','");
spark.sql("LOAD DATA INPATH '/user/hive/warehouse/Bev_BranchA.txt' INTO TABLE BevA")
spark.sql("SELECT Count(*) AS TOTALCOUNT FROM BevA").show()
spark.sql("SELECT Count(*) AS NumBranch2BevAFile FROM BevA WHERE BevA.BranchID='Branch2'").show()
spark.sql("SELECT * FROM BevA").show()
spark.stop()
