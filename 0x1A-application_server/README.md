## Application Server

#### Serve a web app with Nginx and Gunicorn

#### Gunicorn upstart config:

description "Gunicorn application server running myproject"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid user
setgid www-data

env PATH=/home/user/project/projectenv/bin
chdir /home/user/project
exec gunicorn --workers <Number of Workers> --bind <IP:PORT or SOCKET>  <FILE:APP>

#### Nginx Configuration

Server {
    listen 80;
    server_name <DOMAIN || IP>;

    location / {
        include proxy_params;
        proxy_pass <SOCKET || IP>;
    }
}