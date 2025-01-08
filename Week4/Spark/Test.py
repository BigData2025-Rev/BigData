#!/usr/bin/env python

from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "TestApp") #Creates SparkContext

rdd = sc.parallelize([1,2,3,4,5])

print(rdd.collect())

sc.stop()
