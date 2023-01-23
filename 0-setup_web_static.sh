#!/usr/bin/env bash
# Setting up airbnb site server

sudo apt update -y

sudo apt install nginx -y

sudo mkdir /data > /dev/null 2>&1

sudo mkdir /data/web_static > /dev/null 2>&1

sudo mkdir /data/web_static/releases > /dev/null 2>&1

sudo mkdir /data/web_static/shared/ > /dev/null 2>&1

sudo mkdir /data/web_static/releases/test > /dev/null 2>&1

sudo touch /data/web_static/releases/test/index.html && echo "Hello world!" > /data/web_static/releases/test/index.html

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

server_config="server {
                listen 80 ;
                listen [::]:80 default_server;
                root /data/web_static/current;
                index index.html index.htm index.nginx-debian.html
                server_name_ mikejourney.tech;
                location / {
                        try_files $uri $uri/ =404;
                }
                if ($request_filename ~ redirect_me){
                        rewrite ^ https://mikejourney.tech/ permanent;
                }
                error_page 404 /error_404.html;
                location = /error_404.html {
                        internal;
                }
}"

sudo echo $server_config >> /etc/nginx/sites-available/default
