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
  tp.speed = 50;//每50ms偏移一次
  tp.div = div;
  tp.div1 = div1;
  tp.div2 = div2;
  tp.div2.innerHTML = tp.div1.innerHTML;
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
  lft.speed = 50;//每50ms偏移一次
  lft.div = div;
  lft.div1 = div1;
  lft.div2 = div2;
  lft.div2.innerHTML = lft.div1.innerHTML;
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
  rht.div2.innerHTML = rht.div1.innerHTML;
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
