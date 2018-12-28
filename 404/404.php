<?php 
$string = "abcdefghijklmnopqrstuvwxyz0123456789";
$str = "";
for($i=0;$i<6;$i++){
    $pos = rand(0,35);
    $str .= $string{$pos};
}
echo $str;
$value = 'testcrawler'.$str;
#echo "sdfasdfwe";
#echo $value;
setcookie("auth", $value,time()+3600,"/");
#setcookie("auth", $value, time()+3600);  /* 1 小时过期  */
#setcookie("TestCookie", $value, time()+3600, "/~rasmus/", "example.com", 1);
header("Location:/index.html");
#echo"<script>history.go(-1);</script>"
?>
