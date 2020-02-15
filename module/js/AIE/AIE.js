/*********************************************************************************************************************
* 
* <p>类的名称: AIE</p>
* 
* <p>插件名称: 图片插件</p>
* 
* <p>插件描述: Ailvbobing's image enterprise</p>
*
* <p>主要功能: 图片上、下、左、右循环滚动，渐隐渐显，随鼠标滚动改变大小/p>
*
* <p>创建时间: 2011年04月14日20时35分</p>
*
* <p>Copyright: Copyright (c) 2011</p>
*
* <p>Company: 个人</p>
*
* @author 爱履薄冰
* @version 1.0.0
*********************************************************************************************************************/
/*********************************************************************************************************************
* 定义类及必要的参数,及必要的参数
*********************************************************************************************************************/
AIE = {}
/*********************************************************************************************************************
 * 循环移动
 ********************************************************************************************************************/
// 循环上移
AIE_tp = function (div,div1,div2) {
  var tp = {};
  tp.speed = 20;//每20ms偏移一次
  tp.div = div;
  tp.div1 = div1;
  tp.div2 = div2;
  //如果设定div2,则赋值
  if (!div2.isFull) {
    tp.div2.innerHTML = tp.div1.innerHTML;
  }  
  div2.innerHtml = div1.innerHTML;
  tp.scrollTop = function() {
	//div1的高度<div的上偏移量，div1已经完全移出了边框
	if(tp.div.scrollTop > tp.div1.offsetHeight) {
	  tp.div.scrollTop -= tp.div1.offsetHeight;
	}else{
	  tp.div.scrollTop++;//每次移动一个元素。
	}
  }
  tp.interval = setInterval(tp.scrollTop,tp.speed);
  tp.div.onmouseover = function() { clearInterval(tp.interval); }
  tp.div.onmouseout = function() { tp.interval = setInterval(tp.scrollTop,tp.speed); }
}
// 循环下移
AIE_dwn = function (div,div1,div2) {
  var dwn = {};
  dwn.speed = 50;//每50ms偏移一次
  dwn.div = div;
  dwn.div1 = div1;
  dwn.div2 = div2;
  dwn.div2.innerHTML = dwn.div1.innerHTML;
  div2.innerHtml = div1.innerHTML;
  dwn.scrollTop = function() {
	//div1的高度<div的上偏移量，div1已经完全移出了边框
	if(dwn.div.scrollTop == 0) {
	  dwn.div.scrollTop += dwn.div1.offsetHeight;
	}else{
	  dwn.div.scrollTop--;//每次移动一个元素。
	}
  }
  dwn.interval = setInterval(dwn.scrollTop,dwn.speed);
  dwn.div.onmouseover = function() { clearInterval(dwn.interval); }
  dwn.div.onmouseout = function() { dwn.interval = setInterval(dwn.scrollTop,dwn.speed); }
}
// 循环左移
AIE_lft = function (div,div1,div2) {
  var lft = {};
  lft.speed = 20;//每20ms偏移一次
  lft.div = div;
  lft.div1 = div1;
  lft.div2 = div2;
  //不自动赋值
  if (!div2.isFull) {
    lft.div2.innerHTML = lft.div1.innerHTML;
  }
  
  div2.innerHtml = div1.innerHTML;
  lft.scrollLeft = function() {
	//div1的高度<div的上偏移量，div1已经完全移出了边框
	if(lft.div.scrollLeft > lft.div1.offsetWidth) {
	  lft.div.scrollLeft -= lft.div1.offsetWidth;
	}else{
	  lft.div.scrollLeft++;//每次移动一个元素。
	}
  }
  lft.interval = setInterval(lft.scrollLeft,lft.speed);
  lft.div.onmouseover = function() { clearInterval(lft.interval); }
  lft.div.onmouseout = function() { lft.interval = setInterval(lft.scrollLeft,lft.speed); }
}
// 循环右移
AIE_rht = function (div,div1,div2) {
  var rht = {};
  rht.speed = 50;//每50ms偏移一次
  rht.div = div;
  rht.div1 = div1;
  rht.div2 = div2;
	//视情设置第二循环体
	if (!div2.isFull) {
	  rht.div2.innerHTML = rht.div1.innerHTML;
	}
  
  div2.innerHtml = div1.innerHTML;
  rht.scrollLeft = function() {
	//div1的高度<div的上偏移量，div1已经完全移出了边框
	if(rht.div.scrollLeft == 0) {
	  rht.div.scrollLeft += rht.div1.offsetWidth;
	}else{
	  rht.div.scrollLeft--;//每次移动一个元素。
	}
	var stt = document.getElementById('status');
	if(stt != null) {
	  stt.innerHTML = rht.div.scrollLeft + ' ' + rht.div1.offsetWidth + ' ' + rht.div2.offsetWidth;
	}
  }
  rht.interval = setInterval(rht.scrollLeft,rht.speed);
  rht.div.onmouseover = function() { clearInterval(rht.interval); }
  rht.div.onmouseout = function() { rht.interval = setInterval(rht.scrollLeft,rht.speed); }
}

/*********************************************************************************************************************
 * 两幅图片渐显
 ********************************************************************************************************************/
AIE_shw2 = function(imgdividnm,imgurls,imgtts,imgwidth,imgheight) {
  var imgdiv = document.getElementById(imgdividnm);
  imgdiv.i_strngth=1;
  imgdiv.i_image=0;
  imgdiv.imgtts = imgtts;
  imgdiv.imageurl = imgurls;
  imgdiv.imgwidth = imgwidth;
  imgdiv.imgheight = imgheight;
  showimage(imgdividnm);
}
function showimage(imgdividnm) {
  var imgdiv = document.getElementById(imgdividnm);
  if(document.all) {
	if (imgdiv.i_strngth <=110) {
	  imgdiv.innerHTML="<img width="+imgdiv.imgwidth+" height="+imgdiv.imgheight
	  +" style='filter:alpha(opacity="+imgdiv.i_strngth+")' src="+imgdiv.imageurl[imgdiv.i_image]+" border=0>"
	  +imgdiv.imgtts[imgdiv.i_image];
	  imgdiv.i_strngth=imgdiv.i_strngth+10
	  var timer=setTimeout("showimage('"+imgdividnm+"')",100)
	}else {
	  clearTimeout(timer)
	  var timer=setTimeout("hideimage('"+imgdividnm+"')",1000)
	}
  }
  if(document.layers) {
	clearTimeout(timer)
	document.imgdiv.document.write("<img width="+imgdiv.imgwidth+" height="+imgdiv.imgheight
								   +" src="+imgdiv.imageurl[imgdiv.i_image]+" border=0>" +imgdiv.imgtts[imgdiv.i_image])
	document.close()
	imgdiv.i_image++
	if (imgdiv.i_image >= imgdiv.imageurl.length) {imgdiv.i_image=0} 
	var timer=setTimeout("showimage('"+imgdividnm+"')",2000)
  } 
}
function hideimage(imgdividnm) { 
  var imgdiv = document.getElementById(imgdividnm);
  if (imgdiv.i_strngth >=-10) {
	imgdiv.innerHTML="<img width="+imgdiv.imgwidth+" height="+imgdiv.imgheight
	+" style='filter:alpha(opacity="+imgdiv.i_strngth+")' src="+imgdiv.imageurl[imgdiv.i_image]+" border=0>" +imgdiv.imgtts[imgdiv.i_image];
	imgdiv.i_strngth=imgdiv.i_strngth-10
	var timer=setTimeout("hideimage('"+imgdividnm+"')",100)
  }else {
	clearTimeout(timer)
	imgdiv.i_image++
	if (imgdiv.i_image >= imgdiv.imageurl.length) {imgdiv.i_image=0}
	imgdiv.i_strngth=1
	var timer=setTimeout("showimage('"+imgdividnm+"')",500) 
  }
}
/*********************************************************************************************************************
 * 两幅图片渐显 改进版 避免了每次都要等待加入
 ********************************************************************************************************************/
AIE_shw = function(imgdividnm,imgurls,imgtts) {
  var imgdiv = document.getElementById(imgdividnm);
  imgdiv.op=1;//初始化透明度
  imgdiv.i_image=0;
  imgdiv.imgtts = imgtts;//标题数组
  imgdiv.imageurl = imgurls;//地址数组
  imgdiv.innerHTML = "";
  for(var i=0; i < imgurls.length; i++) { //遍历所有图片
  imgdiv.innerHTML += ""//设置层内设置
  + "<div style=display:none;>"
	+ imgurls[i]
	+ imgdiv.imgtts[i]
  + "</div>";
  }
  shwimg(imgdividnm);
}
function shwimg(imgdividnm) {
  var imgdiv = document.getElementById(imgdividnm);//找出父层
  var tempimg = document.getElementById(imgdividnm+"_"+imgdiv.i_image);//找出当前要渐显的图片 
  if(imgdiv.op <= 100) {
	tempimg.style.display = "block";
	tempimg.parentNode.style.display = "block";
	tempimg.style.filter = "alpha(opacity="+imgdiv.op+")";
	imgdiv.op += 10;
	imgdiv.timer = setTimeout("shwimg('"+imgdividnm+"')",100);
  }else{
	clearTimeout(imgdiv.timer);
	imgdiv.timer = setTimeout("hidimg('"+imgdividnm+"')",1000);
  }
}
function hidimg(imgdividnm) { 
  var imgdiv = document.getElementById(imgdividnm);
  var tempimg = document.getElementById(imgdividnm+"_"+imgdiv.i_image);
  if(imgdiv.op >= 0) {
	tempimg.style.filter = "alpha(opacity="+imgdiv.op+")";
	imgdiv.op -=10;
	imgdiv.timer = setTimeout("hidimg('"+imgdividnm+"')",100);
  }else{
	clearTimeout(imgdiv.timer);
	tempimg.style.display = "none";
	tempimg.parentNode.style.display = "none";
	imgdiv.i_image ++;
	if (imgdiv.i_image >= imgdiv.imageurl.length) {imgdiv.i_image=0}
	imgdiv.op = 1;//初始化透明度
	imgdiv.timer = setTimeout("shwimg('"+imgdividnm+"')",100);
  }
}

/*********************************************************************************************************************
* 名称：startSah(idDiv,imgs,[hrefs,[tts]])
* 描述：start show and hide
* 参数：idImgDiv 渐显隐层id，图片集,链接集，tts 标题集
* 功能：实现图片的渐隐和渐显
*********************************************************************************************************************/
AIE.startSah = function (idDiv,imgs,hrefs,tts) { //图片逐渐隐显
  if (tts == null) { //如果未定义标题集，初始化标题集
    tts = new Array(imgs.length);
	for(var i = 0; i < tts.length; i++) { //循环置空数组
	  tts[i] = "";
	} //循环置空结束
  } //初始化标题集结束
  
  if (hrefs == null) { //如果未定义链接集，初始化链接集
    hrefs = new Array(imgs.length);
	for(var i = 0; i < hrefs.length; i++) { //循环置空数组
	  hrefs[i] = "";
	} //循环置空结束
  } //初始化链接集结束
  
  var div = document.getElementById(idDiv);
  div.op = 1;//初始化透明度
  div.i = 0; //初始化图片索引
  div.num = imgs.length; //图片的个数
  for(var i=0; i < imgs.length; i++) { //遍历所有图片
  div.innerHTML += ""//设置层内设置
  + "<a " + hrefs[i] + " target=_blank style=display:none;>" 
	+ imgs[i]
	+ tts[i]
  + "</a>"
  }
  var img = document.getElementById(idDiv + "_" + div.i); //显示第一张图片
  img.style.filter = "alpha(opacity=" + div.op + ")";
  img.parentNode.style.display = "block";
  div.sahFlag = "shw" //开始显示
  div.sahInterval = setInterval("AIE.sah(\"" + idDiv + "\")", 1); //启动渐显渐隐
}
/*********************************************************************************************************************
* 名称：sah(idDiv)
* 参数：idDiv 渐显层id
* 功能：渐显图片，当图片完全显示时再渐隐,完全渐隐时，隐藏当前图片，渐显下一张图片
*********************************************************************************************************************/
AIE.sah = function (idDiv) { //图片渐显隐
  var div = document.getElementById(idDiv);
  var img = document.getElementById(idDiv + "_" + div.i);
  //显示部分
  if (div.sahFlag == "shw") { //开始显示
    if (div.op <= 100) { //如果还没有完全显示
	  div.op += 1;
	  img.style.filter = "alpha(opacity=" + div.op + ")";
	} else { //完全显示了,开始渐隐
	  div.sahFlag = "hid";
	} //显示结束
  } else { //此时div.sahFlag = "hid" 开始渐隐
    if (div.op >= 5) { //如果还没有完全隐藏
	  div.op -= 1;
	  img.style.filter = "alpha(opacity=" + div.op + ")";
	} else { //已经完全隐藏
	  img.parentNode.style.display = "none"; //隐藏当前图片所在的层
	  div.i ++;
	  if (div.i >= div.num) div.i = 0; //如果超过了最大图片个数，回到第一张图片
	  //显示下一张图片
	  img = document.getElementById(idDiv + "_" + div.i);
	  img.style.filter = "alpha(opacity=" + div.op + ")";
	  img.parentNode.style.display = "block";
	  div.sahFlag = "shw";
	} //判断是否完全隐藏结束
  } //渐隐结束
}
/*********************************************************************************************************************
* 名称：wheelResize(img,[maxW = 800],[minW = 100])
* 参数：img 图片，maxW 最大宽度,是一个int类型,minW最小宽度可省
* 功能：随鼠标滚动改变图片大小
* 备注：zoom用于设置或检索对象的缩放比例，此属性不可继承，但它会影响子对象的大小。（类比：background和filter）
* 备注：parseInt(string,［radix］) 由string得到整数,radix：进制，若未设定，则前缀0x为16进制，0为8进制，其它为十进制
*********************************************************************************************************************/
AIE.wheelResize = function (img, maxW,minW) { //自动随鼠标改变图片大小
  if (maxW == null) maxW = 300; //默认最大缩放比例为800%,即图片放大8倍
  if (minW == null) minW = 10;  //默认最小缩放比例为10%，即图片缩至1/10
  var zoom = parseInt(img.style.zoom, 10)|| 100; //检索缩放比例不成功，图片保持在页面的原始大小（不是实际大小）。
  zoom += event.wheelDelta/12;
  if (zoom > minW && zoom < maxW) img.style.zoom = (zoom).toString() + "%"; //加上百分号(toString()可以省去)
  return false;
}

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
/*********************************************************************************************************************
* 名称：准备废弃的类
* 参数：idDiv 封装层的id，用来生成封装层实例objDiv,其它主要有如下可设置参数
* idx    图片索引 默认为-1，循环递加 如objDiv.idx = -1;
* srcs   图片位置数组 如objDiv.srcs = ["src=img/1.gif","src=img/2.gif","src=img/3.gif"];
* hrefs  图片的链接数组，如objDiv.hrefs = ["href=#1","href=#2","href=#2"]
* sizes  图片尺寸数组，共四个元素，大图片宽、高，小图片的宽、高。默认为objDiv.sizes = ["200","150","40","30"]
* effect 效果，默认为objDiv.effect = 23;
* timeOut 循环周期，默认为5000，单位为毫秒，如objDiv.timeOut = 5000
*********************************************************************************************************************/
var navigatorName = "Microsoft Internet Explorer";
var isIE = false; 
if(navigator.appName==navigatorName) isIE = true;
function objSP_Article() {this.ImgUrl=""; this.LinkUrl=""; this.Title="";}
function SlidePic_Article(_id) {this.ID=_id; this.Width=0;this.Height=0; this.TimeOut=5000; this.Effect=23; this.TitleLen=0; this.PicNum=-1; this.Img=null; this.Url=null; this.Title=null; this.AllPic=new Array(); this.Add=SlidePic_Article_Add; this.Show=SlidePic_Article_Show; this.LoopShow=SlidePic_Article_LoopShow;}
function SlidePic_Article_Add(_SP) {this.AllPic[this.AllPic.length] = _SP;}
function SlidePic_Article_Show() {
  if(this.AllPic[0] == null) return false;
  document.write("<div align='center'><a id='Url_" + this.ID + "' href='' target='_blank'><img id='Img_" + this.ID + "' style='width:" + this.Width + "px; height:" + this.Height + "px; filter: revealTrans(duration=2,transition=23);' src='javascript:null' border='0'></a>");
  if(this.TitleLen != 0) {document.write("<br><span id='Title_" + this.ID + "'></span></div>");}
  else{document.write("</div>");}
  this.Img = document.getElementById("Img_" + this.ID);
  this.Url = document.getElementById("Url_" + this.ID);
  this.Title = document.getElementById("Title_" + this.ID);
  this.LoopShow();
}
function SlidePic_Article_LoopShow() {
  if(this.PicNum<this.AllPic.length-1) this.PicNum++ ; 
  else this.PicNum=0; 
  if(isIE==true){
  this.Img.filters.revealTrans.Transition=this.Effect; 
  this.Img.filters.revealTrans.apply(); 
  }
  this.Img.src=this.AllPic[this.PicNum].ImgUrl.substr(4);
  if(isIE==true){
  this.Img.filters.revealTrans.play();
  }
  this.Url.href=this.AllPic[this.PicNum].LinkUrl.substr(5);
  if(this.Title) this.Title.innerHTML="<a href="+this.AllPic[this.PicNum].LinkUrl+" target='_blank'>"+this.AllPic[this.PicNum].Title+"</a>";
  this.Img.timer=setTimeout(this.ID+".LoopShow()",this.TimeOut);
}
