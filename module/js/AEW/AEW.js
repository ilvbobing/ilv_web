/*********************************************************************************************************************
* 
* <p>类的名称: AEW</p>
* 
* <p>插件名称: 窗口插件</p>
* 
* <p>插件描述: Ailvbobing's easy window</p>
*
* <p>主要功能: 显示弹出对话框、双击自动下翻</p>
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
AEW = {}
AEW.popAllHeight = 0; //弹出窗口的总高度
/*********************************************************************************************************************
* 名称：getPath
* 参数：无
* 功能：得到插件的相对地址
*********************************************************************************************************************/
AEW.getPath = function(){
	var path = '';
	var elements = document.getElementsByTagName('script');
	for (var i = 0, len = elements.length; i < len; i++) {
		if (elements[i].src && elements[i].src.match(/\/AEW[\w\-\.]*\.js/)) {
			path += elements[i].src.substring(0, elements[i].src.lastIndexOf('/') + 1);
		}
	}
  path = path.replace('/./','/');
	return path;
}
/*********************************************************************************************************************
* 名称：createPopWin
* 参数：宽，高，前景色，背景色，标题，窗口图片，打开位置，链接
* 比如：AEW.createPopWin("AEW_popWin",240,180,"ffffff","dd8432","网站公告","<img src=img/qxgb.jpg width=234 height=138 boder=0 />","_blank","AEM.htm");
* 功能：生成弹出窗口
*********************************************************************************************************************/
AEW.createPopWin = function (idPopWin,width,height,color,bcolor,tt,img,target,href) { //创建弹出窗口
  AEW.popAllHeight = height;
  AEW.idPopWin = idPopWin; //记录弹出窗口的id
  var htmPopWin = "";
  htmPopWin += ""
  + "<div id=" + idPopWin + " " //外框层开始
  + "style=\"" //样式开始
  + "width:" + width + "px;height:0px;overflow:hidden;" //尺寸
  + "Z-INDEX: 99999;position:absolute;left:0;bottom:0;" //位置
  + "border:1px solid #666;margin:0;padding:0px;display:none;" //边框、留白、显示
  + "color:" + color + ";font-size:16px;" //文字
  + "background: " + bcolor + ";" //背景颜色
  + "\"" //样式结束
  + ">" //窗口外框头
  
	//上方留白
	+ "<div style=\"width:" + (width - 2) + "px;height:4px;overflow:hidden;border-right:1px solid #fff;border-top:1px solid #fff;\">"
	+ "&nbsp;"
	+ "</div>" //上方留白 
	//标题
	+ "<div style=\"height:25px;voerflow:hidden;float:left;padding:5px 5px;\">"
	+ tt //标题正文
	+ "</div>" //标题结束
	//关闭按钮
	+ "<div style=\"height:25px;voerflow:hidden;border-right:1px solid #fff;float:right;padding:5px 5px;\">" //关闭按钮
	  + "<SPAN title=关闭 style=font-weight:bold;cursor:hand;margin-right:4px; onclick=AEW.dwnPopWin(\"" + idPopWin + "\") >"
	    + "<img src=" + AEW.getPath() + "img/close.gif width=16 />"
	  + "</SPAN>"
	+ "</div>"
	
	//图片
	+ "<div "
	+ "style=\"width:" + (width - 2) + "px;height:" + (height - 38) + ";overflow:hidden;"
	+ "padding:2px;border-right:1px solid #fff;background:#E0E0E0;\">"
	  + "<a href = " + href + " target=" + target + ">"
	    + img
	  + "</a>"
	+ "</div>"
  
  + "</div>" //外框层尾
  + "";
  document.open();
  document.write(htmPopWin);
  document.close();
} //创建弹出窗口方法AEM.createPopWin结束
/*********************************************************************************************************************
* 名称：upPopWin(div)
* 参数：需要升起的窗口
* 功能：将弹出窗从底部缓慢升起
*********************************************************************************************************************/
AEW.upPopWin = function (idPopWin) { //弹出窗口向上升起
  var popWin = document.getElementById(idPopWin);
  var popH = parseInt(popWin.style.height);
  popWin.style.height = (popH + 1).toString() + "px";
  popWin.style.height = (popH).toString() + "px";
  popWin.style.display = "block";
  popWin.style.height = (popH + 1).toString() + "px";
  popWin.style.height = (popH).toString() + "px";
  AEW.upInterval = setInterval("AEW.scrollPop(\"" + idPopWin + "\", \"up\")", 1);
  
} //窗口升起方法upPopWin结束
/*********************************************************************************************************************
* 名称：dwnPopWin(idPopWin)
* 参数：需要降下的窗口id
* 功能：将弹出窗缓慢落下
*********************************************************************************************************************/
AEW.dwnPopWin = function (idPopWin) { //弹出窗口向上升起
  AEW.dwnInterval = setInterval("AEW.scrollPop(\"" + idPopWin + "\", \"dwn\")", 1);
} //窗口降下方法dwnPopWin结束
/*********************************************************************************************************************
* 名称：dwnPopWin(idPopWin)
* 参数：idPopWin 弹出窗口的id str == "up" 上升，str == "dwn" 下降 
* 功能：实现上升和下降
*********************************************************************************************************************/
AEW.scrollPop = function (idPopWin, str){ //卷动弹出窗口
  var popWin = document.getElementById(idPopWin);
  var popH = parseInt(popWin.style.height);
  if (str == "up") { //如果是上升
    if (popH < AEW.popAllHeight){ //如果还没有升到最大高度
	  popWin.style.height = (popH + 2).toString() + "px";
    } else { //已经升到了最大高度
      clearInterval(AEW.upInterval);
      window.onscroll = AEW.popMove; //当页面滚动时，弹出窗口也跟随滚动，始终保持在底部
    }
  } else { //如果是下降
    if (popH > 4) { //如果还未降到底
      popWin.style.height = (popH - 2).toString() + "px";
    } else { //已经降到了最底端
      clearInterval(AEW.dwnInterval);
      popWin.style.display = "none";
    }
  } //下降结束
}
/*********************************************************************************************************************
* 名称：popMove
* 参数：无，但调入前，需要把弹出窗口id赋给AEW.idPopWin
* 功能：跟随页面滚动弹出窗口
*********************************************************************************************************************/
AEW.test = true;
AEW.popMove = function () { //跟随滚动弹出窗口
  var popWin = document.getElementById(AEW.idPopWin);
  var popH = parseInt(popWin.style.height);
  popWin.style.height = (popH + 1).toString() + "px"; //通过高度的改变来引起弹出窗口的重新选位
  popWin.style.height = (popH).toString() + "px";
} //跟随滚动弹出窗口方法popMove结束
/*********************************************************************************************************************
* 名称：startAutoScroll(str) //开始自动翻滚
* 参数：str == up 向上翻滚 str == dwn 向下翻滚
* 功能：开始自动翻滚，考虑到实用价值，只会用到向下翻滚
*********************************************************************************************************************/
AEW.startAutoScroll = function (str) { //开始翻滚
  if (str == "dwn") { //如果是下滚
	document.onmousedown = AEW.stpAutoDwnWin;
	document.ondblclick = AEW.autoDwnWin;
  } //下滚结束
}
/*********************************************************************************************************************
* 名称：autoDwnWin() //自动向下流动
* 参数：无
* 功能：实现页面鼠标双击时自动下滚
*********************************************************************************************************************/
AEW.autoDwnWin = function (){ //自动下滚
  AEW.autoDwnTimer = setInterval ("AEW.scrollWindow ()",30);
} //自动下滚方法autoDwnWin结束
/*********************************************************************************************************************
* 名称：stpAutoDwnWin() //停止向下滚动
* 参数：无
* 功能：停止页面自动下滚
*********************************************************************************************************************/
AEW.stpAutoDwnWin = function (){ //停止下滚
  clearInterval(AEW.autoDwnTimer);
} //停止下滚方法stpAutoDwnWin结束
/*********************************************************************************************************************
* 名称：scrollWindow() //滚动窗口
* 参数：无
* 功能：滚动窗口
*********************************************************************************************************************/
AEW.scrollWindow = function () { //滚动窗口
  var currentTop = document.body.scrollTop;
  window.scroll(0, ++currentTop);
  if (currentTop != document.body.scrollTop) { //如果窗口不再能够上卷，则停止
    clearInterval(AEW.autoDwnTimer);
  } //判断窗口是否下滚到底结束
} //滚动窗口方法scrollWindow结束


/*********************************************************************************************************************
* 名称：popDv() //弹出DV展播窗口
* 参数：div 被填充的层 title 标题 img 缩略图 swf 视频,title,imgSrc,swfSrc,href,top,left,width,height
* 功能：滚动窗口
*********************************************************************************************************************/
AEW.popDv = function (div) {
  if (!div){ alert("传入的div参数不是一个实例");return;} //若容器的id为空，则出显示出错信息并返回
  if (!div.dvTitle) {div.dvTitle = "未命名"; } //默认的标题为未命名
  if (!div.dvImg || div.dvImg.length < 4) { div.dvImg = "src=" + AEW.getPath() + "img/1.jpg"; } //默认的图片1.jpg
  if (!div.dvSwf || div.dvSwf.length < 4) { div.dvSwf = "src=" + AEW.getPath() + "img/1.swf"; } //默认视频为1.swf
  if (!div.dvHref || div.dvHref.length < 5) { div.dvHref = "href=" + AEW.getPath() + "?"; } //默认的链接为?
  if (!div.dvMore || div.dvMore.length < 5) { div.dvMore = "href=" + AEW.getPath() + "?"; } //默认的链接为?
  if (!div.dvHeight){ div.dvHeight = 300; } //默认窗口高度为300
  if (!div.dvSuf) { div.dvSuf = ""; } //默认后缀
  if (!div.dvMenuColor || div.dvMenuColor.length < 1 ) { div.dvMenuColor = "#DD8432"; } //默认的颜色为黄褐色
  if (!div.dvMenuTitle) { div.dvMenuTitle = "DV作品快递"; } //默认的颜色为黄褐色
  if (!div.dvCloseHidden) { div.dvCloseVisible = false; } //默认关闭按钮可见

  //获取div的尺寸
  var offsetWidth = div.offsetWidth;
  var offsetHeight = div.offsetHeight;
  //定义页面内容
  var html = "";
  //0、背景
  //图片
  html += "<div id=divDvImg" + div.dvSuf + " style=margin-top:0px;display:block;>"
  + "<img "
  + " style=width:100%;height:" + offsetHeight + ";overflow:hidden;"
  + " src=\"" + div.dvImg.substr(4) + "\""
  + " />"
  + "</div>"
  + "";
  //视频
  html += "<div id=divDvSwf" + div.dvSuf + " style=margin-top:30px;display:none;>"
  //+ "<EMBED id=embedDv" + div.dvSuf + " style=\"BORDER-RIGHT: #aca899 1px solid; BORDER-TOP:#aca899 1px solid;BORDER-LEFT: #aca899 1px solid;WIDTH:" + div.offsetWidth + ";BORDER-BOTTOM: #aca899 1px solid;HEIGHT:" + (div.offsetHeight-70) + ";cursor:hand;\" src=\"" + div.dvSwf.substr(4) + "\"  type=text/html;charset=iso-8859-1  loop=true  autostart=true"
  //+ " />"
  + ""
  + "</div>"
  + "";
  //1、菜单
  html += ""
  + "<div "
  + " style=BACKGROUND:" + div.dvMenuColor + ";FILTER:alpha(opacity=80);TEXT-ALIGN:right;"
  + "WIDTH:" + offsetWidth + ";top:0px;left:0px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:30px;z-index:1;"
  + "padding-top:5px;padding-right:10px;"
  + " ><!--菜单-->"
  + ( div.dvCloseHidden 
  ? ""
  : "<img onmouseup=" + div.id + "Body.dvWidthAct=\"hidden\";AEW.changeDvWidth(\"" + div.id + "Body\"); title=关闭 src=\"" + AEW.getPath() + "img/close.gif\" style=cursor:hand; />")
  + "</div>"
  + "";
  //标题
  html += ""
  + "<div "
  + " style=FILTER:alpha(opacity=100);TEXT-ALIGN:left;"
  + "WIDTH:" + offsetWidth + ";top:0px;left:0px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:30px;z-index:2;"
  + "padding-top:5px;padding-left:5px;"
  + " ><!--菜单-->"
  + "<strong><font color=#FFFFFF>" + div.dvMenuTitle + "&nbsp;&nbsp;</font></strong>"
  + "<a href=\"" + div.dvMore.substr(5) + "\" target=_blank>"
    + ""
  + "</a>"
  + "</div>"
  + "";
  //更多
  html += ""
  + "<div "
  + " style=TEXT-ALIGN:right;"
  + "WIDTH:" + offsetWidth + ";top:0px;right:10px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:30px;z-index:2;"
  + "padding-top:5px;padding-right:25px;"
  + " ><!--标题-->"
  + "<a href=\"" + div.dvMore.substr(5) + "\" target=_blank>"
   + "<font color=#FFFFFF>"
    + "<strong>更多>></strong>"
   + "</font>"
  + "</a>"
  + "</div>"
  + "";
  //2、黑色背景
  html += ""
  + "<div "
  + " style=BACKGROUND:#000;FILTER:alpha(opacity=60);TEXT-ALIGN:right;"
  + "WIDTH:" + offsetWidth + ";bottom:0px;left:0px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:40px;z-index:1;"
  + " ><!--黑底-->"
  + "&nbsp"
  + "</div>"
  + "";
  //3、标题
  html += ""
  + "<div "
  + " style=TEXT-ALIGN:left;"
  + "WIDTH:" + offsetWidth + ";bottom:0px;left:0px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:30px;z-index:2;"
  + " ><!--标题-->"
  + "<a href=\"" + div.dvHref.substr(5) + "\" target=_blank>"
   + "<font color=#FFFFFF><strong>"
    + div.dvTitle
   + "</strong></font>"
  + "</a>"
  + "</div>"
  + "";
  //4、开始箭头
  html += ""
  + "<div "
  + " style=TEXT-ALIGN:right;"
  + "WIDTH:" + offsetWidth + ";bottom:0px;left:0px;TEXT-INDENT:10px;LINE-HEIGHT:25px;POSITION:absolute;HEIGHT:40px;z-index:3;"
  + "padding-right:8px;"
  + " ><!--图片-->"
  + "<img id=imgDvAct" + div.dvSuf + " onmouseup=AEW.changeDvAct(this); title=播放 style=height:100%;overflow:hidden;cursor:hand; src=\"" + AEW.getPath() + "img/play.gif\" />"
  + "</div>"
  div.innerHTML = html;
  document.getElementById("imgDvAct" + div.dvSuf).div = div;
  setTimeout("AEW.changeDvWidth('" + div.id + "Body')",50);
}
/*********************************************************************************************************************
* 名称：changeDvWidth 变换展播窗口的高度，直到高度与设定的高度相等
* 参数：id div的id值
* 功能：逐渐弹出展播窗口
*********************************************************************************************************************/
AEW.changeDvWidth = function (id) {
  if (!id) { alert("在改变展播窗口高度时，传入的层id无效"); return;}
  var div = document.getElementById(id);
  if (!div.dvWidthAct) { 
    div.dvWidthAct = "show"; //默认显示窗口
  }
  if (div.dvWidthAct == "show") { 
    div.style.width = div.offsetWidth + 10;
    if (div.offsetWidth < div.dvWidth) {
      setTimeout("AEW.changeDvWidth('" + div.id + "')",50);
    }
  } else {
    //隐藏窗口
    div.style.width = div.offsetWidth - 10;
    if (div.offsetWidth > 0) {
      setTimeout("AEW.changeDvWidth('" + div.id + "')",50);
    } else {
      div.style.display = "none"; //不再显示窗口
    }
  }
}
/*********************************************************************************************************************
* 名称：changeDvAct 更换DV展播行为图片播放<-->停止() //滚动窗口
* 参数：div 被填充的层 title 标题 img 缩略图 swf 视频,title,imgSrc,swfSrc,href,top,left,width,height
* 功能：滚动窗口
*********************************************************************************************************************/
AEW.changeDvAct = function(img) {
  if (!img) { alert("传入的图片结点不是有效实例"); return;} //图片结点必须有效
  if (!img.swfHTML) { //暂存视频的代码
    //img.swfHTML =  document.getElementById("divDvSwf" + img.div.dvSuf).innerHTML;
	img.swfHTML = ""
    + " <EMBED id=embedDv" + img.div.dvSuf + ""
	+ " style=\"BORDER-RIGHT: #aca899 1px solid; BORDER-TOP:#aca899 1px solid;BORDER-LEFT: #aca899 1px solid;WIDTH:" + img.div.offsetWidth + ";BORDER-BOTTOM: #aca899 1px solid;HEIGHT:" + (img.div.offsetHeight-70) + ";cursor:hand;\""
	+ " src=\"" + img.div.dvSwf.substr(4) + "\"  type=text/html;charset=iso-8859-1  loop=true  autostart=true"
    + " />"
	+ ""
	+ "";
  }
  if (img.src.match(/[\w\-\.]*.play.gif/)) {
    //如果当前是播放，则理发为停止
    img.src = AEW.getPath() + "img/stop.gif";
    img.title = "停止";
    document.getElementById("divDvSwf" + img.div.dvSuf).innerHTML = img.swfHTML;
    document.getElementById("divDvImg" + img.div.dvSuf).style.display = "none";
    document.getElementById("divDvSwf" + img.div.dvSuf).style.display = "block";
  } else {
    img.src = AEW.getPath() + "img/play.gif";
    img.title = "播放";
    document.getElementById("divDvImg" + img.div.dvSuf).style.display = "block";
    document.getElementById("divDvSwf" + img.div.dvSuf).style.display = "none";
    document.getElementById("embedDv" + img.div.dvSuf).clearAttributes();
    document.getElementById("divDvSwf" + img.div.dvSuf).innerHTML = "";
  }
}