# Databricks notebook source
dbutils.fs.ls('/mnt/silver/SalesLT/')

# COMMAND ----------

dbutils.fs.ls('/mnt/gold/')

# COMMAND ----------

input_path = '/mnt/silver/SalesLT/Address/'

# COMMAND ----------

df = spark.read.format('delta').load(input_path)
df

# COMMAND ----------

display(df)

# COMMAND ----------

import re

# COMMAND ----------

df.columns

# COMMAND ----------

import re

# Assuming df is your Spark DataFrame
for old_name in df.columns:
    new_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', old_name)
    df = df.withColumnRenamed(old_name, new_name)

# COMMAND ----------

display(df)

# COMMAND ----------

# Assuming df is your Spark DataFrame
for old_name in df.columns:
    new_name = re.sub(r'([a-z]) ([A-Z])', r'\1_\2', old_name)
    df = df.withColumnRenamed(old_name, new_name)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Transforming all the table columns 

# COMMAND ----------

# storing all table names from SalesLT folder
tables = [i.name.split('/')[0] for i in dbutils.fs.ls('/mnt/silver/SalesLT/')]
tables

# COMMAND ----------

for table in tables:
    #df = spark.read.format('delta').load(f'/mnt/silver/SalesLT/{table}')
    print(f'/mnt/silver/SalesLT/{table}')

# COMMAND ----------

for table in tables:
    df = spark.read.format('delta').load(f'/mnt/silver/SalesLT/{table}')

    columns = df.columns

    for i in columns:
        df = df.withColumnRenamed(i,re.sub('([a-z])([A-Z])',r'\1_\2',i))

    df.write.format('delta').mode('overwrite').save(f'/mnt/gold/SalesLT/{table}/')

# COMMAND ----------

dbutils.fs.ls('/mnt/gold/SalesLT')

# COMMAND ----------

df = spark.read.format('delta').load('/mnt/gold/SalesLT/Address/')
display(df)

# COMMAND ----------


