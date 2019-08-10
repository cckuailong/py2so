# py2so
[English](https://github.com/cckuailong/py2so/blob/master/README.md) || 
[中文](https://github.com/cckuailong/py2so/blob/master/README_zh.md)

## py2so简介
1. py2so可以将python文件转化为so文件，达到加密python文件的目的
2. py2so加密一个py文件，也可以直接加密一整个python项目
3. .py生成的.so文件可以被主文件通过 "from module import \*" 调用
4. py2so可以自动识别项目中的py文件, 如果项目中某些文件你不想加密，py2so也可以实现你的目的
5. 你可以选择是否保留加密前的文件或项目
6. 考虑到用户误操作，默认会保留加密前的项目，项目名后缀为 "_old"
7. py2so 支持 python2 and python3, py2 --> py2so.py    py3 --> py2so_py3.py

## 环境配置
```
sudo bash config.sh
```
安装一些必要的库

## 使用说明
#### Python2
```
使用: 
  python py2so.py [选项] ...
```

```
选项:
  -v,  --version    显示py2so版本
  -h,  --help       显示帮助菜单
  -p,  --py         Python的子版本号, 默认值为 7
                    例: -p 7  (比如你使用python2.7)
  -d,  --directory  Python项目路径 (如果使用-d参数, 将加密整个Python项目)
  -f,  --file       Python文件 (如果使用-f, 将加密单个Python文件)
  -c,  --clear      删除原文件（项目）
                    (警告: -c参数将会删除原文件, 但是为了避免损失，py2so会自动备份原文件)
  -m,  --maintain   标记你不想加密的文件或文件夹路径
                    注意: 文件夹路径需要使用'[]'包起来, 并且需要和-d参数一起使用 
                    例: -m __init__.py,setup.py,[poc,resource,venv,interface]
```

```
例:
  python py2so.py -f test_file.py
  python py2so.py -d ../test_dir -m __init__.py -c
  python py2so.py -d /home/test/test_dir -m [poc/,resource/,venv/,interface/]
  python py2so.py -d test_dir -m __init__.py,setup.py,[poc/,resource/,venv/,interface/] -c
```
#### Python3
```
使用: 
  python py2so_py3.py [选项] ...
```

```
选项:
  -v,  --version    显示py2so_py3版本
  -h,  --help       显示帮助菜单
  -p,  --py         Python的子版本号, 默认值为 7
                    例: -p 7  (比如你使用python3.7)
  -d,  --directory  Python项目路径 (如果使用-d参数, 将加密整个Python项目)
  -f,  --file       Python文件 (如果使用-f, 将加密单个Python文件)
  -c,  --clear      删除原文件（项目）
                    (警告: -c参数将会删除原文件, 但是为了避免损失，py2so_py3会自动备份原文件)
  -m,  --maintain   标记你不想加密的文件或文件夹路径
                    注意: 文件夹路径需要使用'[]'包起来, 并且需要和-d参数一起使用 
                    例: -m __init__.py,setup.py,[poc,resource,venv,interface]
```

```
例:
  python py2so_py3.py -f test_file.py
  python py2so_py3.py -d ../test_dir -m __init__.py -c
  python py2so_py3.py -d /home/test/test_dir -m [poc/,resource/,venv/,interface/]
  python py2so_py3.py -d test_dir -m __init__.py,setup.py,[poc/,resource/,venv/,interface/] -c
```


整个Python项目加密前:

![demo1](https://github.com/cckuailong/py2so/blob/master/img/1.png)

py2so加密后效果:

![demo2](https://github.com/cckuailong/py2so/blob/master/img/2.png)
