/**************************************************
 * 创建数据库：
 * 1、ilv_是系统前缀，用户定义变量时尽量避开。
 * 2、ilv_db是系统数据库。
 * 3、数据库中的数据表一般不使用ilv_前缀。
 * 核心数据：会员、栏目、模块、新闻（评论、相册、留言板、雄鹰心语、邮箱以所属栏目区分）
 * 展示模块：新闻 博客　微博　论坛
 * 通用操作：浏览　添加　删除　编辑　查找　显示
 * 所有类别以所属栏目区分
**************************************************/
CREATE DATABASE ilv_db;
USE ilv_db;
SET NAMES utf8;

/**************************************************
 * 栏目表：
**************************************************/
CREATE TABLE `item` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT, # 0自动序号
  `sid`         BIGINT UNSIGNED      DEFAULT '0', # 1手动序号
  `name`        VARCHAR(255)         DEFAULT 'news', # 2 保存位置
  `account`     TEXT, # 3帐号
  `title`       TEXT, # 4昵称，标题
  `ip`          TEXT, # 5发表IP  
  `password`    TEXT, # 6密码
  `item`        BIGINT UNSIGNED      DEFAULT '13', # 7栏目
  `icon`        TEXT, # 8头像
  `video`       TEXT, # 9视频
  `image`       TEXT, # 10图片
  `attach`      TEXT, # 11附件
  `summary`     TEXT, # 12简介
  `detail`      TEXT, # 13详情
  `dtname`      TEXT, # 14数据表
  `class`       VARCHAR(255)         DEFAULT 'News', # 15操作类
  `module`      TEXT, # 16模块
  `css`         VARCHAR(255)         DEFAULT '', # 17样式表位置
  `level`       SMALLINT(1)          DEFAULT '1', # 18权限0游客1会员2实名7管理8设计
  `hire`        SMALLINT(1)          DEFAULT '1', # 19录用0查封 1普通 2良好 3优质
  `hide`        SMALLINT(1)          DEFAULT '1', # 20隐藏0隐藏 1显示
  `del`         SMALLINT(1)          DEFAULT '1', # 21删除0恢复 1删除
  `datetime`    DATETIME, # 22时间
  `millisecond` SMALLINT(3)          DEFAULT '0', # 23毫秒
  `user`        BIGINT UNSIGNED      DEFAULT '1', # 24管理员
  `source`      BIGINT UNSIGNED      DEFAULT '0', # 25文章数量
  `coment`      BIGINT UNSIGNED      DEFAULT '0', # 26评论数量
  `cite`        BIGINT UNSIGNED      DEFAULT '0', # 27转发数量
  `heat`        BIGINT UNSIGNED      DEFAULT '0', # 28粉丝数量 关注数量
  `score`       BIGINT UNSIGNED      DEFAULT '0', # 29会员积分
  `timedelta`   DATETIME , # 30时间区间
   PRIMARY KEY (`kid`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1  DEFAULT CHARSET=utf8;

# 顶级栏目
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('10','0','2','首页','www','news'); # 内容集中到/www下
update `item` set `module`='module/' where `kid`='10' limit 1;
# 一级栏目(11~20)：应用 模块 会员 信箱 栏目
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('1011','10','2','新闻中心','base','news');
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('1012','10','2','模块','module','news');
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('1013','10','2','会员','user','user');
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('101301','1013','2','管理团队','user','user');
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('101302','1013','2','实名会员','user','user');
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('101303','1013','2','普通会员','user','user');
INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`,`dtname`)VALUES('101304','1013','2','受限会员','user','user');
update `item` set `module`='module/user/' where `kid` like '1013%' limit 10;
update `item` set `class`='User' where `kid` like '1013%' limit 10;

INSERT INTO`item`(`kid`,`item`,`level`,`title`,`name`)VALUES('1014','10','2','栏目','item');
update `item` set `module`='module/item/' where `kid`='1014' limit 1;
update `item` set `dtname`='item' where `kid`='1014' limit 1;

INSERT INTO`item`
(`kid`,`item`,`level`,`title`,`name`,`dtname`,`module`)
VALUES('1015','10','2','活动足迹','active','active','module/active/');

# news
#insert into `item`(`kid`,`item`,`title`,`name`,`dtname`,`module`)
#values('101101','1011','新闻','news','news','module/news/');

# 二级栏目(21~30)：微博
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('1021','10','微博','weibo');
update `item` set `module`='weibo/' where `kid`='1021' limit 1;
# 特色栏目(2101~2110)
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102101','1021','大厅','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102102','1021','微刊','MicroMagazine');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102103','1021','相册','MicroAlbums');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('10210301','102103','相册1','MicroAlbums');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('10210302','102103','相册2','MicroAlbums');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('10210303','102103','相册3','MicroAlbums');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102104','1021','微吧','MicroBar');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102105','1021','求助','MicroHelp');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102106','1021','百科','MicroBaiKe');

INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('1022','10','大厅2','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102201','1022','大厅2201','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102202','1022','大厅2202','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102203','1022','大厅2203','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102204','1022','大厅2204','news');

INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('1023','10','大厅3','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102301','1022','大厅2301','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102302','1022','大厅2302','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102303','1022','大厅2303','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('102304','1022','大厅2304','news');



/**************************************************
 * 插入正常栏目：
**************************************************/
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101101','1011','娱乐','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101102','1011','时事','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101103','1011','军事','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101104','1011','财经','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101105','1011','科技','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101106','1011','时尚','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101107','1011','健康','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101108','1011','体育','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101109','1011','文化','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101110','1011','星座','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101111','1011','幽默','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101112','1011','警句','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101113','1011','社会','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101114','1011','视频','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101115','1011','环境','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101116','1011','教育','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101117','1011','农业','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101118','1011','医疗','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101119','1011','旅游','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101120','1011','宠物','news');
INSERT INTO`item`(`kid`,`item`,`title`,`name`)VALUES('101121','1011','海外','news');

/**************************************************
 * 创建用户表：
**************************************************/
CREATE TABLE `user` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT, # 0自动序号
  `sid`         BIGINT UNSIGNED      DEFAULT '0', # 1手动序号
  `name`        VARCHAR(255)         DEFAULT 'user', # 2类
  `account`     TEXT, # 3帐号
  `title`       TEXT, # 4昵称，标题
  `ip`          TEXT, # 5发表IP  
  `password`    TEXT, # 6密码
  `item`      BIGINT UNSIGNED      DEFAULT '1013', # 7栏目
  `icon`        TEXT, # 8头像
  `video`       TEXT, # 9视频
  `image`       TEXT, # 10图片
  `attach`      TEXT, # 11附件
  `summary`     TEXT, # 12简介
  `detail`      TEXT, # 13详情
  `dtname`      TEXT, # 14数据表
  `class`       VARCHAR(255)         DEFAULT 'User', # 15操作类
  `module`      TEXT, # 16模块
  `css`         TEXT, # 17样式表位置
  `level`       SMALLINT(1)          DEFAULT '1', # 18权限0游客1会员2实名7管理8设计
  `hire`        SMALLINT(1)          DEFAULT '0', # 19录用0待审 1普通 2优质 3头条
  `hide`        SMALLINT(1)          DEFAULT '1', # 20隐藏0隐藏 1显示
  `del`         SMALLINT(1)          DEFAULT '1', # 21删除0删除 1恢复
  `datetime`    DATETIME, # 22时间
  `millisecond` SMALLINT(3)          DEFAULT '0', # 23毫秒
  `user`        BIGINT UNSIGNED      DEFAULT '1', # 24管理员
  `source`      BIGINT UNSIGNED      DEFAULT '0', # 25文章数量
  `coment`      BIGINT UNSIGNED      DEFAULT '0', # 26评论数量
  `cite`        BIGINT UNSIGNED      DEFAULT '0', # 27转发数量
  `heat`        BIGINT UNSIGNED      DEFAULT '0', # 28粉丝数量 关注数量
  `score`       BIGINT UNSIGNED      DEFAULT '0', # 29会员积分
  `timedelta`   DATETIME, # 30时间区间
   PRIMARY KEY (`kid`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1  DEFAULT CHARSET=utf8;

# 插入会员
INSERT INTO`user`(`kid`,`account`,`password`,`title`)VALUES('1','guest','guest','游客');
INSERT INTO`user`(`kid`,`account`,`password`,`title`)VALUES('2','root','root','设计师');
INSERT INTO`user`(`kid`,`account`,`password`,`title`)VALUES('3','admin','admin','管理员');

/**************************************************
 * 登录表：
**************************************************/
CREATE TABLE `active` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT, # 0自动序号
  `sid`         BIGINT UNSIGNED      DEFAULT '0', # 1手动序号
  `name`        VARCHAR(255)         DEFAULT 'news', # 2 保存位置
  `account`     TEXT, # 3帐号
  `title`       TEXT, # 4昵称，标题
  `ip`          TEXT, # 5发表IP  
  `password`    TEXT, # 6密码
  `item`      BIGINT UNSIGNED      DEFAULT '1015', # 7栏目
  `icon`        TEXT, # 8头像
  `video`       TEXT, # 9视频
  `image`       TEXT, # 10图片
  `attach`      TEXT, # 11附件
  `summary`     TEXT, # 12简介
  `detail`      TEXT, # 13详情
  `dtname`      TEXT, # 14数据表
  `class`       VARCHAR(255)         DEFAULT 'News', # 15操作类
  `module`      TEXT, # 16模块
  `css`         VARCHAR(255)         DEFAULT '', # 17样式表位置
  `level`       SMALLINT(1)          DEFAULT '1', # 18权限0游客1会员2实名7管理8设计
  `hire`        SMALLINT(1)          DEFAULT '1', # 19录用0启用 1查封
  `hide`        SMALLINT(1)          DEFAULT '1', # 20隐藏0隐藏 1显示
  `del`         SMALLINT(1)          DEFAULT '1', # 21删除0删除 1恢复
  `datetime`    DATETIME, # 22时间
  `millisecond` SMALLINT(3)          DEFAULT '0', # 23毫秒
  `user`        BIGINT UNSIGNED      DEFAULT '1', # 24管理员
  `source`      BIGINT UNSIGNED      DEFAULT '0', # 25文章数量
  `coment`      BIGINT UNSIGNED      DEFAULT '0', # 26评论数量
  `cite`        BIGINT UNSIGNED      DEFAULT '0', # 27转发数量
  `heat`        BIGINT UNSIGNED      DEFAULT '0', # 28粉丝数量 关注数量
  `score`       BIGINT UNSIGNED      DEFAULT '0', # 29会员积分
  `timedelta`   VARCHAR(255)         DEFAULT '0000-00-00 00:00:00', # 30时间区间
   PRIMARY KEY (`kid`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1  DEFAULT CHARSET=utf8;


/**************************************************
 * 新闻表：
**************************************************/
CREATE TABLE `news` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT, # 0自动序号
  `sid`         BIGINT UNSIGNED      DEFAULT '0', # 1手动序号
  `name`        VARCHAR(255)         DEFAULT 'news', # 2类
  `account`     TEXT, # 3帐号
  `title`       TEXT, # 4昵称，标题
  `ip`          TEXT, # 5发表IP  
  `password`    TEXT, # 6密码
  `item`      BIGINT UNSIGNED      DEFAULT '1021', # 7栏目
  `icon`        TEXT, # 8头像
  `video`       TEXT, # 9视频
  `image`       TEXT, # 10图片
  `attach`      TEXT, # 11附件
  `summary`     TEXT, # 12简介
  `detail`      TEXT, # 13详情
  `dtname`      TEXT, # 14数据表
  `class`       VARCHAR(255)         DEFAULT 'News', # 15操作类
  `module`      TEXT, # 16模块
  `css`         TEXT, # 17样式表位置
  `level`       SMALLINT(1)          DEFAULT '1', # 18权限0游客1会员2实名7管理8设计
  `hire`        SMALLINT(1)          DEFAULT '1', # 19录用0启用 1查封
  `hide`        SMALLINT(1)          DEFAULT '1', # 20隐藏0隐藏 1显示
  `del`         SMALLINT(1)          DEFAULT '1', # 21删除0删除 1恢复
  `datetime`    DATETIME, # 22时间
  `millisecond` SMALLINT(3)          DEFAULT '0', # 23毫秒
  `user`        BIGINT UNSIGNED      DEFAULT '1', # 24管理员
  `source`      BIGINT UNSIGNED      DEFAULT '0', # 25文章数量
  `coment`      BIGINT UNSIGNED      DEFAULT '0', # 26评论数量
  `cite`        BIGINT UNSIGNED      DEFAULT '0', # 27转发数量
  `heat`        BIGINT UNSIGNED      DEFAULT '0', # 28粉丝数量 关注数量
  `score`       BIGINT UNSIGNED      DEFAULT '0', # 29会员积分
   PRIMARY KEY (`kid`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1  DEFAULT CHARSET=utf8;

/**************************************************
 * 插入记录：
**************************************************/
# 默认记录
INSERT INTO`news`(`kid`,`item`,`title`,`user`)VALUES('1','10','记录不存在提示（勿删）','2');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`)VALUES('2','10','暂无优质新闻（勿删）','2','2');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`)VALUES('3','10','暂无头条新闻（勿删）','2','3');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`video`)VALUES('4','10','暂无视频新闻（勿删）','2','1','/module/js/AEV/1.flv');

INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('11','10','图片信息1','2','3','/upload/image/1.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('12','10','图片信息2','2','3','/upload/image/2.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('13','10','图片信息3','2','3','/upload/image/3.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('14','10','图片信息4','2','3','/upload/image/4.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('15','10','图片信息5','2','3','/upload/image/5.jpg');

INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('21','102201','图片信息21','2','3','/upload/image/1.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('22','102201','图片信息22','2','3','/upload/image/2.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('23','102201','图片信息23','2','3','/upload/image/3.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('24','102201','图片信息24','2','3','/upload/image/4.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('25','102201','图片信息25','2','3','/upload/image/5.jpg');

INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('31','102101','图片信息31','2','3','/upload/image/1.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('32','102101','图片信息32','2','3','/upload/image/2.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('33','102101','图片信息33','2','3','/upload/image/3.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('34','102101','图片信息34','2','3','/upload/image/4.jpg');
INSERT INTO`news`(`kid`,`item`,`title`,`user`,`hire`,`image`)VALUES('35','102101','图片信息35','2','3','/upload/image/5.jpg');


/**************************************************
 * 图片表：
**************************************************/
CREATE TABLE `images` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT,
  `sid`         BIGINT UNSIGNED      DEFAULT '0',
  `item`      BIGINT UNSIGNED      DEFAULT '0',
  `type`        TINYINT UNSIGNED     DEFAULT '1', # 类型 1:原创 2:转发 3:评论
  `icon`         TEXT, # 示意图标，在记录前标识
  `title`       TEXT,
  `name`        TEXT,
  `summary`     TEXT, # 摘要
  `detail`      TEXT, # 详情
  `level`       TINYINT UNSIGNED     DEFAULT '1', # 权限 1:正常 2:游客 3：已查封 4:待审核 5:已删除
  `password`    TEXT,
  `datetime`    DATETIME,
  `microseconds`MEDIUMINT UNSIGNED   DEFAULT '0',
  `source`      BIGINT UNSIGNED      DEFAULT '0', # 文章序号
  `user`        BIGINT UNSIGNED      DEFAULT '1',
  `ip`          VARCHAR(255)         DEFAULT '127.0.0.1',
  `heat`        BIGINT UNSIGNED      DEFAULT '0',
   PRIMARY KEY (`kid`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('1','/upload/images/1.jpg','文章1图片','1');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('2','/upload/images/2.jpg','文章2图片','2');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('3','/upload/images/3.jpg','文章3图片','3');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('4','/upload/images/4.jpg','文章4图片','4');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('5','/upload/images/5.jpg','文章5图片','5');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('6','/upload/images/6.jpg','文章6图片','6');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('7','/upload/images/7.jpg','文章7图片','7');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('8','/upload/images/8.jpg','文章8图片','8');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('9','/upload/images/9.jpg','文章9图片','9');
INSERT INTO`images`(`kid`,`summary`,`title`,`source`)VALUES('10','/upload/images/10.jpg','文章10图片','10');

/**************************************************
 * 语言表：
**************************************************/
CREATE TABLE `language` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT,        # The id of the language
  `sid`         BIGINT UNSIGNED      DEFAULT '0',                    # The view order of the language
  `name`        TEXT,                     # The name of the language
  `summary`     TEXT,                     # The discription of the language
   PRIMARY KEY (`kid`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1  DEFAULT CHARSET=utf8;
INSERT INTO`language`(`kid`,`name`)VALUES('1','简体中文');
INSERT INTO`language`(`kid`,`name`)VALUES('2','English');
/**************************************************
 * 翻译表：
**************************************************/
CREATE TABLE `translation` (
  `kid`         BIGINT UNSIGNED      NOT NULL AUTO_INCREMENT,        # The id
  `sid`         BIGINT UNSIGNED      DEFAULT '0',                    # The view order
  `search`      TEXT,                     # The search word
  `answer`      TEXT,                     # The translation
  `summary`     TEXT,                     # Explain in detail
  `source`      BIGINT UNSIGNED      DEFAULT '1',                    # Source language
  `aim`         BIGINT UNSIGNED      DEFAULT '2',                    # Aim language
  `heat`        BIGINT UNSIGNED      DEFAULT '0',                    # How many people suggested
   PRIMARY KEY (`kid`)
   #INDEX(`search`)
)  #TYPE=MyISAM 
AUTO_INCREMENT=1  DEFAULT CHARSET=utf8;
/*参数解释*/
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('c','栏目号','1','2');  # item id
# a action 1添加2编辑3删除4注册5登录6注销
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('a','行为','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('index','索引','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('add','添加','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('edit','编辑','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('del','删除','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('w','微博ID','1','2'); # weibo id = user id
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('r','记录号 ','1','2'); # record id
# t type 网站类别 1微博 2论坛
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('t','显示类型','1','2');


INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('administrator','管理员','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('guest','访客','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('ilvbobing','爱履薄冰','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('p','会员号','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('h','微博主','1','2');
INSERT INTO`translation`(`search`,`answer`,`source`,`aim`)VALUES('what','什么','1','2');







