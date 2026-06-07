FROM nginx:alpine

MAINTAINER Ashutosh Pandit

RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf

COPY error-pages/ /usr/share/nginx/html/

EXPOSE 82

