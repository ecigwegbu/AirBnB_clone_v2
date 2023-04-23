#!/usr/bin/env bash
# install nginx on a new ubuntu server

sudo apt update
sudo apt upgrade -y
sudo apt install -y nginx
sudo service nginx start
sudo apt install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw --force enable
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# add lines as required
line1="\tserver_name localhost;"
line2="        location \/hbnb_static\/ \{"
line3="                alias \/data\/web_static\/current\/;"
line4="        \}"
sudo sed -i --follow-symlinks "s/^\s*server_name localhost;/$line1\n$line2\n$line3\n$line4/" \
        /etc/nginx/sites-enabled/default

# reload nginx
sudo service nginx restart
