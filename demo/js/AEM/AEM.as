var drag=0.1;//震动参数
var flex=0.7;//震动参数
if(typeof(menusZh)=="undefined"){
	menusZh = "示例菜单1|示例菜单2|示例菜单3|菜单4|示例菜单5";
	}
if(typeof(menusUrl)=="undefined"){
	menusUrl = "http://localhost/|#|#|#|#";
	}
var menuZH=menusZh.split("|");
var menuURL=menusUrl.split("|");
var menuColor=new Array(0xD808B8,0x00A2FF,0x96D302,0xFFC600,0xFF5400,0x90A0E0,0x02D396);
/***************************************************************************************************
 * MovieClip.attachMovie(id:String,name:String,depth:Number)
 * 从库中取得一个元件并将其附加到影片剪辑中
 * id:链接名称 name:实例的唯一名称 depth:元件深度
 * 链接元件背景
***************************************************************************************************/
var mLength = 80; //标题长度
var mBlock=this.attachMovie("mblock","mb",0);
	mBlock._y=5; //背景的横坐标
	mBlock.goalX=-100; //自定义目标长
	mBlock.onEnterFrame=function(){
			this.Step = this.Step * flex + (this.goalX - this.px) * drag;
			this.px+=this.Step;
			this._x=this.px;
			if(this.sOut && this._xscale<99.5) this._xscale+=(100-this._xscale)/8;
			if(this.sIn && this._xscale>0.1) this._xscale+=-this._xscale/8; //_xscale 水平缩向比例
	}
var MBColor=new Color(mBlock); //为背景创建一个颜色调整器
for(var i=0;i<menuZH.length;i++){
    var theItem=this.attachMovie("MenuItem","Item"+i,i+10);
	theItem._x=i*mLength+20; //每个菜单项长度为84px
	theItem.mColor=menuColor[i%7]; //选颜色
	theItem.URL=menuURL[i]; //链接地址
	theItem.mc_ZH.itext.text=menuZH[i]; //中文标题
	theItem.mc_EN.itext.text="more"; //menuEN[i];英文标题
	theItem.onEnterFrame=function(){
		if(this.fadeOut){
			if(this.topLine._alpha<99.5) this.topLine._alpha+=(mLength-this.topLine._alpha)/8;
			if(this.mc_EN._alpha>0.5) this.mc_EN._alpha+=-this.mc_EN._alpha/8;
			if(this.mc_ZH._xscale<100) {this.mc_ZH._xscale+=2;this.mc_ZH._yscale+=2;}
		}
			
		if(this.fadeIn){
			if(this.mc_EN._alpha<99.5) this.mc_EN._alpha+=(100-this.mc_EN._alpha)/8;
			if(this.topLine._alpha>0.5) this.topLine._alpha+=-this.topLine._alpha/8;
			if(this.mc_ZH._xscale>100) {this.mc_ZH._xscale-=2;this.mc_ZH._yscale-=2;}
		}
	}
	theItem.onRollOver=function(){
		mBlock.goalX=this._x+42;
		mBlock.sOut=true;
		mBlock.sIn=false;
		MBColor.setRGB(this.mColor);
		new Color(this.topLine).setRGB(this.mColor);
		//new Color(this.mc_ZH).setRGB(0xFFFFFF);
		this.fadeOut=true;
		this.fadeIn=false;
	}
	theItem.onRollOut=function(){
		mBlock.sOut=false;
		mBlock.sIn=true;
		//new Color(this.mc_ZH).setRGB(0x000000);
		this.fadeIn=true;
		this.fadeOut=false;		
	}	
	theItem.onRelease=function(){
		getURL(this.URL);
	}
}
stop();