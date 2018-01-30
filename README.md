# Grants_Prediction
大学生助学金评定Echatrs图表显示说明

##文件介绍
包括路径下的各种文件作用

1. **data** : data文件夹下存放各项学生的在校源数据,用于提取可视化数据信息使用.

	>data
	>>borrow\_train_invert.txt 按学号分组,得到每个学号借阅图书的信息

	>>borrow\_train.txt 每个学号借阅图书信息的原文件
	>>
	>>library\_train.txt 每个学号的图书馆门禁记录
	>>
	>>probability.txt 学号获得助学金的概率文件
	>>
	>>score\_train.txt 每个学号所在学院的排名
	>>
	>>welcome.png 显示欢迎界面的图片原文件
	>>
	>>card 包含所有学生一卡通消费记录的文件夹
	>>>0.csv
	>>>9.csv
	>>>22.csv
	>>>...

	>get\_data
	>>borrow.py 得到学生借阅书籍数据
	
	>>card.py 得到学生消费数据
	
	>>change2.py 处理数据格式
	
	>>createStudentForms.py 处理原数据相关代码
	
	>>library.py 统计学生浏览图书馆次数数据
	
	>> probability.py
	
	>>readFromFile.py 读取文件
	
	>>score.py 得到学生成绩数据

2. **get_data** : get_data文件夹下存放实现提取可视化信息的执行代码.
3. **hello.py** : web.py的轻量级python_web框架,实现python与web相结合.
4. **hello.pyc** : 生成的执行文件,可忽略.
5. **index.html** : 初始界面html文件.
6. **render.html** : 生成的echarts可视化图表的html文件.
7. **result.csv** : 结果文件,存放所有学生的学号, 学院, 排名.

##如何运行
* 运行环境需求
	1. python 2.7
	2. web.py : 轻量级python_web框架
	3. pyecharts : echarts的pythonAPI
	
* 运行步骤

	运行hello.py 生成本地链接:
		
		$ python hello.py 
		http://0.0.0.0:8080/

	复制此链接到浏览器,输入需要查询的学号.
	
	*注: **输入的学号必须是当前目录下 result.csv 里存在的学号,否则不会查找到任何信息!**
	
	点击查找后会显示此学生的各项信息入下: 
	
	* 学号(id) 学院(Faculty) 排名(Rank) 概率(Prediction)
	
	返回点击 **详细信息可视化** 会查看此学生的各项可视化信息
##pyecharts包含图表
包含各种图表的简介

	0. 显示欢迎图表 " Welcome "
	1. 仪表盘 显示该学生在此学院的排名情况
	2. 漏斗图 显示该学生消费方式的概况
	3. 饼图 显示该学生消费方式的占比情况
	4. 条形图 显示该学生在该学年每项消费方式额度的情况
	5. 折线图 显示该学生在该学年每项消费方式额度的情况
	6. 条形图(可伸缩, 可移动) 显示该学生该学年 每个月各项消费的总花费额
	7. 套用时间线 应用条形图和折线图 综合显示该学生每月按照消费方式的消费情况
	8. 极坐标图 显示该学生12个月里 进入图书馆次数的情况
	9. 饼图 显示该学生所有阅读过的书籍信息
	10. 流体图 显示该学生获得助学金的概率大小
