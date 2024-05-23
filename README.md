# web_ui_demo

#### 介绍
web自动化测试框架

#### 软件架构
PO模式三层分离架构


#### 目录结构

    |--web自动化测试框架 # 主目录
       ├─ base # 封装等待元素，页面元素的基本操作方法
       ├─ common # 常用工具
         └─ render_template.py  # 渲染配置文件
         └─ template.conf  # 模板文件
         └─ env.json  # 使用的环境数据
         └─ read_json.py  # 封装测试case数据读取
         └─ utils  # 获取/推出 driver 工具
       ├─ config # 配置文件读取
         └─ config.ini  # 真正运行时的配置文件
         └─ confRead.py   # 封装读取配置文件
       ├─ data # 测试数据相关文件
         └─ xxx.json #测试数据
         └─ xxx.json #测试数据
       ├─ log # 运行时日志
         └─ xxx.log # 日志
       ├─ page # 封装元素获取、操作、业务执行
         └─ xxx.py # 模块封装文件
       ├─ report # allure测试报告	
       ├─ scripts # 测试脚本调用
         └─ conftest.py # 运行用例前置、后置配置，生成allure报告
         └─ test_xxx.py # 运行的用例
       ├─ tmp # allure运行时数据、截图
       ├─ global_config.py	  # 公用log日志封装
       ├─ pytest.ini  	#pytest配置	  
       └─ README.md

#### 使用说明

首先生成运行时的config配置文件
```
cd cd .\common\
python render_template.py template.conf test_env.json ../config/config.ini
```

在项目根目录 多进程执行，命令行执行
```
pytest -n 2
```

单进程执行，注释掉 test_demo_user_home.py 以外test文件中 # @pytest.mark.usefixtures("demo_user_login")
```
pytest -v -m 'smoke'
```

在项目根目录 指定config配置文件执行
```
pytest --confcutdir=./config -v -m 'smoke'
```
