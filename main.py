import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')

# Part 1:

'''
# Step 1
employees = pd.read_sql("""
SELECT *
    FROM employees;
""", conn)

print(employees)

# Step 2
pd.read_sql("""
SELECT *
 FROM employees
WHERE firstName = "Leslie";
""", conn)

# Step 3
pd.read_sql("""
SELECT firstName, lastName, jobTitle
 FROM employees
WHERE firstName = "Leslie";
""", conn)

# Step 4
# Strictly less than 5
pd.read_sql("""
SELECT *, length(lastName) AS name_length
 FROM employees
WHERE name_length < 5;
""", conn)

# OR

# Less than or equal to 4.
pd.read_sql("""
SELECT *, length(lastName) AS name_length
 FROM employees
WHERE name_length <= 4;
""", conn)
'''

# Part 2:
orders = pd.read_sql("""
SELECT *
 FROM orderDetails;
""", conn)

print(orders)

pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
 FROM orderDetails
WHERE rounded_price_int >= 100;
""", conn)

pd.read_sql("""
SELECT *
 FROM orders;
""", conn)

pd.read_sql("""
SELECT *, strftime("%Y", orderDate) AS year
 FROM orders
WHERE year = "2005";
""", conn)

pd.read_sql("""
SELECT *
 FROM employees
WHERE jobTitle LIKE "Sale%";
""", conn)

pd.read_sql("""
SELECT COUNT(priceEach)
 FROM orderDetails
WHERE priceEach >=200;
""", conn)

conn.close()