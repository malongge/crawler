
				
<?php
header('Content-Type:application/json');
$servername = "localhost";
$username = "crawler";
$password = "hV1l0Sol";
 
// 创建连接
$mysqli = new mysqli($servername, $username, $password,'crawler');
// 检测连接
if ($mysqli->connect_error) {
    die("连接失败: " . $mysqli->connect_error);
} 
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
    $raw_success = array('classnum' => $classnum, 'price' => $price);
    $res_success = json_encode($raw_success);
    // Feedback for end user
    echo $res_success;
}
mysqli_close($mysqli);
?>

	
		
