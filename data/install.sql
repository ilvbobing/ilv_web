USE ilv_db;
SET NAMES utf8;


# INSERT INTO`column`(`kid`,`column`,`level`,`title`,`name`)VALUES('1014','10','2','栏目','column');
# update `column` set `module`='module/column/' where `kid`='1014' limit 1;
# update `column` set `dtname`='column' where `kid`='1014' limit 1;
# update `column` set `module`='module/user/' where `kid` like '1013%' limit 10;
# update `column` set `class`='User' where `kid` like '1013%' limit 10;
INSERT INTO`column`
(`kid`,`column`,`level`,`title`,`name`,`dtname`,`module`)
VALUES('1015','10','2','活动足迹','active','active','module/active/');




