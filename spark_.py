from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize SparkSession (entry point for Spark)
spark = SparkSession.builder \
    .appName("SparkInMemoryHDFS") \
    .master("local[*]") \
    .getOrCreate()

# Simulate data (in practice, this could be read from HDFS)
# Create a sample dataset: list of numbers
numbers = [(i,) for i in range(1, 9)]  # [(1,), (2,), ..., (8,)]
df = spark.createDataFrame(numbers, ["value"])

# Alternative: Read from HDFS (uncomment if using HDFS)
# df = spark.read.csv("hdfs://namenode:8021/input/numbers.csv")

# 1. In-Memory Processing: Filter even numbers and square them
# These are transformations (lazy, executed in memory)
even_df = df.filter(col("value") % 2 == 0)  # Filter: 2, 4, 6, 8
squared_df = even_df.select((col("value") * col("value")).alias("squared_value"))  # Square: 4, 16, 36, 64

# Cache the DataFrame to keep it in memory
squared_df.cache()

# 2. Distributed Nature: Data is partitioned (visible in Spark UI or logs)
# Check number of partitions (simulates distribution across cluster)
print(f"Number of partitions: {squared_df.rdd.getNumPartitions()}")

# 3. Action: Trigger computation to compute sum
# This executes the DAG in memory across partitions
result = squared_df.agg({"squared_value": "sum"}).collect()[0][0]
print(f"Sum of squared even numbers: {result}")

# 4. Write result to HDFS (simulated with local file)
# Save as CSV (in practice, this would write to HDFS)
squared_df.write.csv("output/squared_numbers", mode="overwrite")

# Alternative: Write to HDFS (uncomment if using HDFS)
# squared_df.write.csv("hdfs://namenode:8021/output/squared_numbers", mode="overwrite")

# Stop SparkSession
spark.stop()