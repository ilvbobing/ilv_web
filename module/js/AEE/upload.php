<?php
//定义允许上传的文件扩展名
$ext_arr = array('gif','jpg','png','bmp','swf','mp3','wmv');
//最大文件大小
$max_size = 10000000;
//更改目录权限
@mkdir($save_path, 0777);
//有上传文件时
if (empty($_FILES) === false) {
	//文件保存目录路径
	$save_path = $_POST["AEE_uploadPath"];
	//原文件名
	$file_name = $_FILES['AEE_uploadFile']['name'];
	//服务器上临时文件名
	$tmp_name = $_FILES['AEE_uploadFile']['tmp_name'];
	//文件大小
	$file_size = $_FILES['AEE_uploadFile']['size'];
	//文件的全部路径
	$file_path = $save_path.$_POST['AEE_uploadFinally'];
	//检查目录
	if (@is_dir($save_path) === false) {
		echo '<script type="text/javascript">alert("It was not possible to open destination directory.");</script>';
		exit;
	}
	//检查目录写权限
	if (@is_writable($save_path) === false) {
		echo '<script type="text/javascript">alert("The directory is not writable.");</script>';
		exit;
	}
	//检查是否已上传
	if (@is_uploaded_file($tmp_name) === false) {
		echo '<script type="text/javascript">alert("Possible file upload attack.");</script>';
		exit;
	}
	//检查文件大小
	if ($file_size > $max_size) {
		echo '<script type="text/javascript">alert("The uploaded file exceeds the max_size.");</script>';
		exit;
	}
	//获得文件扩展名
	$file_ext = strtolower(trim(array_pop(explode(".",$file_name))));
	//检查扩展名
	if (in_array($file_ext, $ext_arr) === false) {
		echo '<script type="text/javascript">alert("This type of file is not accepted.");</script>';
		exit;
	}
	//移动文件
	if (move_uploaded_file($tmp_name, $file_path) === false) {
		echo '<script type="text/javascript">alert("Something is wrong with the file.");</script>';
		exit;
	}
	echo '<script type="text/javascript">parent.AEE.popupDiv.innerHTML=\'\';</script>';
}
?>