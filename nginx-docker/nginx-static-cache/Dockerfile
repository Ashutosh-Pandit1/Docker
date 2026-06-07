FROM nginx:alpine

MAINTAINER Ashutosh Pandit

RUN rm /etc/nginx/nginx.conf

COPY nginx.conf /etc/nginx/nginx.conf

COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/style.css

EXPOSE 83
