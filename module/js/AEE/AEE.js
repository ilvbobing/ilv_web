/*********************************************************************************************************************
 * 名称:附件上传位置 3.1.0
 * 功能:实现所见即所得编辑（WYSWYG）
 * 时间:2010年7月30日06时51分
 * 地点:政治处
 * 作者:闲庭信步
 * QQ:445424680
 * 邮箱 :445424680@qq.com
*********************************************************************************************************************/
/*********************************************************************************************************************
 * 1 设置常量
 * 2 预设函数
 * 3 动态函数　脚本入口　AEE.show
 * 4 工具函数
*********************************************************************************************************************/

/*********************************************************************************************************************
 * 1 设置常量
 * 1.1 判断浏览器
 * 1.2 AEE.colors 颜色数组
 * 1.3 AEE.fontFamilys 字体数组
 * 1.4 AEE.icons 工具栏图标数组
 * 1.5 AEE.signs 符号数组
 * 1.6 AEE.imageTypes 图片文件类型列表
 * 1.7 AEE.mediaTypes 视频文件类型数组
 * 1.8 AEE.flashTypes Flash文件类型数组
 * 1.9 AEE.language 程序术语
*********************************************************************************************************************/
/*********************************************************************************************************************
 * 创建全局类 An Easy Editor
*********************************************************************************************************************/
AEE = {};
/*********************************************************************************************************************
 * 1 设置常量
*********************************************************************************************************************/
/*********************************************************************************************************************
 * 1.1 判断浏览器
*********************************************************************************************************************/
AEE.ua = navigator.userAgent.toLowerCase()
AEE.viewer = "firefox"
if(AEE.ua.match(/.*msie.*/)){
    AEE.viewer = "ie"
}
/*********************************************************************************************************************
 * 1.2 AEE.colors 颜色数组
*********************************************************************************************************************/
AEE.colors = [//颜色数组
"#FF0000", "#FFFF00", "#00FF00", "#00FFFF", "#0000FF", "#FF00FF", "#FFFFFF", "#F5F5F5", "#DCDCDC", "#FFFAFA",
"#D3D3D3", "#C0C0C0", "#A9A9A9", "#808080", "#696969", "#000000", "#2F4F4F", "#708090", "#778899", "#4682B4",
"#4169E1", "#6495ED", "#B0C4DE", "#7B68EE", "#6A5ACD", "#483D8B", "#191970", "#000080", "#00008B", "#0000CD",
"#1E90FF", "#00BFFF", "#87CEFA", "#87CEEB", "#ADD8E6", "#B0E0E6", "#F0FFFF", "#E0FFFF", "#AFEEEE", "#00CED1",
"#5F9EA0", "#48D1CC", "#00FFFF", "#40E0D0", "#20B2AA", "#008B8B", "#008080", "#7FFFD4", "#66CDAA", "#8FBC8F",
"#3CB371", "#2E8B57", "#006400", "#008000", "#228B22", "#32CD32", "#00FF00", "#7FFF00", "#7CFC00", "#ADFF2F",
"#98FB98", "#90EE90", "#00FF7F", "#00FA9A", "#556B2F", "#6B8E23", "#808000", "#BDB76B", "#B8860B", "#DAA520",
"#FFD700", "#F0E68C", "#EEE8AA", "#FFEBCD", "#FFE4B5", "#F5DEB3", "#FFDEAD", "#DEB887", "#D2B48C", "#BC8F8F",
"#A0522D", "#8B4513", "#D2691E", "#CD853F", "#F4A460", "#8B0000", "#800000", "#A52A2A", "#B22222", "#CD5C5C",
"#F08080", "#FA8072", "#E9967A", "#FFA07A", "#FF7F50", "#FF6347", "#FF8C00", "#FFA500", "#FF4500", "#DC143C",
"#FF0000", "#FF1493", "#FF00FF", "#FF69B4", "#FFB6C1", "#FFC0CB", "#DB7093", "#C71585", "#800080", "#8B008B",
"#9370DB", "#8A2BE2", "#4B0082", "#9400D3", "#9932CC", "#BA55D3", "#DA70D6", "#EE82EE", "#DDA0DD", "#D8BFD8",
"#E6E6FA", "#F8F8FF", "#F0F8FF", "#F5FFFA", "#F0FFF0", "#FAFAD2", "#FFFACD", "#FFF8DC", "#FFFFE0", "#FFFFF0",
"#FFFAF0", "#FAF0E6", "#FDF5E6", "#FAEBD7", "#FFE4C4", "#FFDAB9", "#FFEFD5", "#FFF5EE", "#FFF0F5", "#FFE4E1"
];
/*********************************************************************************************************************
 * 1.3 AEE.fontFamilys 字体数组
*********************************************************************************************************************/
AEE.fontFamilys = [//字体名称数组
	'宋体','黑体','仿宋_GB2312','楷体_GB2312','新宋体','Arial','Arial Black','Times New Roman','Courier New',
	'Tahoma','Verdana','GulimChe', 'MS Gothic'
];
/*********************************************************************************************************************
 * 1.4 AEE.icons 工具栏图标数组
*********************************************************************************************************************/
AEE .icons = [//图标名称数组:['代号','名称','执行方法']
	['source','源码编辑','AEE.changeMode(this);'],
	['print','打印','AEE.designDoc.execCommand(\'print\',false,null);'],
	['preview','预览','AEE.preview(\'preview\');'],

	['cut','剪切','AEE.designDoc.execCommand(\'cut\',false,null);'],
	['copy','复制','AEE.designDoc.execCommand(\'copy\',false,null);'],
	['paste','粘贴','AEE.designDoc.execCommand(\'paste\',false,null);'],
	['undo','撤消','AEE.designDoc.execCommand(\'undo\',false,null);'],
	['redo','重做','AEE.designDoc.execCommand(\'redo\',false,null);'],
	['selectall','全选','AEE.designDoc.execCommand(\'selectall\',false,null);'],
	['link','插入超链接','AEE.insertLink(this);'],
	['unlink','取消链接','AEE.designDoc.execCommand(\'unlink\',false,null);'],
	['table','插入表格','AEE.insertTable(this);'],
	['date','插入日期和时间','AEE.insertDate(this);'],
	['title','大纲标题','AEE.insertTitle(this);'],
	['fontFamily','文本字体','AEE.showFontTable(this,\'fontFamily\',AEE.fontFamilys,\'font-family\',\'fontname\');'],
	['size','字体大小','AEE.insertSize(this)'],
	['superscript','上标','AEE.designDoc.execCommand(\'superscript\',false,null);'],
	['subscript','下标','AEE.designDoc.execCommand(\'subscript\',false,null);'],
	['color','文字颜色','AEE.showColorTable(this,\'color\');'],
	['background','背景颜色','AEE.showColorTable(this,\'background\');'],
	['bold','加粗','AEE.designDoc.execCommand(\'bold\',false,null);'],
	['italic','倾斜','AEE.designDoc.execCommand(\'italic\',false,null);'],
	['underline','下划线','AEE.designDoc.execCommand(\'underline\',false,null);'],
	['strikethrough','删除线','AEE.designDoc.execCommand(\'strikethrough\',false,null);'],
	['justifyleft','左对齐','AEE.designDoc.execCommand(\'justifyleft\',false,null);'],
	['justifycenter','居中对齐','AEE.designDoc.execCommand(\'justifycenter\',false,null);'],
	['justifyright','右对齐','AEE.designDoc.execCommand(\'justifyright\',false,null);'],
	['justifyfull','分散对齐','AEE.designDoc.execCommand(\'justifyfull\',false,null);'],
	['insertorderedlist','编号','AEE.designDoc.execCommand(\'insertorderedlist\',false,null);'],
	['insertunorderedlist','项目符号','AEE.designDoc.execCommand(\'insertunorderedlist\',false,null);'],
	['indent','右缩进','AEE.designDoc.execCommand(\'indent\',false,null);'],
	['outdent','左缩进','AEE.designDoc.execCommand(\'outdent\',false,null);'],
	['hr','插入彩色分割线','AEE.insertHr(this);'],
	['sign','插入特殊符号','AEE.insertSign(this);'],
	['image','插入图片','AEE.showUploadWin(this,\'image\');'],
	['flash','插入Flash','AEE.showUploadWin(this,\'flash\');'],
	['media','插入视频','AEE.showUploadWin(this,\'media\');'],
	['layer','插入彩色层','AEE.showColorTable(this,\'layer\');'],
	['mood','插入心情图标','AEE.insertMood(this);'],

	['removeformat','去除格式','AEE.designDoc.execCommand(\'removeformat\',false,null);'],
	['about','关于','alert(AEE.name+\' \'+AEE.version);']
];
/*********************************************************************************************************************
 * 1.5 AEE.signs 符号数组
*********************************************************************************************************************/
	AEE.signs = [//符号数组
	'§','№','☆','★','○','●','◎','◇','◆','□','℃','‰','■','△','▲','※',
	'→','←','↑','↓','〓','¤','°','＃','＆','＠','＼','︿','＿','￣','―','α',
	'β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ',
	'σ','τ','υ','φ','χ','ψ','ω','≈','≡','≠','＝','≤','≥','＜','＞','≮',
	'≯','∷','±','＋','－','×','÷','／','∫','∮','∝','∞','∧','∨','∑','∏',
	'∪','∩','∈','∵','∴','⊥','∥','∠','⌒','⊙','≌','∽','〖','〗','【','】'
    ];
/*********************************************************************************************************************
 * 1.6 AEE.imageTypes 图片文件类型列表
*********************************************************************************************************************/
AEE.imageTypes = ['.gif','.jpg','.bmp','.png','.JPG'];
/*********************************************************************************************************************
 * 1.7 AEE.mediaTypes 视频文件类型数组
*********************************************************************************************************************/
AEE.mediaTypes = ['.mp3','.wma','.wmv','.rm','.asf'];
/*********************************************************************************************************************
 * 1.8 AEE.flashTypes Flash文件类型数组
*********************************************************************************************************************/
AEE.flashTypes = ['.swf'];
/*********************************************************************************************************************
 * 1.9 AEE.language 程序术语
*********************************************************************************************************************/
AEE.language = {
	cancel : '取消', confirm : '确定',
	flashError : 'Flash格式不对,只接受swf',
	height : '插件高度必须为正整数',
	idError : '请输入正确的文本域id', imageError : '图片格式不对，只接受gif/jpg/png/bmp',
	linkBlank:'空白窗口',linkError:'文字和地址不能为空',linkHref:'跳转地址',linkSelf:'当前窗口',linkTarget:'目标窗口',linkValue:'显示文字',
	local : '本地',
	media : '视频格式不对，只接受mp3/wma/wmv/rm/asf',
	preview : '预览',
	remote : '远程',
	tableError : '表格长度和宽度均要为正整数',
	widthError : '插件宽度必须为正整数'
};


/*********************************************************************************************************************
 * 2 预设函数
 * 2.1 AEE.appandChild(child) AEE.designBody插入结点(子结点)
 * 2.2 AEE.showUploadWin(img,menuName) 显示上传窗口(图标按钮,图标名称)
 * 2.3 AEE.getLeft(id) 获得对象的绝对横坐标(结点)
 * 2.4 AEE.getTop() 获得对象的绝对纵坐标
 * 2.5 AEE.getPath() 获得脚本相对地址
 * 2.6 AEE.showColorTable(img,menuName) 显示彩色图表(图标按钮,图标名称)
 * 2.7 AEE.showPopupDiv(img,html) 显示弹出菜单(按钮图标,内部html)
*********************************************************************************************************************/
/*********************************************************************************************************************
 * 2.1 AEE.appandChild(child) AEE.designBody插入结点(子结点)
*********************************************************************************************************************/
AEE.appandChild = function(child){
	if(AEE.range){
		AEE.range.collapse(true);//光标移至开头
		AEE.range.select();//仍然将这部分选中
		AEE.range.pasteHTML(child.outerHTML);
	}else{
		AEE.designBody.appendChild(child);
	}
	AEE.popupDiv.style.display = 'none';
}
AEE.upflag = -1;
/*********************************************************************************************************************
 * 2.2 AEE.showUploadWin(img,menuName) 显示上传窗口(图标按钮,图标名称)
*********************************************************************************************************************/
AEE.showUploadWin = function(img,menuName){
	AEE.upflag += 1;
	//AEE.uploadPHP = AEE.getPath() + 'upload.jsp';
	AEE.uploadPHP = '/py';
	var html = '';
	// 1 初始化框架
  html = '';
  if(AEE.viewer=="ie"){
      html = '';
	    html += '<iframe id=AEE_uploadFrame '
		     + '  frameborder=0'
	         + ' style="width=100%;height:100%;border:0;"'
		     + ' ></iframe>';
	    AEE.uploadDiv.innerHTML = html;
	    AEE.uploadDoc = AEE_uploadFrame.document;	 
  } else if(AEE.viewer=="firefox"){
      html += '<iframe id=AEE_uploadFrame'+AEE.upflag+' '
         + '  frameborder=0'
           + ' style="width=100%;height:100%;border:0;"'
         + ' ></iframe>';
      AEE.uploadDiv.innerHTML = html;
      AEE.uploadDoc = document.getElementById("AEE_uploadFrame"+AEE.upflag).contentWindow.document;
  }
	// 2 显示上传菜单
	//var left = AEE.getLeft(AEE.packDiv) + AEE.getLeft(img)+30;
	//var top = AEE.getTop(AEE.packDiv) + AEE.getTop(img)+30;
	var left = AEE.packDiv.offsetLeft + AEE.getLeft(img);
	var top = AEE.packDiv.offsetTop + AEE.getTop(img)+30;
	AEE.uploadDiv.style.left = left;
	AEE.uploadDiv.style.top = top;
	AEE.popupDiv.style.display = 'none';
	AEE.uploadDiv.style.display = 'block';

	
	/*********************************************************************************************************************
	*<二 />部署构件
	*********************************************************************************************************************/
	html = '';
	html += '<body'
	     + ' style="background:'+ AEE.bgColor +';overflow:hidden;"'
		 + ' >';
	//预览
	html += '<div id=AEE_uploadPreview'
	     + ' style="height:200px;border:1px solid '+ AEE.borderColor +';"'
		 + ' align=center'
		 + ' ></div>';
	html +='<form id=AEE_uploadForm action='+ AEE.uploadPHP +' target=_self method=post enctype="multipart/form-data">'
	//选择
	html+='<table align=center><tr><td>'
		 +'<select id="AEE_uploadPlace" onchange="javascript:AEE.uploadPlace();">'
		 +'<option value=Local>'+ AEE.language.local +'</option>'
		 +'<option value=Remote selected>'+ AEE.language.remote +'</option>'
		 +'</select>'
		 +'</td><td>'
		 +'<input type=text name=AEE_uploadPath value='+ AEE.uploadPath2 +' style="display:none;" />'
		 +'<input type=text id=AEE_uploadFinally name=AEE_uploadFinally style="display:none;" />'
		 +'<input type=text id=AEE_uploadLink size=15 style="display:block;" />'
		 +'<input type=file id=AEE_uploadFile name=AEE_uploadFile size=5 style="display:none;" />'
		 +'</td></tr></table>';
	//提交
	html+='<table width=100% align=center><tr><td align=center>'
	     +'<input style=cursor:pointer; type=button value='+ AEE.language.preview +' onclick="javascript:AEE.preview(\''+menuName+'\');" >'
		 +'&nbsp;'
	     +'<input style=cursor:pointer; type=button value='+ AEE.language.confirm +' onclick="javascript:AEE.upload(\''+menuName+'\');" >'
		 +'&nbsp;'
		 +'<input style=cursor:pointer; type=button value='+ AEE.language.cancel +' onclick="javascript:AEE.uploadDiv.style.display=\'none\';" >'
		 +'</td></tr></table>';
	html+='</form>';
	html += '</body>';
	//<三 />写入框架
	AEE.uploadDoc.open();
	AEE.uploadDoc.write(html);
	AEE.uploadDoc.close();
	AEE.uploadDoc.AEE = AEE;
}
/*********************************************************************************************************************
 * 2.3 AEE.getLeft(id) 获得对象的绝对横坐标(结点)
*********************************************************************************************************************/
AEE.getLeft = function(id){//获得对象横坐标
  if(id.tagName!='BODY'){
	return (id.offsetLeft+this.getLeft(id.offsetParent))
  }else{
	return 0;
  }
}
/*********************************************************************************************************************
 * 2.4 AEE.getTop() 获得对象的绝对纵坐标
*********************************************************************************************************************/
AEE.getTop = function(id){//获得对象纵坐标，找到BODY结点为止
  if(id.tagName!='BODY'){
	return (id.offsetTop+AEE.getTop(id.offsetParent))
  }else{
	return 0;
  }
}
/*********************************************************************************************************************
 * 2.5 AEE.getPath() 获得脚本相对地址
*********************************************************************************************************************/
AEE.getPath = function(){
	var path = '';
	var elements = document.getElementsByTagName('script');
	for (var i = 0, len = elements.length; i < len; i++) {
		if (elements[i].src && elements[i].src.match(/\/AEE[\w\-\.]*\.js/)) {
			path += elements[i].src.substring(0, elements[i].src.lastIndexOf('/') + 1);
		}
	}
        path = path.replace('/./','/');
	return path;
}
/*********************************************************************************************************************
 * 2.6 AEE.showColorTable(img,menuName) 显示彩色图表(图标按钮,图标名称)
*********************************************************************************************************************/
AEE.showColorTable = function(img,menuName){
	var html = '';
	html += '<table width=100% align=center><tr> '
	for (i = 0; i < AEE.colors.length; i++) {
		if (i >= 10 && i%10 == 0) {
			html += '</tr><tr>';
		}
		html += '<td'
		+ ' style="border:0px solid '+AEE.borderColor+';cursor:pointer;width:10%;height:20px;background:'+this.colors[i]+'; " '
		+ ' onmouseover="javascript:this.style.borderWidth=2;" '
		+ ' onmouseout="javascript:this.style.borderWidth=0;"'
	    + ' onclick="javascript:AEE.'+menuName+'(\'' + AEE.colors[i] + '\');" '
		+ ' >&nbsp;</td>';
	}
	html += '</tr></table>';
	AEE.showPopupDiv(img,html);
}
/*********************************************************************************************************************
 * 2.7 AEE.showPopupDiv(img,html) 显示弹出菜单(按钮图标,内部html)
*********************************************************************************************************************/
AEE.showPopupDiv = function(img,html){
	//var left = AEE.getLeft(AEE.packDiv) + AEE.getLeft(img)+30;
	//var top = AEE.getTop(AEE.packDiv) + AEE.getTop(img)+30;
	var left = AEE.packDiv.offsetLeft + AEE.getLeft(img);
	var top = AEE.packDiv.offsetTop + AEE.getTop(img)+30;
	AEE.popupDiv.style.left = left;
	AEE.popupDiv.style.top = top;
	AEE.popupDiv.innerHTML = html;
	AEE.uploadDiv.style.display = 'none';
	AEE.popupDiv.style.display = 'block';
}
/*********************************************************************************************************************
 * 3 动态函数
 * 3.1 AEE.show 脚本入口
 * 3.2 AEE.updateSelection() 更新焦点
 * 3.3 AEE.updateContentTextarea() 更新文本域内容
*********************************************************************************************************************/
/*********************************************************************************************************************
 * 3.1 AEE.show(id,width,height,uploadPath,bgColor,menuColor,borderColor,selectColor)显示插件
*********************************************************************************************************************/
AEE.show = function(id,width,height,uploadPath1,uploadPath2,bgColor,menuColor,borderColor,selectColor){
	//接收参数
	if(!id){ alert(AEE.language.idError);return;} //若容器的id为空，则出显示出错信息并返回
	if(!(AEE.contentTextarea=document.getElementById(id))){alert(AEE.language.idError);return;} //记录容器
	value = AEE.contentTextarea.value + '';
	if(width){ AEE.width = width; }
	if((AEE.height=parseInt(height))<1){alert(AEE.language.heightError);return;}
	if(uploadPath1){ AEE.uploadPath1 = uploadPath1; }else{ AEE.uploadPath1 = AEE.getPath() + 'upload/'; }
	if(uploadPath2){ AEE.uploadPath2 = uploadPath2; }else{ AEE.uploadPath2 = AEE.getPath() + 'upload/'; }
	if(bgColor){ AEE.bgColor = bgColor; }else{ AEE.bgColor = '#FFF'; }
	if(menuColor){ AEE.menuColor = menuColor; }else{ AEE.menuColor = '#EFEEE1'; }
	if(borderColor){ AEE.borderColor = borderColor; }else{ AEE.borderColor = '#ACA899'; }
	if(selectColor){ AEE.selectColor = selectColor; }else{ AEE.selectColor = '#316AC5'; }

	//创建插件包装AEE_packFrame 包装对背景不做设置
	var html = '';
	html = '<div id=AEE_packDiv><iframe id=AEE_packFrame'
	+ ' style="width:'+AEE.width+';height:'+AEE.height+';border:1px solid '+AEE.borderColor+';"'
	+ ' frameborder=0 scrolling=no marginwidth=0 marginheight=0'
	+ ' ></iframe></div>'
	+ ' <div id=AEE_popupDiv'
	+ ' style="width:300;height:300;border:1px solid '+AEE.borderColor+';background:'+AEE.bgColor+';'
	+ ' display:none;position:absolute;"'
	+ ' >弹出菜单</div>'
	+ ' <div id=AEE_uploadDiv'
	+ ' style="width:300;height:300;border:1px solid '+AEE.borderColor+';background:'+AEE.bgColor+';'
	+ ' display:none;position:absolute;"'
	+ ' >上传菜单</div>'	;
	document.open();
	document.write(html);
	document.close();
	AEE.packDiv = AEE_packDiv;
	AEE.packFrame = AEE_packFrame;
	AEE.packDoc = AEE.packFrame.document;
	if(AEE.viewer=="firefox"){ //以下代码只适合火狐
	    AEE.packDoc = AEE.packFrame.contentWindow.document;
	    //使iframe可编辑，因为我们使用Div来编辑，以下代码不用
	    //AEE.packDoc.designMode = 'on';
	    //AEE.packDoc.contentEditable = 'true';
	}
	AEE.popupDiv = AEE_popupDiv;
	AEE.uploadDiv = AEE_uploadDiv;
	//填充填充AEE_packFrame
	html = ''
	+ ' <div id=menuDiv'
	+ ' style="height:100;background:'+AEE.menuColor+';overflow=hidden;"'
	+ ' >';//工具菜单 不对边框设置
	for(i=0;i<AEE.icons.length;i++){
		html += '<img id=AEE_' + AEE.icons[i][0]
		+ ' style="cursor:pointer;border:1px solid '+AEE.menuColor+';"'
		+ ' src='+AEE.getPath()+'icon/'+AEE.icons[i][0]+'.gif title='+AEE.icons[i][1]
		+ ' onmouseover="this.style.borderColor=\''+AEE.borderColor+'\';"'
		+ ' onmouseout="this.style.borderColor=\''+AEE.menuColor+'\';"'
		+ ' onclick="'+AEE.icons[i][2]+'"'
		+ ' />';
	}

	html +=  '</div>'
	+ ' <div id=designDiv>'
	+ ' <iframe id=designFrame'
	+ ' style="width:100%;height:'+(AEE.height-120)+';border:0px;'
	+ ' frameborder=0 marginwidth=0 marginheight=0"'
	+ ' ></iframe>'
	+ ' </div>'
	+ ' <textarea id=codeTextarea'
	+ ' style="padding:5px;margin:0px;width:100%;height:'+(AEE.height-120)+';'
	+ ' display:none;border:0px;background:'+AEE.bgColor+';"'
	+ ' onmouseup="AEE.updateSelection();AEE.updateContentTextarea();"'
	+ ' onkeyup="AEE.updateSelection();AEE.updateContentTextarea();"'
	+ ' onkeypress="AEE.updateContentTextarea();"'
	+ ' onmouseover="AEE.updateContentTextarea();"'
	+ ' >'+value+'</textarea>'
	+ ' <div id=statusDiv'
	+ ' style="height:20;background:'+AEE.menuColor+';border:1px solid '+AEE.borderColor+';"'
	+ ' >状态栏</div>'
	+ ' ';
  
	AEE.packDoc.open();
	AEE.packDoc.write(html);
	AEE.packDoc.close();
	AEE.packDoc.AEE = AEE;
	//以下3行代码只适合IE
	AEE.designDiv = AEE.packFrame.designDiv;
	AEE.codeTextarea = AEE.packFrame.codeTextarea;
	AEE.statusDiv = AEE.packFrame.statusDiv;
	if(AEE.viewer=="firefox"){ /*以下代码是可兼容IE的*/
	    AEE.designDiv = AEE.packDoc.getElementById('designDiv');
	    AEE.codeTextarea = AEE.packDoc.getElementById('codeTextarea');
	    AEE.statusDiv = AEE.packDoc.getElementById('statusDiv');
	}
	//填充所见即所得框架	
	AEE.designFrame = AEE.packFrame.designFrame;
	if(AEE.viewer=="firefox"){ //兼容火狐	
	    AEE.designFrame = AEE.packDoc.getElementById('designFrame');
	}
	AEE.designDoc = AEE.designFrame.document;	
	if(AEE.viewer=="firefox"){ //兼容火狐	    
	    AEE.designDoc = AEE.designFrame.contentWindow.document;
	}
	html = '<body id=designBody'
	+ ' style="padding:5px;margin:0px;background:'+AEE.bgColor+';"'
	+ ' contenteditable=true'
	+ ' onmouseup="AEE.updateSelection();AEE.updateContentTextarea();"'
	+ ' onkeyup="AEE.updateSelection();AEE.updateContentTextarea();"'
	+ ' onkeypress="AEE.updateContentTextarea();"'
	+ ' onmouseover="AEE.updateContentTextarea();"'
	+ ' >'+value+'</body>';
	
	AEE.designDoc.open();
	
	AEE.designDoc.write(html);
	AEE.designDoc.close();
	AEE.designDoc.AEE = AEE;
	AEE.designBody = AEE.designFrame.designBody;
	if(AEE.viewer=='firefox'){
	    AEE.designBody = AEE.designDoc.getElementById('designBody');
	}
	AEE.mode = 'design';
	
}
/*********************************************************************************************************************
 * 3.2 AEE.updateSelection() 更新焦点
*********************************************************************************************************************/
AEE.updateSelection = function(){
  if(AEE.viewer=="ie"){
      AEE.selection = AEE.designDoc.selection;
      AEE.range = AEE.selection.createRange();
      AEE.rangeText = AEE.range.text;
  }
	
	if(AEE.viewer=="firefox"){
	    AEE.rangeText = AEE.designDoc.getSelection()	    
	}
	AEE.popupDiv.style.display = 'none';
	AEE.uploadDiv.style.display = 'none';
}
/*********************************************************************************************************************
 * 3.3 AEE.updateContentTextarea() 更新文本域内容
*********************************************************************************************************************/
AEE.updateContentTextarea = function(){
  var value = '';
  if(AEE.mode == 'design'){
	    value = AEE.designBody.innerHTML;
	    AEE.contentTextarea.value = value;
	    AEE.codeTextarea.value = value;
  }else if(AEE.mode == 'source'){
	    value = AEE.codeTextarea.value;
	    AEE.contentTextarea.value = value;
	    AEE.designBody.innerHTML = value;
  }
}


/*********************************************************************************************************************
 * 4 工具函数
 * 4.1 AEE.changeMode(img)
 * 4.2 打印
 * 4.3 预览
 * 4.4 剪切
 * 4.5 复制
 * 4.6 粘贴
 * 4.7 撤消
 * 4.8 重做
 * 4.9 全选
 * 4.7 AEE.insertLink(img) 插入超级链接(按钮图标)
 * 4.8 取消超链接
 * 4.9 AEE.insertTable(img) 插入表格(按钮图标)
 * 4.10 AEE.insertDate(img) 插入日期和时间(按钮图标)
 * 4.11 AEE.insertTitle(img) 插入大纲标题(按钮图标)
 * 4.12 AEE.showFontTable(img,menuName) 显示字体表格(图标按钮,图标名称,显示数组,样式)
 * 4.13 AEE.insertSize(img) 插入文字大小(按钮图标)
 * 4.16 AEE.color(color) 设置文本颜色(颜色)
 * 4.17 AEE.background(color) 设置背景颜色(颜色)
 * 4.30 AEE.insertHr(img) 插入彩色分割线(按钮图标)
*********************************************************************************************************************/
/*********************************************************************************************************************
 * 4.1 AEE.changeMode(img) 改变编辑方式 所见即所得编辑 <<====>>代码编辑(按钮图标)
*********************************************************************************************************************/
AEE.changeMode = function(img){
	if(img.src.indexOf('source')!=-1){
		img.src = AEE.getPath() + 'icon/design.gif';
		AEE.designDiv.style.display = 'none';
		AEE.codeTextarea.style.display = 'block';
		AEE.mode = 'source'; // 更改编辑模式
		//隐藏其它图标
		for (i = 1; i < this.icons.length; i++) {
			var el = AEE.packDoc.getElementById('AEE_'+this.icons[i][0]);
			el.style.visibility = 'hidden';
		}
	}else if(img.src.indexOf('design')!=-1){
		img.src = AEE.getPath() + 'icon/source.gif';
		AEE.designDiv.style.display = 'block';
		AEE.codeTextarea.style.display = 'none';
		AEE.mode = 'design'; // 更改编辑模式
		//显示其它图标
		for (i = 1; i < this.icons.length; i++) {
			var el = AEE.packDoc.getElementById('AEE_'+this.icons[i][0]);
			el.style.visibility = 'visible';
		}
	}
}
/*********************************************************************************************************************
 * 4.7 AEE.insertLink(img) 插入超级链接(按钮图标)
*********************************************************************************************************************/
AEE.insertLink = function(img){
	var html = '';
	html+='<table width=100% align=center><tr><td align=center>'
    +this.language.linkValue+'<input type=text id=AEE_linkValue size=24 /><br />'
    +this.language.linkHref+'<input type=text id=AEE_linkHref size=24 value=http:// /><br />'
    +this.language.linkTarget+'<select id=AEE_linkTarget><option value=_blank selected>'+this.language.linkBlank
    +'</option><option value=_self>'+this.language.linkSelf+'</option></select>'
    +'<input type=button value='+this.language.confirm+' onclick="javascript:AEE[\'setLink\']()" />&nbsp;'
    +'<input type=button value='+this.language.cancel+' onclick="javascript:AEE.popupDiv.style.display=\'none\';" />'
    +'</td></tr></table>';
	AEE.showPopupDiv(img,html);

	this.setLink = function(){//插入链接
	    var linkValue = document.getElementById('AEE_linkValue').value;
		var linkHref = document.getElementById('AEE_linkHref').value;
	    if(linkValue=='' || linkHref==''){
			this.statusDiv.innerHTML = this.language.linkError;
			return false;
		}
		var element = AEE.designDoc.createElement('a');
		element.href = linkHref;
		element.innerHTML = linkValue;
		element.target = document.getElementById('AEE_linkTarget').value;
		AEE.appandChild(element);
		this.popupDiv.style.display = 'none';
		this.statusDiv.innerHTML = '';
	    return true;

	}
}
/*********************************************************************************************************************
 * 4.9 AEE.insertTable(img) 插入表格(按钮图标)
*********************************************************************************************************************/
AEE.insertTable = function(img){
	var html = '';
	html += '<table width=100% align=center><tr><td align=center valign=middle>'
	+ ' 共<input type=text id=AEE_tableWidth size=14 />行<br \>'
	+ ' 共<input type=text id=AEE_tableHeight size=14 />列<br \>'
	+ ' <input type=button value='+ AEE.language.confirm +''
	+ ' onclick="javascricpt:AEE[\'setTable\'](AEE_tableWidth.value,AEE_tableHeight.value)" />&nbsp'
	+ ' <input type=button value='+ AEE.language.cancel +''
	+ ' onclick="javascript:AEE.popupDiv.style.display=\'none\';AEE.statusDiv.innerHTML=\'\';" />'
	+ ' </td></tr></table>';
	AEE.showPopupDiv(img,html);
	//定义插入表格方法
	AEE.setTable = function(width,height){
		if(width<=0 || height<=0 || isNaN(width) || isNaN(height)){
			AEE.statusDiv.innerHTML = AEE.language.tableError;
			return;
		}
		var element = AEE.designDoc.createElement("table");
		element.cellPadding = 0;
		element.cellSpacing = 0;
		element.border = 1;
		element.style.width = 200;
		element.style.height = 150;
		for (var i = 0; i < height; i++) {
			var rowElement = element.insertRow(i);
			for (var j = 0; j < width; j++) {
				var cellElement = rowElement.insertCell(j);
				cellElement.innerHTML = "&nbsp;";
			}
		}
		if(AEE.range){
			AEE.range.collapse(true);
			AEE.range.select();
			AEE.range.pasteHTML(element.outerHTML);
		}else{
			AEE.designBody.appendChild(element);
		}
		AEE.popupDiv.style.display = 'none';
		AEE.statusDiv.innerHTML = '';
		return true;
	}
}
/*********************************************************************************************************************
 * 4.10 AEE.insertDate(img) 插入日期和时间(按钮图标)
*********************************************************************************************************************/
AEE.insertDate = function(img){
	var html = '';
	var nows = AEE.getNows();
	for(var i = 0; i<nows.length; i++){
		html += '<div'
		+ ' style="cursor:pointer;background:'+AEE.bgColor+';"'
		+ ' onmouseover="this.style.background=\''+AEE.selectColor+'\';"'
		+ ' onmouseout="this.style.background=\''+AEE.bgColor+'\';"'
		+ ' onclick="var element=AEE.designDoc.createElement(\'span\');'
		+ ' element.innerHTML = \''+nows[i]+'\'; AEE.appandChild(element)"'
		+ '>&nbsp;&nbsp;'+ nows[i]+ '</div>';
	}
	AEE.showPopupDiv(img,html);
}
/*********************************************************************************************************************
 * 4.11 AEE.insertTitle(img) 插入大纲标题(按钮图标)
*********************************************************************************************************************/
AEE.insertTitle = function(img){
	AEE.titles = ['标题 1','标题 2','标题 3','标题 4','标题 5','标题 6'];
	var html = '';
	for(var i = 0; i<AEE.titles.length; i++){
		html += '<div'
		     + ' style="cursor:pointer;background:'+AEE.bgColor+';"'
			 + ' onclick="javascript:AEE.setTitle(\'H' + (i+1) + '\');" '
			 + ' onmouseover="javascript:this.style.background=\''+AEE.selectColor+'\';" '
			 + ' onmouseout="javascript:this.style.background=\''+AEE.bgColor+'\';"'
			 + ' ><H' + (i+1) + ' style="margin:2px;">' + AEE.titles[i] + '</H' + (i+1) + '></div>';
	}
	AEE.showPopupDiv(img,html);
  //定义设置函数
	AEE.setTitle = function(str){//设置标题
		if(AEE.rangeText){
			str = '<'+str+'>'
			if(AEE.viewer=="ie"){
			    AEE.range.execCommand('FormatBlock',false,str);
			} else if(AEE.viewer=="firefox"){
			    AEE.designDoc.execCommand('FormatBlock', false, str);
			}
		}else{
			var element = AEE.designDoc.createElement(str);
			element.innerHTML = str;
			AEE.designBody.appendChild(element);
		}
		AEE.popupDiv.style.display = 'none';
	}
}
/*********************************************************************************************************************
 * 4.12 AEE.showFontTable(img,menuName) 显示字体表格(图标按钮,图标名称,显示数组,样式)
*********************************************************************************************************************/
AEE.showFontTable = function(img,menuName,array,style,cmd){
	var html='';
	for (var i = 0; i < array.length; i++) {
		html += '<div'
		+ ' style="'+style+';background:'+ AEE.bgColor +';cursor:pointer;"'
		+ ' onclick="javascript:AEE.'+menuName+'(\''+ cmd +'\',\''+ array[i] +'\');" '
		+ ' onmouseover="javascript:this.style.background=\''+ AEE.selectColor +'\';" '
		+ ' onmouseout="javascript:this.style.background=\''+ AEE.bgColor +'\';"'
	    + ' >' + array[i] +'</div>';
	}
	AEE.showPopupDiv(img,html);
}
/*********************************************************************************************************************
 * 4.12.1 AEE.fontFamily(cmd,str) 设置字体(命令,字体名称)
*********************************************************************************************************************/
AEE.fontFamily = function(cmd,str){
	var element = this.designDoc.createElement('span');
	element.style.fontFamily = str;
	element.innerHTML = str;
	if(this.rangeText){
	  if(AEE.viewer=='ie'){
	      AEE.range.execCommand(cmd,false,str);
	  } else if(AEE.viewer=="firefox"){
	      //AEE.designDoc.execCommand('FormatBlock', false, str);
	      AEE.designDoc.execCommand(cmd,false,str);
	  }		
	}else{
		this.designBody.appendChild(element);
	}
	this.popupDiv.style.display = 'none';
}
/*********************************************************************************************************************
 * 4.13 AEE.insertSize(img) 插入文字大小(按钮图标)
*********************************************************************************************************************/
AEE.insertSize = function(img){
	AEE.fontSizes = ['10pt','12pt','14pt','18pt','24pt','36pt','72pt'];
	var html = '';
	for (i = 0; i < AEE.fontSizes.length; i++) {
		html += '<div'
		+ ' style="line-height:'+this.fontSizes[i]+';font-size:'+this.fontSizes[i]+';'
	    + ' background:'+AEE.bgColor+';cursor:pointer;"'
		+ 'onmouseover="javascript:this.style.background=\''+AEE.selectColor+'\';" '
		+ 'onmouseout="javascript:this.style.background=\''+AEE.bgColor+'\';"'
		+ 'onclick="javascript:AEE.setSize(\''+AEE.fontSizes[i]+'\');" '
		+ ' >' + AEE.fontSizes[i]+'</div>';
	}
	AEE.showPopupDiv(img,html);

	AEE.setSize = function(str){//设置字体
		var element = AEE.designDoc.createElement('span');
		element.style.fontSize = str;
		element.style.lineHeight = str;
		element.innerHTML = str;
	  if(AEE.rangeText){
			str = (str.substr(0,str.indexOf('p')))/2-3;
			if(AEE.viewer=='ie'){
			    AEE.range.execCommand('fontsize',false,str);
			} else if(AEE.viewer=='firefox'){
			    AEE.designDoc.execCommand('fontsize',false,str);
			}
			
		}else{
			AEE.designBody.appendChild(element);
		}
		AEE.popupDiv.style.display = 'none';
	}
}
/*********************************************************************************************************************
 * 4.16 AEE.color(color) 设置文本颜色(颜色)
*********************************************************************************************************************/
AEE.color = function(color){
	if(AEE.rangeText){
	    if(AEE.viewer=="ie"){
	        AEE.range.execCommand('forecolor',false,color);
	    } else if(AEE.viewer=="firefox"){
	        AEE.designDoc.execCommand('forecolor',false,color);
	    }
		
	}else{
		var element = this.designDoc.createElement('span');
		element.style.color = color;
		element.innerHTML = color;
		AEE.designBody.appendChild(element);
	}
	AEE.popupDiv.style.display = 'none';
}
/*********************************************************************************************************************
 * 4.17 AEE.background(color) 设置背景颜色(颜色)
*********************************************************************************************************************/
AEE.background = function(color){
	if(AEE.rangeText){
	    if(AEE.viewer=='ie'){
	        AEE.range.execCommand('backcolor',false,color);
	    } else if(AEE.viewer=='firefox'){
	        AEE.designDoc.execCommand('backcolor',false,color);
	    }
		
	}else{
		var element = AEE.designDoc.createElement('span');
		element.style.background = color;
		element.innerHTML = color;
		AEE.designBody.appendChild(element);
	}
	AEE.popupDiv.style.display = 'none';
}
/*********************************************************************************************************************
 * 4.30 AEE.insertHr(img) 插入彩色分割线(按钮图标)
*********************************************************************************************************************/
AEE.insertHr = function(img){
	var html = '<table width=100% align=center><tr>';
	for (var i = 0; i < AEE.colors.length; i++) {
		if (i >= 10 && i%10 == 0) {
			html += '</tr><tr>';
		}
		html += '<td'
		+ ' style="border:0px solid '+AEE.borderColor+';cursor:pointer;width:10%;height:20px;background:'+AEE.colors[i]+'; " '
		+ ' onmouseover="javascript:this.style.borderWidth=2;" '
		+ ' onmouseout="javascript:this.style.borderWidth=0;"'
		+ ' onclick="javascript:AEE.setHr(\'' + AEE.colors[i] + '\');" '
		+ ' ></td>';
	}
	html += '</tr></table>';
	AEE.showPopupDiv(img,html);

	AEE.setHr = function(str){//设置字体
		var element = AEE.designDoc.createElement('hr');
		element.style.color = str;
		AEE.appandChild(element);
		AEE.popupDiv.style.display = 'none';
	}
}

/*********************************************************************************************************************
 * AEE.getNows() 获得当前的日期和时间
*********************************************************************************************************************/
AEE.getNows = function(){
	var date = new Date();
	var year = date.getFullYear().toString();
	var month = date.getMonth().toString();
	var day = date.getDate().toString();
	var hour = date.getHours().toString();
	if(hour.length<2) hour = '0' + hour;
	var minute = date.getMinutes().toString();
	if(minute.length<2) minute = '0' + minute;
	var second = date.getSeconds().toString();
	if(second.length<2) second = '0' + second;
	var nows = [
	year+'-'+month+'-'+day,year+'年'+month+'月'+day+'日',year+'/'+month+'/'+day,year+'.'+month+'.'+day,
	hour+'时'+minute+'分'+second+'秒',hour+'时'+minute+'分',hour+':'+minute+':'+second,hour+':'+minute
	];
	return nows;
}




/*********************************************************************************************************************
 * AEE.insertMood(img) 插入表情图标(按钮图标)
*********************************************************************************************************************/
AEE.insertMood = function(img){
	AEE.moods = new Array();
	for(var i = 1; i <= 28; i++){
		var moodName = AEE.getPath() + 'mood/';
		if(i < 10){ moodName += '0'; }
		moodName += i + '.gif';
		AEE.moods[i - 1] = moodName;
	}
	var html='';
	html += '<table width=100% align=center><tr> '
	for (i = 0; i < AEE.moods.length; i++) {
		if (i >= 10 && i%10 == 0) {
			html += '</tr><tr>';
		}
		html += '<td>'
		+ '<img'
		+ ' style="border:0px solid '+ AEE.borderColor +';cursor:pointer;"'
		+ ' onmouseover="javascript:this.style.borderWidth=2;" '
		+ ' onmouseout="javascript:this.style.borderWidth=0;"'
		+ ' onclick="javascript:AEE.setMood(\'' + AEE.moods[i] + '\');" '
		+ ' src='+ AEE.moods[i] +' />'
		+ ' </td>';
	}
	html += '</tr></table>';
	AEE.showPopupDiv(img,html);

	AEE.setMood = function(src){//设置心情
		var element = this.designDoc.createElement("img");
		element.src = src;
		element.style.width = '20px';
		element.style.height = '20px';
		if(AEE.range){
			AEE.range.collapse(true);
			AEE.range.select();
			AEE.range.pasteHTML(element.outerHTML);
		}else{
			AEE.designBody.appendChild(element);
		}
		AEE.popupDiv.style.display = 'none';
	}
}

/*********************************************************************************************************************
 * AEE.insertSign(img) 插入特殊符号(按钮图标)
*********************************************************************************************************************/
AEE.insertSign = function(img){
	var html = '';
	html += '<table width=100% align=center><tr>';
	for (i = 0; i < this.signs.length; i++) {
		if (i >= 10 && i%10 == 0) {
			html += '</tr><tr>';
		}
		html += '<td align=center valign=center style="border:0px solid '+ AEE.borderColor +';cursor:pointer;" ' +
		'onclick="javascript:AEE.setSign(\''+ AEE.signs[i] +'\');" ' +
		'onmouseover="javascript:this.style.borderWidth=1;" ' +
		'onmouseout="javascript:this.style.borderWidth=0;">' + AEE.signs[i] + '</td>';
	}
	html += '</tra></table>';
	AEE.showPopupDiv(img,html);

	this.setSign=function(str){
		var element = this.designDoc.createElement("span");
		element.appendChild(this.designDoc.createTextNode(str));
		if(AEE.range){
			AEE.range.collapse(true);
			AEE.range.select();
			AEE.range.pasteHTML(element.outerHTML);
		}else{
			AEE.designBody.appendChild(element);
		}
		AEE.popupDiv.style.display = 'none';
	}
}


/*********************************************************************************************************************
 * AEE.layer(color) 插入彩色层(颜色)
*********************************************************************************************************************/
AEE.layer = function(color){
	var element = AEE.designDoc.createElement('div');
	element.style.background = color;
	element.style.width = 120;
	element.style.height = 75;
	AEE.appandChild(element);
}


/*********************************************************************************************************************
 * AEE.name 程序名称
*********************************************************************************************************************/
AEE.name = 'An Easy Editor';//名称

/*********************************************************************************************************************
 * AEE.preview(menuName) 预览窗体、图片、Flash、视频(菜单名称)
*********************************************************************************************************************/
AEE.preview = function(menuName){
	if(menuName == 'preview'){//预览窗体
		var newWin = window.open('', 'AEE_Preview','width=800,height=600,left=0,top=0,resizable=yes,scrollbars=yes');
		newWin.document.open();
		newWin.document.write(AEE.contentTextarea.value);
		newWin.document.close();
		return;
	}else{
		//设置本地文件
		if (AEE.uploadDoc.getElementById('AEE_uploadPlace').value == 'Local') {
		    var src = 'file:///' + AEE.uploadDoc.getElementById('AEE_uploadFile').value;
		}else{
			var src = AEE.uploadDoc.getElementById('AEE_uploadLink').value;
		}
		//检测文件后缀名
		var iPoint = src.lastIndexOf('.');
		if(iPoint>=0){//获得图片后缀名
			fileType = src.substr(iPoint);
			fileType.toLowerCase();
		}else{
			AEE.statusDiv.innerHTML = AEE.language[menuName + 'Error'];
			return;
		}
		//检查文件类型
		var succeed = false;
		for(var i = 0; i < AEE[menuName + 'Types'].length; i++){
			if(fileType == AEE[menuName + 'Types'][i]){
				succeed = true; break;
		    }
		}
		if(!succeed){
			AEE.statusDiv.innerHTML = AEE.language[menuName + 'Error'];
			return;
		}
		if(menuName == 'image'){
			var element = AEE.uploadDoc.createElement("img");
		}else if(menuName == 'flash'){
			var element = AEE.uploadDoc.createElement("embed");
			element.quality = "high";
			element.type = "application/x-shockwave-flash";
		}else if(menuName = 'media'){
			var element = AEE.uploadDoc.createElement("embed");
			element.loop = 'true';
			element.autostart = 'true';
		}
		element.src=src;
		element.style.width = '240px';
		element.style.height = '150px';
		var el = AEE.uploadDoc.getElementById('AEE_uploadPreview');
		if (el.hasChildNodes()) {
			el.removeChild(el.childNodes[0]);
		}
		el.appendChild(element);
		return true;
	}
}



/*********************************************************************************************************************
 * AEE_showCodeTextarea() 弹出所见即所得窗体designBody内容
*********************************************************************************************************************/
function AEE_showCodeTextarea(){ alert(AEE.codeTextarea.value); }

/*********************************************************************************************************************
 * AEE_showContentTextarea() 弹出文本域contentTextarea内容
*********************************************************************************************************************/
function AEE_showContentTextarea(){ alert(AEE_contentTextarea.value); }

/*********************************************************************************************************************
 * AEE.upload(menuName) 上传附件(菜单名称)
*********************************************************************************************************************/
AEE.upload = function(menuName){
	//设置本地文件
	var place = AEE.uploadDoc.getElementById('AEE_uploadPlace').value;
	if ( place == 'Local') {
		var src = 'file:///' + AEE.uploadDoc.getElementById('AEE_uploadFile').value;
	}else{
		var src = AEE.uploadDoc.getElementById('AEE_uploadLink').value;
	}
	//检测文件后缀名
	var iPoint = src.lastIndexOf('.');
	if(iPoint>=0){//获得图片后缀名
		fileType = src.substr(iPoint);
		fileType.toLowerCase();
	}else{
		AEE.statusDiv.innerHTML = AEE.language[menuName + 'Error'];
		return;
	}
	fileName = src.substr(0,iPoint);
	// 去掉文件名中的斜杠和反斜杠
	idxStart = fileName.lastIndexOf("/");
	if(idxStart!=-1){
	    fileName = fileName.substr(idxStart+1);
	}
	idxStart = fileName.lastIndexOf("\\");
	if(idxStart!=-1){
	    fileName = fileName.substr(idxStart+1);
	}
	//检查文件类型
	var succeed = false;
	for(var i = 0; i < AEE[menuName + 'Types'].length; i++){
		if(fileType == AEE[menuName + 'Types'][i]){
			succeed = true; break;
		}
	}
	if(!succeed){
		AEE.statusDiv.innerHTML = AEE.language[menuName + 'Error'];
		return;
	}

	//如果是本地文件，上传到服务器
	if (place=='Local') {
	  //定义二级目录
	  subDir = "";
	  if(menuName == "image"){
	    subDir = "image/";
	  } else {
	    subDir = "video/";
	  }
	  //检测服务端文件是否已经存在
	  isExists = true;
	  fileIdx = -1;
	  filePath = "";
	  while(isExists){ //循环设置文件
	      fileIdx++;
	      filePath = AEE.uploadPath1 + "" + subDir + fileName;
	      if(fileIdx>0){
	          filePath += "("+fileIdx+")";
	      }
	      filePath += fileType;
	      var xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	      xmlhttp.open("GET",filePath,false);
	      xmlhttp.send();
	      //alert(filePath+":"+xmlhttp.readyState+":"+xmlhttp.status+":"+isExists);
	      if(xmlhttp.readyState==4){
	          if(xmlhttp.status==200){
	              isExists = true;
	          } else if(xmlhttp.status==404) {
	              isExists = false;//文件不存在
	          }
	      } else {
	          //发生了其它情况，比如xmlhttp创建不成功等
	      }
	      if(fileIdx==5)break;
	  }	  
		src = filePath;
		//向服务器P传递参数
		AEE.uploadDoc.getElementById('AEE_uploadForm').action = ""
		+ AEE.uploadPHP 
	  + "?AEE_uploadFinally=" 
		+ AEE.uploadPath2
		+ "/" + subDir + fileName;
		AEE.uploadDoc.getElementById('AEE_uploadForm').submit();
	}
	if(menuName == 'image'){
		var element = AEE.designDoc.createElement("img");
	}else if(menuName == 'flash'){
		var element = AEE.designDoc.createElement("embed");
		element.quality = "high";
		element.type = "application/x-shockwave-flash";
	}else if(menuName = 'media'){
		var element = AEE.designDoc.createElement("embed");
		element.loop = 'true';
		element.autostart = 'true';
	}
	element.src = src;
	element.style.border = '1px solid '+AEE.borderColor;
	element.style.width = "100%";
	//element.style.height = 150;
	//element.style.align = "middle";
	//element.style.marginLeft = "50%";
	//element.style.align = "middle";

	//加一层外包装
	var imgDiv = AEE.designDoc.createElement("div");
	imgDiv.id = (new Date()).getTime().toString(10);
	imgDiv.style.width = "80%";
	imgDiv.style.overflow = "hidden";
	imgDiv.style.textAlign = "left";
	imgDiv.style.marginLeft = "10%";
	//添加元素
	if (menuName == "image") {
    //如果是图片
    imgDiv.innerHTML = "<img src=\"" + src + "\" style=\"width:100%;overflow:hidden;border:1px solid " + AEE.borderColor + ";\" />";
  } else {
    imgDiv.innerHTML = "<EMBED "
    + " style=\"width:100%;overflow:hidden;border:1px solid " + AEE.borderColor + ";\""
    + " src=\"" + src + "\""
    + " type=text/html;charset=iso-8859-1"
    + " loop=true"
    + " autostart=true"
    + " />";
  }
	imgDiv = AEE.appandChild(imgDiv);
	imgDiv.appandChild(element);
	//AEE.appandChild(element);
	AEE.popupDiv.style.display = 'none';
	AEE.statusDiv.innerHTML = '';
	return true;
}

/*********************************************************************************************************************
 * AEE.uploadPlace() 更改附件位置
*********************************************************************************************************************/
AEE.uploadPlace = function(){
	var value = AEE.uploadDoc.getElementById('AEE_uploadPlace').value;
	if(value=='Local'){
		AEE.uploadDoc.getElementById('AEE_uploadFile').style.display = 'block';
		AEE.uploadDoc.getElementById('AEE_uploadLink').style.display = 'none';
	}else{
		AEE.uploadDoc.getElementById('AEE_uploadFile').style.display = 'none';
		AEE.uploadDoc.getElementById('AEE_uploadLink').style.display = 'block';
	}
}

/*********************************************************************************************************************
 * AEE.version 程序版本
*********************************************************************************************************************/
AEE.version = '3.1.0.0';//版本：结构升级 功能改善 群众建议（奇数：测试+公众 偶数：稳定+商业）


