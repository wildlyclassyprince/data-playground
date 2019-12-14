# DvD Rental Pipeline

A pipeline to show the most popularly rented out movies. The data is taken from the `dvdrental` dataset. Data versioning is managed using `dvc`.

## Prerequisites:
```bash
$ cd dvdrental/
$ wget https://jdbc.postgresql.org/download/postgresql-42.2.9.jar
$ mv postgresql-42.2.9.jar ~/anaconda3/lib/site-packages/pyspark/jars
$ pip install -r app/requirements
```

## Run:
```bash
$ python3 app.py
```