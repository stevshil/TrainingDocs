FROM almalinux:8
MAINTAINER YourCompanyName
LABEL author="YourName"
# Install apache and php
RUN yum -y install httpd php php-cli php-common php-gd php-json php-intl php-mbstring php-mysqli php-openssl php-pdo php-xml php-zip
RUN mkdir /run/php-fpm
COPY startweb /startweb
COPY info.php /var/www/html
RUN chmod +x /startweb
EXPOSE 80
EXPOSE 443
ENTRYPOINT ["/startweb"]
