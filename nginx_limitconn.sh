#! /bin/bash
cp nginx_limitconn /etc/nginx/sites-available/default 
service nginx restart
echo 'http://47.52.164.88/test.php?id=168' 
