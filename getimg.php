<?php
//用php爬取bing有关二次元动漫图片链接并逐行添加到TXT
//设置脚本超时时间
set_time_limit(0);
//初始化一个新文件
$file = fopen("bingpic.txt", "w") or die("Unable to open file!");
//设置bing搜索关键字
$keywords = '二次元动漫';
//设置bing搜索结果页数
$pages = 10;
//循环抓取搜索结果
for ($i=0; $i < $pages; $i++) { 
    //拼接bing搜索url
    $url = 'http://cn.bing.com/images/search?q='.$keywords.'&first='.$i*35+1;
    //使用file_get_contents抓取搜索结果
    $html = file_get_contents($url);
    //使用正则表达式匹配出图片链接
    preg_match_all('/<img\ssrc=\"(.*?)\"/', $html, $matches);
    //循环遍历匹配出的图片链接
    foreach ($matches[1] as $key => $value) {
        //将图片链接添加到文件中
        fwrite($file, $value."\r\n");
    }
}
//关闭文件
fclose($file);
?>