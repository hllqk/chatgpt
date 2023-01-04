<?php
#用php获取https://pixiv.moeyy.xyz/api/illust/random?format=image的重定向跳转后链接并添加到txt
$url = "https://pixiv.moeyy.xyz/api/illust/random?format=image";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
$data = curl_exec($ch);
$headers = curl_getinfo($ch);
curl_close($ch);

$file = fopen('url.txt','a');
fwrite($file, $headers['url']."\r\n");
fclose($file);