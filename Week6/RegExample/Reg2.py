from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.ml.linalg import Vectors

sparkSession = SparkSession.builder.appName("example-pyspark-hdfs").getOrCreate()
print("created Spark Session")
#df_load = sparkSession.read.csv("hdfs://localhost:9000/user/will/Advertising.csv")
#df_load.show()
df = sparkSession.read.format('com.databricks.spark.csv').\
    options(header='true',inferschema='true').\
    load("hdfs://localhost:9000/user/will/Advertising.csv",header=True)
df.show(5,True)
df.printSchema()
df.describe().show()

def transData(data):
    return data.rdd.map(lambda r: [Vectors.dense(r[:-1]),r[-1]]).toDF(['features','label'])

transformed= transData(df)
transformed.show(5)

from pyspark.ml import Pipeline
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator
# Automatically identify categorical features, and index them.
# We specify maxCategories so features with > 4 distinct values are treated as continuous.
featureIndexer = VectorIndexer(inputCol="features", \
                               outputCol="indexedFeatures", \
                               maxCategories=4).fit(transformed)

# Split the data into training and test sets (40% held out for testing)
(trainingData, testData) = transformed.randomSplit([0.6, 0.4])

trainingData.show(5)
testData.show(5)

# Import LinearRegression class
from pyspark.ml.regression import LinearRegression
# Define LinearRegression algorithm
lr = LinearRegression()

pipeline = Pipeline(stages=[featureIndexer, lr])
model = pipeline.fit(trainingData)

def modelsummary(model):
    import numpy as np
    print ("Note: the last rows are the information for Intercept")
    print ("##","-------------------------------------------------")
    print ("##"," Estimate | Std.Error | t Values | P-value")
    coef = np.append(list(model.coefficients),model.intercept)
    Summary=model.summary
    for i in range(len(Summary.pValues)):
        print ("##",'{:10.6f}'.format(coef[i]), \
               '{:10.6f}'.format(Summary.coefficientStandardErrors[i]), \
               '{:8.3f}'.format(Summary.tValues[i]), \
               '{:10.6f}'.format(Summary.pValues[i]))
    print ("##",'---')
    print ("##","Mean squared error: % .6f" \
           % Summary.meanSquaredError, ", RMSE: % .6f" \
           % Summary.rootMeanSquaredError )
    print ("##","Multiple R-squared: %f" % Summary.r2, ", \
    Total iterations: %i"% Summary.totalIterations)

modelsummary(model.stages[-1])

# Make predictions.
predictions = model.transform(testData)

predictions.select("features","label","prediction").show(5)

from pyspark.ml.evaluation import RegressionEvaluator
# Select (prediction, true label) and compute test error
evaluator = RegressionEvaluator(labelCol="label",
                                predictionCol="prediction",
                                metricName="rmse")
rmse = evaluator.evaluate(predictions)
print("Root Mean Squared Error (RMSE) on test data = %g" % rmse)

y_true = predictions.select("label").toPandas()
y_pred = predictions.select("prediction").toPandas()
import sklearn.metrics

r2_score = sklearn.metrics.r2_score(y_true, y_pred)
print('r2_score: {0}'.format(r2_score))

##https://runawayhorse001.github.io/LearningApacheSpark/regression.html
