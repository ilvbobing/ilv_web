/***********************************************************************
 * 名称:jsAddForm 表单提交实例
 * 功能:提交表单
 * 时间:2011年10月26日13时20分
 * 作者:ilvbobing
 * 邮箱 :314244633@qq.com
***********************************************************************/
/***********************************************************************
 * 定义实例
***********************************************************************/
jsFormAdd = {}
/***********************************************************************
 * jsAddForm.submit 提交表单方法
***********************************************************************/
jsFormAdd.submit = function(form){
  alert("static/cell/default/acs.js:form="+form);
  if(form == null){
	  form = document.getElementById("formAdd");
  }
  // 正则表达式
  var idre = /^[0-9]{2}$/;
  var dtnmre = /^[A-Za-z_]{1}\w*$/;
  var authorre = /[\S]{1}/; //至少有一个非空字符
  var nmre = /^[A-Za-z_]{1}\w*$/;
  var pswre = /[\S]{1}/;
  var ttre = /[\S]{1}/;
  var msg="";
  var succeed=true;

  var title=document.getElementById('divAddTitle');
  if(title && title.value.search(ttre) == -1){
    msg += "文章标题不能为空，至少含有一个非空白字符。<br>";
    succeed = false;
  }
  
  var summaryNode=document.getElementById("divAddSummary");
  
  var summaryLen = 0;
  var chre = /^[\u4e00-\u9fa5]$/; //中文正则表达式
  var fullre = /^[^\x00-\xff]$/; //所有全角字符
  var ascre = /^[\x00-\xff]$/; //所有半角字符
  if(summaryNode){
      //计算字符串长度  
      var summary = summaryNode.value;    
      var strLen = summary.length;
      for(var i=0; i<strLen; i++){
          sc = summary.charAt(i);
          if(sc.match(ascre)){
              summaryLen++; //半角字符
          } else {
              summaryLen += 2; //全角字符
          }
      }
      if(summary.search(ttre)==-1){
          msg += "文章摘要不能为空，至少含有一个非空白字符。<br>\r\n"
          succeed = false;
      }
      if(summaryLen>280){
          msg += "文章摘要不能超过140个汉字（或280个字母、数字等，含标点）。<br>\r\n"
          succeed = false;
      }
  }

  //检测id号
  var id=document.getElementById("id");
  if(id && id.value.search(idre) == -1){
    msg += "序号不能为空，为01~99之间的整数，注意01前的0不能省略。<br>\r\n";
    succeed = false;
  }

  var author = document.getElementById("author");
  if (author && author.value.search(authorre) == -1) {
    msg += "文章作者不能为空，至少含有一个非空白字符。<br>\r\n";
    succeed = false;
  }
  
  //检测数据表名
  var dtnm=document.getElementById('dtnm');
  if(dtnm && dtnm.value.search(dtnmre) == -1){
    msg += "数据表不能为空，由字母、下划线和数字组成，首字符为字母或下划线。<br>\r\n";
    succeed = false;
  }
  //检测栏目名
  var nm=document.getElementById('nm');
  if(nm && nm.value.search(nmre) == -1){
    msg += "栏目名不能为空，由字母、下划线和数字组成，首字符为字母或下划线。<br>\r\n";
    succeed = false;
  }

  var psw=document.getElementById('psw');
  if(psw && psw.value.search(pswre) == -1){
    msg += "密码不能为空。<br>\r\n";
    succeed = false;
  }
  
  var psw2=document.getElementById('psw2');
  if(psw && psw2 && psw.value != psw2.value){
    msg += "两次输入密码不一致。<br>\r\n";
    succeed = false;
  }

  // 显示信息
  if (!succeed) {
    //如果检测失败，显示错误信息
	  document.getElementById('divAddMsg').innerHTML = msg;
	  //document.getElementById('divAddMsg').focus();
	  document.getElementById('divAddMsg').style.display = 'block';
	  alert(msg);
  } else {
    //如果检测无误，提交投稿表单
    form.submit(); 
  }
} //提交表单方法结束

/*********************************************************************************************************************
 * jsAddForm.submit 提交添加回复表单方法
*********************************************************************************************************************/
jsFormAdd.submitAddCmt = function(form) {
  if(form == null){
    form = document.getElementById("fromAddCmt");
  }
  //定义参数
  if (form.areaAddCmtCnt) {
    //如果找到了内容
    var cntValue = form.areaAddCmtCnt.value;
    if (cntValue == null || cntValue.length == 0) {
      //如果值为空或值长度为0
      divAddCmtMsg.innerHTML = "信息：回复内容不能为空!!!";
      return false;
    } else {
      //回复内容合法，提交表单
      form.submit();
      //divAddCmtMsg.innerHTML = "信息：提交成功!!!内容为：" + cntValue;
    }
  } else {
    //如果没有找到内容结点
    divAddCmtMsg.innerHTML = "信息：没有定义回复内容的结点";
    return false;
  }
}
