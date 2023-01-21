FROM httpd:2.4
MAINTAINER YourCompanyName
LABEL author="YourName"
# Install apache and php
RUN apt update
RUN apt -y install libapache2-mod-php
RUN ln -sf /dev/stdout /var/log/apache2/access.log
RUN ln -sf /dev/stderr /var/log/apache2/error.log
COPY info.php /var/www/html
ENV APACHE_CONFDIR=/etc/apache2
ENV APACHE_RUN_DIR=/var/run/apache2
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2/pid
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
ENTRYPOINT ["apache2","-d","/etc/apache2","-DFOREGROUND"]
