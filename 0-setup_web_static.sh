#!/usr/bin/env bash
# install nginx on a new ubuntu server

apt update
apt install -y nginx
service nginx start
apt install -y ufw
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw --force enable
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

# add lines as required
line1="\tserver_name _;"
line2="        location \/hbnb_static\/ \{"
line3="                alias \/data\/web_static\/current\/;"
line4="        \}"
sed -i --follow-symlinks "s/^\s*server_name _;/$line1\n$line2\n$line3\n$line4/" \
        /etc/nginx/sites-enabled/default

# reload nginx
service nginx restart
