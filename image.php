<?php
    $string = "abcdefghijklmnopqrstuvwxyz0123456789";
    $str = "";
    for($i=0;$i<6;$i++){
        $pos = rand(0,35);
        $str .= $string{$pos};
    }
    session_start();
    $_SESSION['img_number'] = $str;
    $img_handle = imagecreate(80, 20);  //图片大小80X20
    $back_color = ImageColorAllocate($img_handle, 255, 255, 255); //背景颜色（白色）
    $txt_color = ImageColorAllocate($img_handle, 0,0, 0);  //文本颜色（黑色）
    Imagefill($img_handle, 0, 0, $back_color);             //填充图片背景色
    ImageString($img_handle, 28, 10, 0, $str, $txt_color);//水平填充一行字符串
    ob_clean();   // ob_clean()清空输出缓存区    
    header("Content-type: image/png"); //生成验证码图片    
    Imagepng($img_handle);//显示图片
?>
