<!-- 可以使用PHP的cURL库来实现下载Pixiv图片的功能。

首先，需要使用cURL库获取Pixiv图片的URL，然后使用cURL库下载图片到本地。

下面是一个使用cURL库下载Pixiv图片的示例代码： -->

<?php 
// 设置Pixiv图片的URL 
$url = 'http://i2.pixiv.net/img-original/img/2018/07/03/00/00/13/71736891_p0.jpg'; 

// 初始化一个cURL会话 
$ch = curl_init(); 

// 设置cURL会话的选项 
curl_setopt($ch, CURLOPT_URL, $url); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 

// 执行cURL会话 
$data = curl_exec($ch); 

// 关闭cURL会话 
curl_close($ch); 

// 保存图片 
$fp = fopen('pixiv_image.jpg', 'wb'); 
fwrite($fp, $data); 
fclose($fp); 
?>