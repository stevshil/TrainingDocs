FROM node:16 AS compile
RUN git clone https://github.com/rat9615/simple-nodejs-app.git /web
WORKDIR /web
RUN npm install

FROM node:16
# OK to copy files
RUN mkdir /app
COPY --from=compile /web/index.js /web/package-lock.json /web/package.json /app
# Directories must be created as only files are copied
RUN mkdir /app/node_modules
COPY --from=compile /web/node_modules /app/node_modules
RUN mkdir /app/views
COPY --from=compile /web/views /app/views
WORKDIR /app
EXPOSE 3000
ENTRYPOINT ["npm","start"]
