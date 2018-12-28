
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>CSS覆盖leftleft 算术</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, target-densitydpi=device-dpi, minimal-ui">
	<style type="text/css">
body{
  width:950px;
}
</style>
  </head>
  
  <body>
  <div id="app" data-server-rendered="true">
    <div class="index-page">
		<div >
			<div class="special-course-view" data-v-294d1676>
				<div class="course__title" data-v-2c02addf>
				<h3 data-v-2c02addf>CSS覆盖leftleft 算术</h3>
				</div> 
				<div class="subject-teacher" data-v-2c02addf>
					<div class="xue-card-info" data-v-2c02addf>
						<div class="xue-card-subject-avatar xue-avatar-style1" data-v-2c02addf>
							<span data-v-2c02addf>
								<img src="111.png" data-v-2c02addf>
							</span>
						</div> 
					</div> 
				</div>
				<div class="xue-course-start" data-v-2c02addf>
				
<?php
header('Content-type:text/html; charset=UTF-8');
$servername = "localhost";
$username = "crawler";
$password = "hV1l0Sol";
 
// 创建连接
$mysqli = new mysqli($servername, $username, $password,'crawler');
// 检测连接
if ($mysqli->connect_error) {
    die("连接失败: " . $mysqli->connect_error);
} 
echo "<!--连接成功-->";
//    define('DB_HOST','localhost');
//    define('DB_USER','root');
//    define('DB_PWD','345823');//密码
//    define('DB_NAME','trigkit');
//
//    //连接数据库
//    $connect = mysql_connect(DB_HOST,DB_USER,DB_PWD) or die('数据库连接失败，错误信息：'.mysql_error());
//
//    //选择指定数据库，设置字符集
//    mysql_select_db(DB_NAME,$connect) or die('数据表连接错误，错误信息：'.mysql_error());
//    mysql_query('SET NAMES UTF8') or die('字符集设置出错'.mysql_error());
// Get input
$id = $_REQUEST[ 'id' ];
//mysql_query('SET NAMES UTF8') or die('字符集设置出错'.mysql_error());
mysqli_set_charset($mysqli,utf8);
//mysqli_query('SET NAMES UTF8') or die('字符集设置出错'.mysqli_error());; 
// Check database
$query  = "SELECT classnum, price FROM crawler WHERE pageid = '$id';";
$result = mysqli_query($mysqli,  $query ) or die( '<pre>' . ((is_object($mysqli)) ? mysqli_error($mysqli) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );
//echo $result;
// Get results
while( $row = mysqli_fetch_assoc( $result ) ) {
    // Get values
    //echo $row;
    $classnum = $row["classnum"];
    $price  = $row["price"];
    $length=strlen($price);
    // Feedback for end user
    echo '<!--'.$price.' -->';
    echo '
		<div class="xue-course-start__time" data-v-2c02addf><span class="course-all-num" data-v-2c02addf>共'.$classnum.'讲</span>
					</div> 
					<div class="xue-course-start__course-price" data-v-2c02addf>
						<span class="discount-price" data-v-2c02addf>
						    优惠价:<span class="price-unit" data-v-2c02addf>￥</span></sapn>
				
	';
    switch ($length)
    {
    case 1:
      echo "Number 1";
      break;
    case 2:
      echo '
<span >
<b>
<i style="width:10px;">'.$price[0].'</i>
<i style="width:10px;">'.$price[0].'</i>
<i style="width:10px;color:#fff">'.$price[1].'</i>
<i style="width:10px;color:#fff">'.$price[0].'</i>
</b>
<b><i style="width:18px;left:-28px;background:#fff;color:#fff;position: relative;">'.$price[0].'</i></b>
<b><i style="width:18px;left:-57px;background:#fff;position: relative;">'.$price[1].'</i></b>
</span>';
      break;
    case 3:
      echo '
<span >
<b>
<i style="width:10px;">'.$price[0].'</i>
<i style="width:10px;">'.$price[1].'</i>
<i style="width:10px;">7</i>
<i style="width:10px;color:#fff">5</i>
</b>
<b><i style="width:10px;left:-28px;background:#fff;position: relative;">'.$price[2].'</i></b>
</span>';
      break;
    case 4:
      echo '
<span >
<b>
<i style="width:10px;">'.$price[0].'</i>
<i style="width:10px;">'.$price[0].'</i>
<i style="width:10px;">'.$price[0].'</i>
<i style="width:10px;">'.$price[3].'</i>
</b>
<b><i style="width:18px;left:-28px;background:#fff;position: relative;">'.$price[2].'</i></b>
<b><i style="width:18px;left:-57px;background:#fff;position: relative;">'.$price[1].'</i></b>
</span>';
      break;
    default:
      echo "No number between 1 and 3";
    }

}
mysqli_close($mysqli);
?>

				</div></div></div>
<?php
$s = $id-1;
$x = $id+1;

echo '				
<a href="test6.php?id='.$s.'">上一篇</a>
<a href="test6.php?id='.$x.'">下一篇</a>				
'
?>				
	
		
 <!----></div> <div class="footer" data-v-622986ff><div class="page-footer" data-v-622986ff><div class="foot" data-v-622986ff><span class="left" data-v-622986ff><span data-v-622986ff>使用元素位移，对元素进行覆盖</span><br> <span data-v-622986ff>注册</span></span> <span class="right" data-v-622986ff><a href="/index/" data-xeslog-params="key=xeslog-index-touch&amp;action=click-index-touch&amp;click_id=3.11.1&amp;api_id=&amp;target_id=3.1.0" class="router-link-exact-active router-link-active" data-v-622986ff>首页</a>
        |
        |
    </div></div></div> <!----></div>
  </body>
</html>

