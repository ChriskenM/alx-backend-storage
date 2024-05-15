<h1> redis_basic </h1>

- Read or watch:

- Redis Crash Course Tutorial
- Redis commands
- Redis python client
- How to Use Redis With Python

<h3>Requirements</h3>

- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly #!/usr/bin/env python3

<h3> Install Redis on Ubuntu 18.04 </h3>

```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
