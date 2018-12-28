#! /bin/bash
cp nginx_img2 /etc/nginx/sites-available/default 
service nginx restart
echo 'http://47.52.164.88/test.php10?id=168' 
