FROM httpd:2.4
MAINTAINER YourCompanyName
LABEL author="YourName"
# Install apache and php
RUN apt update
RUN apt -y install libapache2-mod-php
COPY startweb /startweb
COPY info.php /var/www/html
RUN chmod +x /startweb
ENTRYPOINT ["/startweb"]
