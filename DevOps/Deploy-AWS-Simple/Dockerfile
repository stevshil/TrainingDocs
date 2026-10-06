FROM node:22-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM httpd:2.4-alpine AS runtime
RUN sed -i 's/^#LoadModule rewrite_module/LoadModule rewrite_module/' /usr/local/apache2/conf/httpd.conf \
    && sed -i 's|^#Include conf/extra/httpd-vhosts.conf|Include conf/extra/httpd-vhosts.conf|' /usr/local/apache2/conf/httpd.conf

COPY apache/000-default.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf
COPY --from=build /app/dist/ /usr/local/apache2/htdocs/

EXPOSE 80