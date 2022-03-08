# Databricks notebook source
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

from test_python import *

print(hello("tristen"))

# COMMAND ----------

x = 1
y = 2

z = add_them(x, y)

print(z)
