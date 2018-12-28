#! /bin/bash
cp nginx_img /etc/nginx/sites-available/default 
service nginx restart
echo 'http://47.52.164.88/test9.php?id=168' 
