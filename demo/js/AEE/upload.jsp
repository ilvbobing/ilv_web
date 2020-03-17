<%@ page contentType="text/html; charset=GBK" %>
<%@ page import="java.io.BufferedOutputStream" %>
<%@ page import="java.io.File" %>
<%@ page import="java.io.FileOutputStream" %>
<%@ page import="java.io.IOException" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.Date" %>
<%@ page import="java.util.Hashtable" %>
<%@ page import="javax.servlet.ServletInputStream" %>
<%@ page import="javax.servlet.http.HttpServletRequest" %>
<%@ page import="javax.servlet.http.HttpServletResponse" %>
<%@ page import="java.text.SimpleDateFormat" %>
<script type=text/javascript>
<!--
//alert("AEE/upload.jsp");
//-->
</script>
<%! //添加声明
/*********************************************************************************************************************
 * <br>名称：getStrInput
 * <br>参数: 无
 * <br>创建时间：2011年04月12日23时39分
 * <br>创建目的：调试程序时，观察输入流的具体内容，强烈建议测试的上载文件使用文本文件，简洁明了。
 * <br>修改心得：request.getInputStream只能使用一次，否则会出现IOException。即它不能和process同时使用
 * <br>相关知识：getInputStream()与getReader()两者也不能同时使用，且它们都只能使用一次。
 * <br>功能：调试时，观察JSP中request的输入流具体内容。
*********************************************************************************************************************/
//所有输入信息
public String getStrInput(HttpServletRequest req, HttpServletResponse res){
String strInput = ""; //所有信息
String msg = "<br><strong>The msg is :</strong><br>"; //初始化信息
int BUFSIZE = 1024*8;
try { //引用输入流
  ServletInputStream sis = req.getInputStream();
  int rtnPos = 0;
  byte[] buffs = new byte[BUFSIZE * 8];
  while((rtnPos = sis.readLine(buffs, 0, buffs.length)) != -1){
    String strBuff = new String(buffs, 0, rtnPos);
    strInput += strBuff;
  }
} catch (IOException ex) {
  msg += ex.toString() + "<br>";
}
System.out.println(strInput + msg);
return strInput + msg;
}
//获得指定地址所包含的文件名，含有扩展名
private String getFileName(String input){
   int fIndex = input.lastIndexOf("\\");
   if (fIndex == -1) {
       fIndex = input.lastIndexOf("/");
       if (fIndex == -1) {
           return input;
       }
   }

   input = input.substring(fIndex + 1);
   return input;
}
//给文件加上时间戳，防止出现重复，时间戳(this.timeID)在构造函数中已经初始化
private String getFileNameByTime(String input){
 //初始化时间戳
 Date dt = new Date();
 SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddHHmmssSSS");
 int index = input.indexOf(".");
 return input.substring(0,index) + sdf.format(dt) + input.substring(index);
}
//获得指定名称的参数值，若有多个值，则取第一个值
public String getParameter(Hashtable<String,ArrayList> prms,String name){
   String value = "";
   if ( name == null || name.trim().length() == 0 )
     return value; //如果参数的名称为null或参数名字由空字符组成，则返回一个长度为0的字符串
   value = (prms.get(name) == null)?"":(String)((ArrayList)prms.get(name)).get(0);
   return value;
}
//获得指定名称的参数值序列，返回一个字符数组
public String[] getParameters(Hashtable<String,ArrayList> prms,String name){
   if ( name == null || name.trim().length() == 0 )
       return null;
   if ( prms.get(name) == null )
       return null;
   ArrayList al = (ArrayList)prms.get(name);
   String[] strArr = new String[al.size()];
   for ( int i=0;i<al.size();i++ )
       strArr[i] = (String)al.get(i);
   return strArr;
}
/*********************************************************************************************************************
 * <br>函数名称：getPrms
 * <br>传入参数: 请求、响应、上传目录
 * <br>创建时间：2010年04月13日10时47分
 * <br>主要功能：获取form中的参数及数值，并将需要上载的文件存入服务器。
*********************************************************************************************************************/
Hashtable<String,ArrayList> getPrms(HttpServletRequest request,HttpServletResponse response,String uploadPath) { //初始化参数信息
//全局信息
//初始化参数散列<prmnm,prmvls>
Hashtable<String,ArrayList> prms = new Hashtable<String,ArrayList>();
int BUFSIZE = 1024 * 8; //每次读取的字节大小

//运行信息
String err = "";
String msg = "";
//所有输入字符流信息
String strInput = "";

try{ //排除异常
  //初始化临时变量
  String prmnm = null; //参数名
  String prmvl = null; //参数值
  String filnm = null; //文件名
  ArrayList prmvls = null; //参数值列表
  ArrayList filnms = null; //文件名列表
  File tmpFile = null; //临时文件
  FileOutputStream baos = null; //文件输出流
  BufferedOutputStream bos = null; //输出缓冲区

  //缓冲区信息
  int rtnPos = 0; //从输入流中读出的字节数
  byte[] buffs = new byte[BUFSIZE * 8]; //字节缓冲区

  //分割符
  String contentType = request.getContentType(); // 取得ContentType
  if(contentType == null){ //若内容类型不存在，则直接返回
    return prms;
  }
  int index = contentType.indexOf("boundary="); //获得分割符首索引
  String boundary = "--" + contentType.substring(index + 9); //得到参数开始标志
  String endBoundary = boundary + "--"; //得到参数结束标志
  ServletInputStream sis = request.getInputStream(); //从request对象中取得流。

  //循环读取
  while ((rtnPos = sis.readLine(buffs, 0, buffs.length)) != -1) { //循环读取，每次读取1行
    String strBuff = new String(buffs, 0, rtnPos); //获得第一行的字符串
    if (strBuff.startsWith(boundary)) { //如果是参数开始标志

      //如果上一参数未关闭，则关闭
      if (prmnm != null && prmnm.trim().length() > 0) { //参数名不为空，且不是由空字符组成

        //保存参数或文件信息
        if (filnm == null) { //如果是一般参数（文件名为空）
          prmvls = prms.get(prmnm); //试图取出名称对应的参数值列表
          if(prmvls == null) prmvls = new ArrayList(); //若不存在，则创建新的
          prmvls.add(prmvl); //添加参数值
          prms.put(prmnm,prmvls); //将更新后的参数值列表加入到散列中
        } else if ( filnm.trim().length() == 0 ){ //如果文件名由空白字符组成
          filnm = ""; //将文件名置空，这一赋值在开始标志中应该已经完成
          filnms = prms.get(prmnm); //试图取出参数名对应的文件地址列表
          if(filnms == null) filnms = new ArrayList(); //若不存在，则创建新的
          filnms.add(filnm); //添加新的文件名
          prms.put(prmnm,filnms); //将更新后的文件名列表加入到散列中
        } else { //它是文件,则直接将文件名放入列表，再存入散列
          filnms = prms.get(prmnm); //试图取出参数名对应的文件地址列表
          if(filnms == null) filnms = new ArrayList(); //若不存在，则创建新的
          filnms.add(filnm); //添加新的文件名
          prms.put(prmnm,filnms); //将更新后的文件名列表加入到散列中
          //关闭流
          bos.flush();
          baos.close();
          bos.close();
        } //文件名是否存在判断结束

        //初始化临时变量
        prmnm = null; //参数名
        prmvl = null; //参数值
        filnm = null; //文件名
        prmvls = null; //参数值列表
        filnms = null; //文件名列表
        tmpFile = null; //临时文件
        baos = null; //文件输出流
        bos = null; //输出缓冲区
      } //关闭上一参数结束

      rtnPos = sis.readLine(buffs, 0, buffs.length); //开始读取参数开始的相关信息
      if (rtnPos == -1){ //如果没有读出，则进入下一循环
        continue; //进入下一循环
      }
      strBuff = new String(buffs, 0, rtnPos); //得到字符串，即参数信息
      if (!strBuff.toLowerCase().startsWith("content-disposition: form-data; ")) { //如果不是form数据，则进入下一循环
        continue;
      }

      //获取参数名，初始化参数值
       int nIndex = strBuff.toLowerCase().indexOf("name=\""); //参数名开始索引
       int nLastIndex = strBuff.toLowerCase().indexOf("\"", nIndex + 6); //参数名结束索引
       if (nIndex != -1 && nLastIndex != -1) { //如果索引有效
         prmnm = strBuff.substring(nIndex + 6, nLastIndex); //获得参数名 name = input_file
       } else { //如果没有得到参数名，进入下一循环
         continue;
       }
       prmvl = ""; //初始化参数值

       //获取文件名
       int fIndex = strBuff.toLowerCase().indexOf("filename=\""); //获取文件名的索引
       int fLastIndex = strBuff.toLowerCase().indexOf("\"", fIndex + 10); //得到文件名的尾索引
       if (fIndex != -1 && fLastIndex != -1) {
         filnm = strBuff.substring(fIndex + 10, fLastIndex); //获取文件名 D:\JSP-ACS\aaa.txt
         if (filnm.trim().length() != 0) { //如果文件名不是由空白字符组成，则加上时间戳
           filnm = this.getFileName(filnm); //获取文件的名称 aaa.txt
           filnm = "/" + this.getFileNameByTime(filnm) + "aaaa"; //文件名加上时间戳
           //初始化文件流
           //filnm = uploadPath + "/" + filnm; //添加上传地址
           tmpFile = new File(uploadPath); //由脚本来确定文件的位置
           baos = new FileOutputStream(tmpFile);
           bos = new BufferedOutputStream(baos);
         }
       }
       if (filnm != null) { //如果是文件
         rtnPos = sis.readLine(buffs, 0, buffs.length); //跳过一行文件类型：Content-Type: text/plain
         strBuff = new String(buffs, 0, rtnPos);
       }
       rtnPos = sis.readLine(buffs, 0, buffs.length); //跳过一行空白
       strBuff = new String(buffs, 0, rtnPos);

    } else if (strBuff.startsWith(endBoundary)) { //如果是参数结束标志

      //保存参数或文件信息
      if (filnm == null) { //如果是一般参数（文件名为空）
        prmvls = prms.get(prmnm); //试图取出名称对应的参数值列表
        if(prmvls == null) prmvls = new ArrayList(); //若不存在，则创建新的
        prmvls.add(prmvl); //添加参数值
        prms.put(prmnm,prmvls); //将更新后的参数值列表加入到散列中
      } else if ( filnm.trim().length() == 0 ){ //如果文件名由空白字符组成
        filnm = ""; //将文件名置空，这一赋值在开始标志中应该已经完成
        filnms = prms.get(prmnm); //试图取出参数名对应的文件地址列表
        if(filnms == null) filnms = new ArrayList(); //若不存在，则创建新的
        filnms.add(filnm); //添加新的文件名
        prms.put(prmnm,filnms); //将更新后的文件名列表加入到散列中
      } else { //它是文件,则直接将文件名放入列表，再存入散列
        filnms = prms.get(prmnm); //试图取出参数名对应的文件地址列表
        if(filnms == null) filnms = new ArrayList(); //若不存在，则创建新的
        filnms.add(filnm); //添加新的文件名
        prms.put(prmnm,filnms); //将更新后的文件名列表加入到散列中
        //关闭流
        bos.flush();
        baos.close();
        bos.close();
      } //文件名是否存在判断结束

      //初始化临时变量
      prmnm = null; //参数名
      prmvl = null; //参数值
      filnm = null; //文件名
      prmvls = null; //参数值列表
      filnms = null; //文件名列表
      tmpFile = null; //临时文件
      baos = null; //文件输出流
      bos = null; //输出缓冲区
    } else { //如果是参数的内容部分
      if ( prmnm == null ) { continue; } //如果参数名为空，则转入下一循环
      if ( filnm == null ) { //如果是一般参数
        System.out.println("test :" + prmvl + "--" + strBuff);
        prmvl = prmvl + strBuff; //累加字符串
      } else if ( filnm.trim().length() == 0 ) { //如果文件名由空白字符组成，则进入下一循环
        continue; //此行应该为空白，故直接跳过
      } else { //参数是一个文件
        bos.write(buffs, 0, rtnPos); //写入文件
        baos.flush();
      } //判断是否为文件结束

    } //判断标志结束

  } //循环读取结束

} catch (IOException e) { //捕捉IO异常
  err = "Fil.process() IOException:" + e.toString() + "<br>";
  System.out.println(err); //在命令行中输入出错信息
} //排除异常结束
return prms;
} //方法init结束

%>
<%
String htmAll = "";//需要显示的内容
//定义允许上传的文件扩展名
String extarr = "gif,jpg,png,bmp,swf,mp3,wmv";
String ext_arr[] = extarr.split(",");
//最大文件大小
int max_size = 10000000;
String uploadPath = "";
uploadPath = request.getParameter("AEE_uploadFinally");
Hashtable<String,ArrayList> prms = getPrms(request,response,uploadPath); //至此就已经把文件上传完了
out.println("uploadPath:" + uploadPath + "<br>");
%>
<%
//out.println(getStrInput(request,response));
//out.println(prms.get("AEE_uploadPath"));
%>
