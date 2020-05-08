# 创建容器

docker hub官方文档中命令
```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d -p 本机端口:3306 mysql:tag --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```
将容器内部端口3306绑定到主机端口，在python模块中需要主机端口的参数。本项目用的mysql版本是5.7

# 修改mysql容器的字符编码，若不修改，数据库无法正常使用中文

* 进入容器
```
docker exec -it 容器 /bin/bash
```
* 执行代码
```
SET NAMES 'utf8';
```
* 修改配置文件etc/mysql/mysql.conf.d/mysql.cnf，补上缺少的内容
```
[mysqld]
default-character-set = utf8
character_set_server = utf8

[mysql]
default-character-set = utf8

[mysql.server]
default-character-set = utf8

[mysqld_safe]
default-character-set = utf8

[client]
default-character-set = utf8
```

# 在容器中创建数据库
* 进入容器
```
docker exec -it 容器 /bin/bash
```
* 进入mysql
```
mysql -u root -p
```
* 创建数据库
```
create database tkdbase;
```
