# tkd_management_system

* 代码clone下来后，先创建虚拟环境，然后用pip下载requirements.txt的依赖包
* 该项目使用SQLAlchemy连接docker创建的mysql数据库，所以需要自己额外部署mysql容器，具体步骤查看tkd_gym/mysql_op.md

pip3 install

### Deployment guide

Start up
```bash
$ docker-compose up -d
```
Once succeed, visit web page here: http://127.0.0.1:5000/

Status of container
```bash
$ docker-compose ps
$ docker-compose top
$ docker-compose logs -f
```

Shut down service
```bash
$ docker-compose rm -sf
```
