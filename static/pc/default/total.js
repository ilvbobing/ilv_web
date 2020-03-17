/***************************************************************************************************
* Ilv_Shine shine images
***************************************************************************************************/
Ilv_Shine = {}
/***************************************************************************************************
* Ilv_Shine.show shine images
***************************************************************************************************/
Ilv_Shine.show = function(swfDir,pyDir,srcs,hrefs,titles,width,height){

    if(!swfDir) swfDir = "news.swf";
    if(!pyDir) pyDir = "";
    if(!srcs) srcs= "1.jpg|2.jpg|3.jpg|4.jpg|5.jpg"
    if(!hrefs) hrefs = "/py|#|#|#|#";
    if(!titles) titles = "title1|titel2|tite3|title4|title5"
    if(!width) width = 486
    if(!height) height = 295
    var text_height=50
    var swf_height = height+text_height
    //get the srcs's vs dir of swf
    var picArray = srcs.split("|")
    srcs = pyDir+picArray[0]
    for(var i=0; i<5; i++){
        srcs += "|" + pyDir+picArray[i];
    }
    // alert(srcs);
    var html = '';
    html += ' <embed src="'+swfDir+'" wmode="opaque"';
    html += ' FlashVars="pics='+srcs;
    html += '&links='+hrefs;
    html += '&texts='+titles;
    html += '&borderwidth='+width;
    html += '&borderheight='+height;
    html += '&textheight='+text_height;
    html += '"';
    html += ' menu="false" bgcolor="#F0F0F0" quality="high"';
    html += ' width="'+ width +'"';
    html += ' height="'+ height +'"';
    html += ' allowScriptAccess="sameDomain"';
    html += ' type="application/x-shockwave-flash"';
    html += ' pluginspage="http://www.macromedia.com/go/getflashplayer" />';
    document.open();
    document.write(html);
    document.close();
}
