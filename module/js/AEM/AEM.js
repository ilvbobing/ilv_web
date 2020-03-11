/***************************************************************************************************
 * AEM an easy menu 菜单
***************************************************************************************************/
AEM = {};
//注：定义函数时，不能为函数在参数中赋初值
/***************************************************************************************************
 * 1 show 显示菜单
 * swfDirswf相对网页的位置,菜单集，链接集
***************************************************************************************************/
AEM.show = function(swfDir,menusZh,menusUrl){
    
    if(!swfDir) swfDir = "AEM.swf";
    if(!menusZh) menusZh = "新闻频道|电影频道|音乐频道|游戏频道|网络电视|网友论坛|会员专区|测试菜单";
    if(!menusUrl)menusUrl= "http://localhost/|#|#|#|#|#|#|#";
    menusUrl = encodeURIComponent(menusUrl)
    embedHtml = '<embed src='+swfDir+' wmode=opaque'
        + ' FlashVars="menusZh='+menusZh+'&menusUrl='+menusUrl+'"'
        + ' menu=false bgcolor=F0F0F0 quality=high width=900 height=40 allowScriptAccess=sameDomain'
        + ' style="border:0px solid red;width:900px;height:40px;"'
        + ' type=application/x-shockwave-flash'
        + ' pluginspage=http://www.macromedia.com/go/getflashplayer>'
        + '</embed>';
    document.open();
    document.write(embedHtml);
    document.close();
    //alert("AEM.js--test6");
}
