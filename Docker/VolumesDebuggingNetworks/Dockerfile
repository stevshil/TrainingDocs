# Pull specific version of MySQL
FROM mysql:5.7.19
# Set environment variable for MySQL with default value
ENV MYSQL_ROOT_PASSWORD=n3u3d4
# Copy our SQL schema to be loaded at container run time
COPY myschema.sql /docker-entrypoint-initdb.d
# EXPOSE is not required as it is inherited from the FROM image
# EXPOSE 3306
