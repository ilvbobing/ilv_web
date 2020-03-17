/**************************************************************
*作品简介：
***************************************************************
*名称：Ailvboing's Easy Editor
*简称: AEE
*时间：2009年10月18日20时32分
*名称：简单文本编辑器（随便起个名字）
*功能：实现网上所见即所得的编辑（算得上是名符其实）
*特点：尽量用较少的代码完成最多的功能（好像有点矛盾）
*希望：能够像Word一样功能强大（纯粹是痴心妄想）
*作者：爱履薄冰(Ailvbobing)（在网上的代号）
*QQ号：137284422（使用时间应该很长）
*版本: 3.0.0.0
**************************************************************/
版本更新：
1、1.0.0.0 
  制作时间 : 2009年10月18日20时32分至2009年10月22日01时24分 实用时间约20小时 
  界面简单：纯黑白色 
  程序清晰：只有一层，没有程序嵌套
  存在不足：粘贴功能未能完成
2、2.0.0.0
  制作时间：2009年10月20日至2009年10月24日，
  程序更新：加入IFrame技术
3、3.0.0.0
  制作时间：2009年10月29日至2009年11月03日
  程序更新：添加IFrame包装，代码进行了模块化

一、测试环境

1、操作系统：Microsoft Windows XP Professional 2002 Service Pack 3
2、浏览器：Microsoft Internet Explorer 6.0
3、服务器：APMXE5

二、属性和方法

AEE.appandChild(child) AEE.designBody插入结点(子结点)

AEE.background(color) 设置背景颜色(颜色)

AEE.changeMode(img) 改变编辑方式 所见即所得编辑 <<====>>代码编辑(按钮图标)

AEE.color(color) 设置文本颜色(颜色)

AEE.colors 颜色数组

AEE.flashTypes Flash文件类型数组

AEE.fontFamily(cmd,str) 设置字体(命令,字体名称)

AEE.fontFamilys 字体数组

AEE.getLeft(id) 获得对象的绝对横坐标(结点)

AEE.getNows() 获得当前的日期和时间

AEE.getPath() 获得脚本相对地址

AEE.getTop() 获得对象的绝对纵坐标

AEE.icons 工具栏图标

AEE.imageTypes 图片文件类型列表

AEE.insertDate(img) 插入日期和时间(按钮图标)

AEE.insertHr(img) 插入彩色分割线(按钮图标)

AEE.insertLink(img) 插入超级链接(按钮图标)

AEE.insertMood(img) 插入表情图标(按钮图标)

AEE.insertSign(img) 插入特殊符号(按钮图标)

AEE.insertSize(img) 插入文字大小(按钮图标)

AEE.insertTable(img) 插入表格(按钮图标)

AEE.insertTitle(img) 插入大纲标题(按钮图标)

AEE.language 程序术语

AEE.layer(color) 插入彩色层(颜色)

AEE.mediaTypes 视频文件类型数组

AEE.name 程序名称

AEE.preview(menuName) 预览窗体、图片、Flash、视频(菜单名称)

AEE.show(id,value,width,height,uploadPath,bgColor,menuColor,borderColor,selectColor)显示插件

AEE_showCodeTextarea() 弹出所见即所得窗体designBody内容

AEE_showContentInput() 弹出文本域contentInput内容

AEE.showColorTable(img,menuName) 显示彩色图表(图标按钮,图标名称) 

AEE.showPopupDiv(img,html) 显示弹出菜单(按钮图标,内部html)

AEE.showUploadWin(img,menuName) 显示上传窗口(图标按钮,图标名称)

AEE.updateContentInput() 更新文本域内容

AEE.updateSelection() 更新焦点

AEE.upload(menuName) 上传附件(菜单名称)

AEE.uploadPlace() 更改附件位置

AEE.version 程序版本

三、注意

编辑器中的全局变量，均带有“AEE_”前缀，用户在自定义全局变量时，请尽量避免与编辑器冲突。