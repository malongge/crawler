<?php
// autoimg.php
$getexpires=$_REQUEST[ 'Expires' ];
$getsigned=$_REQUEST[ 'Sign' ];
$accessKeyId="nz2pc56s936lznjt3pdx7lch"; 
$accessKeySecret="secret_key"; 
$authsigned = base64_encode(hash_hmac("sha1", $getexpires, $accessKeySecret, true));
// 假设sign参数为校验参数，有该参数即可通过验证，否则不通过
echo time();
echo "\n";
echo $getexpires;
echo "\n";
echo $authsigned;
echo "\n";
echo $getsigned;
if(time()<=$getexpires){
	if ($authsigned==$getsigned){
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
		echo "校验失败";
	}
}else{
	echo "时间戳过期";
}

//if (!isset($_GET['Sign'])) {
//    exit('get img failed!');
//}

?>
