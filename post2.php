<style type="text/css">
.table {
    font-family:Arial, Helvetica, sans-serif;
    font-size:12px;
    color:#333;
    background-color:#E4E4E4;
}
.table td {
    background-color:#F8F8F8;
}
</style>


<form id="form1" name="form1" method="post" action="post2.php">
    <input type="text" name="code" />
    <img  src="image.php" id = "refresh" title="刷新验证码" align="absmiddle" onclick="document.getElementById('refresh').src='image.php' ">
    <font >点击图片刷新</font>
    <input name="Submit" type="submit" value="登录"/>
</form>

<?php
session_start();
header("Content-Type:text/html;charset=utf-8");
#$_SESSION['count'] = $_SESSION['count'] - 1;
if(isset($_REQUEST['Submit'])){
if($_POST['code'] == $_SESSION['img_number']){
    echo "验证码正确";
    $_SESSION['count'] = $_SESSION['count'] + 2;
    # echo"<script>history.go(-1);</script>";  
    header("Location:test2.php");
}else{
    echo "验证码错误";
}
}
?>

