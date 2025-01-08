#!/usr/bin/env python

from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "TestApp") #Creates SparkContext

rdd = sc.parallelize([1,2,3,4,5])

print(rdd.collect())

pokemon_rdd = sc.textFile("/user/will2/Pokemon.csv")

pokemon_rdd_list = pokemon_rdd.map(lambda x: x.split(","))

print(pokemon_rdd_list.take(5))

pokemon_rdd_list.saveAsTextFile("/user/will2/pyspark_ex_out")

sc.stop()
