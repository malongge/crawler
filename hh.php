<?php
    $string = "3479";
    $img_handle = imagecreate(80, 20);  //图片大小80X20
    $back_color = ImageColorAllocate($img_handle, 255, 255, 255); //背景颜色（白色）
    $txt_color = ImageColorAllocate($img_handle, 0,0, 0);  //文本颜色（黑色）
    Imagefill($img_handle, 0, 0, $back_color);             //填充图片背景色
    ImageString($img_handle, 28, 10, 0, $string, $txt_color);//水平填充一行字符串
    ob_clean();   // ob_clean()清空输出缓存区    
    header("Content-type: image/png"); //生成验证码图片    
    Imagepng($img_handle);//显示图片
    Imagepng($img_handle,'price.png');
?>
