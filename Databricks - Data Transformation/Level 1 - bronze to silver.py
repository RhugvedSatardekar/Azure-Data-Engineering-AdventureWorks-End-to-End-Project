# Databricks notebook source
dbutils.fs.ls('/mnt/bronze/SalesLT')

# COMMAND ----------

dbutils.fs.ls('/mnt/silver/')

# COMMAND ----------

input_path = '/mnt/bronze/SalesLT/Address/Address.parquet' # lets perform only for one file 

# COMMAND ----------

df = spark.read.format('parquet').load(input_path) # pyspark dataframe

# COMMAND ----------

display(df)

# COMMAND ----------

# casting the data type of the ModifiedDate column to date 

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

df = df.withColumn("ModifiedDate",date_format(from_utc_timestamp(df.ModifiedDate.cast (TimestampType()), "UTC"), "yyyy/MM/dd"))

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transforming Date columns of all tables 

# COMMAND ----------

table_name= []

for i in dbutils.fs.ls('/mnt/bronze/SalesLT/'):
    table_name.append(i.name.split('/')[0])


# COMMAND ----------

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp,date_format
from pyspark.sql.types import TimestampType

for i in table_name:
    path = '/mnt/bronze/SalesLT/'+ i +'/'+ i +'.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col,date_format(from_utc_timestamp(df[col].cast(TimestampType()),"UTC"),"yyyy-MM-dd"))
    
    output = '/mnt/silver/SalesLT/'+ i + '/'
    df.write.format('delta').mode("overwrite").save(output)
