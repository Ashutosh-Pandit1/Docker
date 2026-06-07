FROM nginx:alpine

MAINTAINER Ashutosh Pandit

WORKDIR /app

RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /usr/share/nginx/html/app1 /usr/share/nginx/html/app2

COPY index-app1.html /usr/share/nginx/html/app1/index.html
COPY index-app2.html /usr/share/nginx/html/app2/index.html

EXPOSE 81
