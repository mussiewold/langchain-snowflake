CREATE WAREHOUSE my_warehouse WITH WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 300 AUTO_RESUME = TRUE;

CREATE DATABASE telecom_db;

CREATE SCHEMA telecom_schema;

CREATE TABLE telecom_schema.customers (
    customer_id STRING,
    name STRING,
    age INT,
    gender STRING,
    tenure INT,
    service STRING,
    monthly_charges FLOAT,
    total_charges FLOAT,
    churn BOOLEAN
);