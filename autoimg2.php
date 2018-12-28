<?php
// autoimg.php
echo $_COOKIE["auth"];

if(preg_match('/testcrawler([a-z0-9]{6})/',$_COOKIE["auth"])){
	
	// 图片真实存放路径
	$imagePath = $_SERVER['DOCUMENT_ROOT'] . '/download/';
		
	// 获取url中的图片名 如 http://localhost/111.jpg 获取值为111.jpg
	$image = trim(parse_url($_SERVER['REQUEST_URI'])['path'], '/');
		
	// 拼接图片真实全路径 如 /home/qii/imgtest/download/111.jpg
	$fullPath = $imagePath . $image;
		
	// 获取图片mime信息 设置Content-type头
	$mime = getimagesize($fullPath)['mime'];
	header("Content-Type: $mime");
	// 设置sendfile头部，让nginx跳转到download下查找对应图片 相当于交给nginx进行后续处理
	header("X-Accel-Redirect: /download/$image");
}else{
	echo "not auth";
}

//if (!isset($_GET['Sign'])) {
//    exit('get img failed!');
//}

?>
