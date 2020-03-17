/*********************************************************************************************************************
* 名称：AIE.shine 升级后的图片渐显 只能使用一次@@
* 参数：idDiv 封装层的id，用来生成封装层实例objDiv,其它主要有如下可设置参数
* idx    图片索引 默认为-1，循环递加 如objDiv.idx = -1;
* srcs   图片位置数组 如objDiv.srcs = ["src=img/1.gif","src=img/2.gif","src=img/3.gif"];
* hrefs  图片的链接数组，如objDiv.hrefs = ["href=#1","href=#2","href=#2"]
* sizes  图片尺寸数组，共四个元素，大图片宽、高，小图片的宽、高。默认为objDiv.sizes = ["200","150","40","30"]
* effect 效果，默认为objDiv.effect = 23;
* timeOut 循环周期，默认为5000，单位为毫秒，如objDiv.timeOut = 5000
*********************************************************************************************************************/
AIE = {}
AIE.shine = function(idDiv) {
  if (idDiv == null) {
    alert("传入的参数不能为空。");
	return false;
  }
  var objDiv = document.getElementById(idDiv);
  if (objDiv == null) {
    alert("没有定义相应id的封装层。" + idDiv);
	return false;
  }
  /*********************************************************************************************************************
  * 初始化
  *********************************************************************************************************************/
  if (!objDiv.isLoop) {  //如果还没有开始循环	
	//定义默认的循环参数
	if (objDiv.idx == null) {
	  //默认开始索引为-1，自加后正好为0。
	  objDiv.idx = 0;
	}
    if (!objDiv.srcs){
	  alert("没有定义需要渐显的图片数组");
	  return false;
	}
  if (objDiv.srcs.length == 0) {
    //防止出现没有图片的情况!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return false;
  }
	if (objDiv.hrefs == null) {
	  objDiv.hrefs = new Array();
	  for (var i = 0; i < objDiv.srcs.length; i++) {
	    objDiv.hrefs[i] = "href=#" + i;
	  }
	}
	if (objDiv.sizes == null) {
	  //默认大图片宽、高，小图片宽、高
	  objDiv.sizes = ["600", "400", "60", "40"];
	}
	if (objDiv.effect == null) {
	  //默认效果值为23
	  objDiv.effect = 23;
	}
	//设置默认循环周期5000毫秒
	if (objDiv.timeOut == null) {
	  objDiv.timeOut = 3000;
	}
	//加入iFrame
	var html = "";
	html += ""
	+ "<iframe id=AIE_shineFrame"
	+ " style=\"width:" + objDiv.sizes[0] + ";height:" + objDiv.sizes[1] + ";border:1px solid #000;"
	+ "position:relative;left:0px;top:0px;\""
	+ " frameborder=5 scrolling=no marginwidth=0 marginheight=0"
	+ " ></iframe>"
	+ "";
	//objDiv.innerHTML = html;
	//objDiv.packFrame.style.width = objDiv.sizes[0];
	//objDiv.packFrame.style.height = objDiv.sizes[1];
	objDiv.packDoc = objDiv.packFrame.document;
	//显示所有图片
	htm = ""
	+ "<div id=frmDiv align=center><!--封装开始-->"
	  + "<a id=Url_" + objDiv.id + " target=_blank href=# >"
		+ "<img id=Img_" + objDiv.id
		+ " style=width:" + objDiv.sizes[0] + ";height:" + objDiv.sizes[1] + ";filter:revealTrans(duration=2,transition=23);"
		+ " src=javascript:null;"
		+ " border=0"
		+ " />"
	  + "</a>"
	//+ "</div>" //后面再封装
	+ "";
	htm += "</div>";
	//设置黑底
	if (objDiv.sizes.length >= 4 || objDiv.tts != null) {
	  //如果存在小图标或有标题，则要设置黑色背景背景
	  htm += ""
	  + "<div "
	  + " style=BACKGROUND:#000;FILTER:alpha(opacity=60);TEXT-ALIGN:right;opacity:0.3;"
	  + "WIDTH:" + objDiv.sizes[0] + ";bottom:0px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:" + objDiv.sizes[3]*2 + ";z-index:1;"
	  + " ><!--黑底-->"
	  + "&nbsp"
	  + "</div>"
	  + "";	
	}
	
	//设置小图标，利用绝对坐标
	var htmImgSmall = null;
	if (objDiv.sizes.length >= 4) {
	  //如果需要设置小图标
	  htmImgSmall = "";	  
	  for (var i = 0; i < objDiv.srcs.length; i++) {
		//循环加入图标
		htmImgSmall += ""
		+ "<div style=display:inline;foat:left;margin-left:8px;CURSOR:pointer;>"
		  + "<a href=" + objDiv.hrefs[i].substr(5) + " target=_blank>"
		    + "<img style=\"border:1px solid #666;width:" + objDiv.sizes[2] + ";height:" + objDiv.sizes[3] + ";\" alt=" + objDiv.tts[i] 
			+ " src=" + objDiv.srcs[i].substr(4) + ""
			+ " onmouseover="
			+ "frmDiv.idx=" + i + ";"
			+ "frmDiv.objDiv.chosedIdx=frmDiv.idx;"
			+ "frmDiv.objDiv.Img.filters.revealTrans.apply();"
			+ "frmDiv.objDiv.Img.src=frmDiv.objDiv.srcs[frmDiv.idx].substr(4);"
			+ "frmDiv.objDiv.Url.href=frmDiv.objDiv.hrefs[frmDiv.idx].substr(5);"
			+ "frmDiv.objDiv.Img.filters.revealTrans.play();"
			+ "this.style.borderColor='red';"
			
			+ " onmouseout=this.style.borderColor='#666';"
			+ " />"
		  + "</a>"
		+ "</div>"
		+ "";
	  } //循环加入图标结束
	}
	//添加小图标的封装
	if (htmImgSmall != null) {
	  htmImgSmall = ""
	  + "<div style=position:absolute;left:0px;bottom:20px;z-index:2;>"
		+ htmImgSmall
	  + "</div>"
	  + "";
	  htm += htmImgSmall;
	}
	//书写标题
	if (objDiv.tts != null) {
	  //如果存在标题
	  htm += ""
	  + "<div id=Title_" + objDiv.id + ""
	  + " style=font-weight:normal;font-size:16px;line-height:18px;FONT-FAMILY:微软雅黑,黑体;text-align:left;"
	  + "width:" + objDiv.sizes[0] + ";height:30px;overflow:hidden;"
	  + "position:absolute;left:0px;bottom:-10px;z-index:3;"
	  + "padding-left:10px;"
	  + " >"
	  + "</div>"
	  + "";
	}
	
	//写入网页代码
	objDiv.packDoc.open();
	objDiv.packDoc.write(htm);
	objDiv.packDoc.close();
	
	objDiv.Img = objDiv.packDoc.getElementById("Img_" + objDiv.id);
	objDiv.Url = objDiv.packDoc.getElementById("Url_" + objDiv.id);
	objDiv.Title = objDiv.packDoc.getElementById("Title_" + objDiv.id);
	objDiv.frmDiv = objDiv.packDoc.getElementById("frmDiv");
	objDiv.frmDiv.idx = objDiv.idx;
	objDiv.frmDiv.objDiv = objDiv;
	objDiv.isLoop = true; //开始循环体开始
  } //判断循环是否开始结束
  /*********************************************************************************************************************
  * 开始循环 默认循环周期为objDiv.timeOut = 5000 单位默认为毫秒
  *********************************************************************************************************************/
  if (objDiv.isLoop) { //设置循环体
	//如果用户选择了某个图标
	if (objDiv.chosedIdx != null) {
	  objDiv.idx = objDiv.chosedIdx; //防止图片自动变化
	  objDiv.chosedIdx = null; //复位选定标志
	}
	//判断浏览器
	if (objDiv.isIE == null) {
	  var navigatorName = "Microsoft Internet Explorer";
	  objDiv.isIE = false; 
	  if(navigator.appName==navigatorName){
		objDiv.isIE = true;
	  }  
	}
	
	if(objDiv.isIE==true){
	  //如果是IE浏览器，则显示效果
	  objDiv.Img.filters.revealTrans.Transition=objDiv.effect; 
	  objDiv.Img.filters.revealTrans.apply(); 
	}
	//这里有一个技巧，先设定标题、链接，再设定图片，紧接着就要启动效果，否则效果会跟不上。
	objDiv.Img.src = objDiv.srcs[objDiv.idx].substr(4);
	if(objDiv.isIE == true){
	  objDiv.Img.filters.revealTrans.play();
	}
	objDiv.Url.href = objDiv.hrefs[objDiv.idx].substr(5);
	if (objDiv.Title) {
	  //如果标题存在
	  objDiv.Title.innerHTML = "<a href=" + objDiv.hrefs[objDiv.idx].substr(5) + " target=_blank><font color=#FFFFFF>" + objDiv.tts[objDiv.idx] + "</font></a>";
	}
	if (objDiv.idx < objDiv.srcs.length -1) {
	  //如果索引号一直小于图片的数量，自动加1
	  objDiv.idx++;
	} else {
	  //如果idx = 图片的最大序号
	  objDiv.idx = 0;
	}
	//如果用户选择了某个图标
	if (objDiv.chosedIdx != null) {
	  objDiv.idx = objDiv.chosedIdx; //防止图片自动变化
	  objDiv.chosedIdx = null; //复位选定标志
	}
	objDiv.timer = setTimeout("AIE.shine('" + objDiv.id + "')", objDiv.timeOut);  
  } //循环体结束
  return true;
}