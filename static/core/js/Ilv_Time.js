getbigdate = function(){
  var day="";
  var month="";
  var ampm="";
  var ampmhour="";
  var myweekday="";
  var year="";
  mydate=new Date();
  myweekday=mydate.getDay();
  mymonth=mydate.getMonth()+1;
  myday= mydate.getDate();
  myyear= mydate.getYear();
  year=(myyear > 200) ? myyear : 1900 + myyear;
  if(myweekday == 0)
  weekday=" 星期日 ";
  else if(myweekday == 1)
  weekday=" 星期一 ";
  else if(myweekday == 2)
  weekday=" 星期二 ";
  else if(myweekday == 3)
  weekday=" 星期三 ";
  else if(myweekday == 4)
  weekday=" 星期四 ";
  else if(myweekday == 5)
  weekday=" 星期五 ";
  else if(myweekday == 6)
  weekday=" 星期六 ";
  //document.write(year+"年"+mymonth+"月"+myday+"日 "+weekday);
  //转换日期
  bigyears = ["〇","一","二","三","四","五","六","七","八","九"];
  bigyear = "二〇二" + bigyears[year-2020] + "年";
  bigmonths = ["一","二","三","四","五","六","七","八","九","十","十一","十二"];
  bigmonth = bigmonths[mydate.getMonth()] + "月";
  bigdays = [
  "一","二","三","四","五","六","七","八","九","十",
  "十一","十二","十三","十四","十五","十六","十七","十八","十九","二十",
  "二十一","二十二","二十三","二十四","二十五","二十六","二十七","二十八","二十九","三十",
  "三十一"
  ];
  bigday = bigdays[mydate.getDate() - 1 ] + "日";
  bighour = mydate.getHours()>9 ? mydate.getHours() : "0"+mydate.getHours();
  bigminute = mydate.getMinutes() > 9 ? mydate.getMinutes() : "0" + mydate.getMinutes();
  bigsecond = mydate.getSeconds() >9 ? mydate.getSeconds() : "0" + mydate.getSeconds();
  bigtime = bighour + ":" + bigminute + ":" + bigsecond;
  htmdate = ""+bigyear+bigmonth+bigday+weekday+bigtime+"";
  return htmdate;
}
updatetime = function(dividnm){
  document.getElementById(dividnm).innerHTML = getbigdate();
  window.setTimeout("updatetime('"+dividnm+"')",1000);
}
