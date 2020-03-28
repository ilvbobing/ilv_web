/***************************************************************************************************
* Name:FormAct
* Todo:submit the form
* Datetime:2014-04-25 11:34:00
* Author:Lingbrother
* QQ:137284422
* Email:137284422@qq.com
***************************************************************************************************/
/***************************************************************************************************
 * Define class
***************************************************************************************************/
FormAct = {};
/***************************************************************************************************
* Standard parameters
***************************************************************************************************/
FormAct.br = "<br>\r\n";
/***********************************************************************
* II Prepared method
***********************************************************************/
/***********************************************************************
* III Main interface
***********************************************************************/

/*******************************************************************
* 3 act
*******************************************************************/
FormAct.submit = function(form){
    if(!form) form=document.getElementById("form_act");
    succeed = true;
    msg = "";
    // account
    var accountRe = /^[\w\d_]+$/;
    var account = document.getElementById("input_account");
    
    if(account){
        if(account.value.search(accountRe)==-1){            
            
            msg += "用户帐号不能为空，由字母、数字、下划线组成。"+FormAct.br;
            
            succeed = false;
        } else {
            title = document.getElementById("input_title");
            if(title){
                title.value = account.value;
            }
        }
    }
    //alert("static/core/FormAct.js:测试是否被调用4，account.value="+account.value);
    // password
    var passwordRe = /^[\w\d_-]*$/;
    var password = document.getElementById("input_password");
    if(password && password.value.search(passwordRe)==-1){
        msg += "用户密码由字母、数字、下划线组成。"+FormAct.br;
        succeed = false;
    }
    var password2 = document.getElementById("input_password2");
    if(password2 && password && password2.value != password.value){
        msg += "两次输入密码不一致。"+FormAct.br;
        succeed = false;
    }
    // title must have one noblank character
    var titleRe = /^.*\S.*$/;
    var title = document.getElementById("input_title");
    if(title && title.value.search(titleRe)==-1){
        msg += "标题不能为空。"+this.br;
        succeed = false;
    }
    
    // name must construct by character num and uderstack.
    var nameRe = /^[\w\d\._]+$/;
    var name = document.getElementById("input_name");
    if(name && name.value.search(nameRe)==-1){
        msg += "名称不能为空，由字母、数字、下划线组成。"+this.br;
        succeed = false;
    }
    
    // summary must short in 280 characters or 140 zhs.
    var summary = document.getElementById("textarea_summary");
    if(summary){
        ascre = /^[\x00-\xff]$/
        var chre = /^[\u4e00-\u9fa5]$/; //chinese regex
        var fullre = /^[^\x00-\xff]$/; //hull regex
        var ascre = /^[\x00-\xff]$/; //half regex
        var summaryValue = summary.value;
        var strLen = summaryValue.length;
        var summaryLen = 0;
        for(var i=0; i<strLen; i++){
            sc =summaryValue.charAt(i);
            if(sc.match(ascre)){
                summaryLen++; //half character
            } else {
                summaryLen += 2; //full character
            }
        }
        
        if(summaryLen>280){
            msg += "文章摘要不能超过140个汉字（或280个字母、数字等，含标点）。"+this.br;
            succeed = false;
        }
    }
    
    // display message
    if (!succeed) {
    
      //if failed,show the error message
      document.getElementById('div_msg').innerHTML = msg;
      //document.getElementById('divAddMsg').focus();
      document.getElementById('div_msg').style.display = 'block';
      alert(msg);
    } else {
      //if succeed submit the form
      //form.method = "post";
      //form.enctype = "multipart/form-data";
      form.submit(); 
    }    
}

