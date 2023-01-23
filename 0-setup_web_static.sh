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

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default


sudo service nginx restart
