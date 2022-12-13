Scala

spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar

import spark.implicits._

import org.apache.spark.sql.types._

import org.apache.spark.sql.functions

import java.sql.Timestamp

import org.apache.spark.sql.streaming.Trigger.ProcessingTime

val bucket = "idsaproje2"

spark.conf.set("temporaryGcsBucket", bucket)

spark.conf.set("parentProject", "diesel-octane-371212")

val kafkaDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers","34.75.244.4:9092").option("subscribe","ornek").load

val schema = StructType(List(StructField("name",StringType),StructField("country",StringType),StructField("localtime", StringType),StructField("temp_c",FloatType)))


val activationDF = kafkaDF.select(from_json($"value".cast("string"),schema).alias("activation"))


val df = activationDF.select($"activation"("name").alias("name"),

$"activation"("country").alias("country"),

$"activation"("localtime").alias("localtime"),

$"activation"("temp_c").alias("temp_c"))

val modelCountDF = df.filter($"activation"("temp_c")>0)


val modelCountQuery = modelCountDF.writeStream.outputMode("append").format("bigquery").option("table","idsadb.idsadb_table").option("checkpointLocation", "/path/to/checkpoint/dir/in/hdfs").option("credentialsFile","/home/zsfdsfsfe/diesel.json").option("failOnDataLoss",false).option("truncate",false).start().awaitTermination()







import spark.implicits._

import org.apache.spark.sql.types._

import org.apache.spark.sql.functions

import java.sql.Timestamp

import org.apache.spark.sql.streaming.Trigger.ProcessingTime

val bucket = "idsaproje1"

spark.conf.set("temporaryGcsBucket", bucket)

spark.conf.set("parentProject", "mineral-rune-365815")

val kafkaDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers","34.170.27.9:9092").option("subscribe","ornek").load

val schema = StructType(List(StructField("name",StringType),StructField("country",StringType),StructField("localtime",StringType),StructField("temp_c",FloatType)))
val activationDF = kafkaDF.select(from_json($"value".cast("string"),schema).alias("activation"))
val modelCountDF = activationDF.groupBy($"activation"("name"),$"activation"("country"),$"activation"("localtime"),$"activation"("temp_c")).count.sort($"count".desc)


val modelCountQuery = modelCountDF.writeStream.outputMode("complete").format("bigquery").option("table","idsadb.idsadb_table").option("checkpointLocation", "/path/to/checkpoint/dir/in/hdfs").option("credentialsFile","/home/isteveriseti1/mineral.json").option("failOnDataLoss",false).option("truncate",false).start().awaitTermination()
