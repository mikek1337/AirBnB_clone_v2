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

