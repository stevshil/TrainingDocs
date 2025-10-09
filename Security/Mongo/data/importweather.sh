#!/bin/bash

mongoimport --db='example' --collection='weather' \
--file='/docker-entrypoint-initdb.d/weather.json' \
--type=json --username='root' --password='secret123' \
--authenticationDatabase=admin

mongoimport --db='example' --collection='listings' \
--file='/docker-entrypoint-initdb.d/listingsAndReviews.json' \
--type=json --username='root' --password='secret123' \
--authenticationDatabase=admin
