'''
A data pipeline for the dvdrental dataset.
'''

# Imports
from json import load
from pyspark.sql import SparkSession

NAME = 'DvD Rental Pipeline'
URL = 'jdbc:postgresql://localhost:5432/dvdrental'
CONF = '.config/config.json'
QUERY1 = '(select * from film) as q1'
QUERY2 = '(select * from inventory) as q2'
QUERY3 = '(select * from rental) as q3'


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


def get_data(properties: dict, url: str, query: str, name: str):
    '''Run app.'''
    spark = SparkSession.builder.appName(name).getOrCreate()
    return spark.read.jdbc(url=url, table=query, properties=properties)


if __name__ == "__main__":
    # Get the data
    properties = config(CONF)
    fil = get_data(properties, URL, QUERY1, NAME)
    inv = get_data(properties, URL, QUERY2, NAME)
    ren = get_data(properties, URL, QUERY3, NAME)

    # Join
    right = fil \
        .join(inv, fil.film_id == inv.film_id)\
        .drop(inv.film_id)
    df = right \
        .join(ren, ren.inventory_id == right.inventory_id) \
        .drop(ren.inventory_id)

    # Group, filter, order and show
    df.groupBy('title') \
        .count() \
        .filter('count > 20') \
        .orderBy('count', ascending=False) \
        .withColumnRenamed('count', 'frequency') \
        .show()
