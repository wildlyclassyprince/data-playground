'''
A data pipeline for the dvdrental dataset.
'''

# Imports
from json import load
from pyspark.sql import SparkSession

NAME = 'DvD Rental Pipeline'
URL = 'jdbc:postgresql://localhost:5432/dvdrental'
QUERY = '(select * from actor limit 10) as q1'
CONF = '.config/config.json'


def config(file: str) -> dict:
    '''Preliminary configuration.'''
    # Config
    with open(file, 'r') as c:
        config = load(c)
        user = config['user']
        password = config['password']
        driver = config['driver']
    properties = {'user': user, 'password': password, 'driver': driver}
    return properties


def main(properties: dict, url: str, query: str, name: str):
    '''Run app.'''
    spark = SparkSession.builder.appName(name).getOrCreate()
    df = spark.read.jdbc(url=url, table=query, properties=properties)
    df.show()
    df.printSchema()


if __name__ == "__main__":
    properties = config(CONF)
    main(properties, URL, QUERY, NAME)
