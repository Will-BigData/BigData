from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark test")
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Test your Spark session
df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])
df.show()

data = [("John", 28), ("Jane", 25)]
columns = ["Name", "Age"]


df2 = spark.createDataFrame(data, columns)
df2.show()
df3=df2.coalesce(1)

#df3.write.format("csv").mode("overwrite").save("file:///opt/spark/work-dir")


# Get the SparkContext from the SparkSession
sc = spark.sparkContext

# Create an RDD from a collection (e.g., a list)
dataRDD = [1, 2, 3, 4, 5]
rdd = sc.parallelize(dataRDD)

# Perform an action to verify the RDD
print(rdd.collect())  # Output: [1, 2, 3, 4, 5]

