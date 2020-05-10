# tkd_management_system

* 代码clone下来后，先创建虚拟环境，然后用pip下载requirements.txt的依赖包

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
