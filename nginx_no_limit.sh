#! /bin/bash
cp nginx_no_limit /etc/nginx/sites-available/default 
service nginx restart
echo 'http://47.52.164.88/test2.php?id=168'
echo 'http://47.52.164.88/test3.html'
echo 'http://47.52.164.88/test4.html'
echo 'http://47.52.164.88/test5.php?id=168'
echo 'http://47.52.164.88/test6.php?id=168'
echo 'http://47.52.164.88/test7.php?id=168'
echo 'http://47.52.164.88/test8.php?id=168'

