# Databricks notebook source
1+1

# COMMAND ----------

dataFrame = spark.read.option("inferSchema", True).csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
dataFrame.write.saveAsTable("diamonds")