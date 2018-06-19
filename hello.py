# -*- coding: utf-8 -*-
import web  
import sys
sys.path.append(r'get_data/')

#导入对应检索数据的文件
import score, card, change2, borrow, library, probability, whole_info
#导入pyecharts模块显示所需要的包
from pyecharts import Page, Timeline, Style, Overlap, Scatter, Gauge, \
                      Funnel, Bar, Line, Pie, Polar, Liquid, Radar, EffectScatter

urls = (  
    '/index', 'index',  
    '/blog/\d+', 'blog',  
    '/(.*)', 'hello',
)  
app = web.application(urls, globals())  
  
class hello:          
    def GET(self, name):  
        return open(r'index.html').read()  

class index:  
    def GET(self):  
        query = web.input()  
        print "query : ", query
        return query

class blog:  
    def POST(self):  
        data = dict(web.input())
        #data = str(data)

        if not data['bt_type']:
            return
        else:
            if data['bt_type'] == "bt1":
                print "data: ", data
                stu_id = int(data['id']) #change to int 
                print "type is :", type(data['id'])
                #get_data file func
                guage = score.get_score_data(stu_id)            #提取成绩数据 展示成绩排名
                funnel = card.all_month(stu_id)                 #提取一卡通消费数据 展示消费方式占比
                bar_12month = card.month_sum(stu_id)            #提取一卡通消费数据 按消费方式展示花费金额
                bar_eachmonth = card.each_month(stu_id)         #提取一卡通消费数据 统计每个月的花费总额 按照时间线展示
                pie = borrow.bookname(stu_id)                   #提取图书馆借阅数据 展示阅读过的书籍
                polar = library.librarytime(stu_id)             #提取图书馆门禁记录 记录去过图书馆的次数 按月显示
                prediction = probability.prediction(stu_id)     #获取学号对应获得助学金的概率值 用概率显示
                whole = whole_info.extract(stu_id)				

                #打印提取出来的各项信息
                print "------------------"
                print guage ,funnel, bar_12month, bar_eachmonth, pie, polar, prediction, whole
                print "------------------"
                #create Echarts file func
                create_echarts(guage, 
                               funnel, 
                               bar_12month,
                               bar_eachmonth,
                               pie,
                               polar,
                               prediction,
                               whole).render()             #生成显示网页render.html

                return getid(stu_id, prediction)                #返回查找到的学号id 学院faculty 排名rank 概率prediction
            elif data['bt_type'] == "bt2":
                return open(r'render.html').read()              #打开生成echarts的网页

'''
find student's info from id.csv
'''
def getid(name, pre):
    with open('data/test/result.txt') as f:
        list_id = f.readlines()
        list_stu_id = [stu_id.strip().split(',') for stu_id in list_id]#列表表达式 生成查询学号id的列表
        #print "*******************"
        #print "list_stu_id is", list_stu_id
        #print "*******************"
        #print "-------------------"
        #print "student ID is :", name
        #print "-------------------"
        #print "type: ", type(name),"type_: ", type(list_stu_id[0][2])
        for stu_info in list_stu_id:
            #print "name: ", str(name) ," stu_info :" ,stu_info, "stu[0] ", stu_info[0]
            if str(name) == stu_info[0]:
                return "name :", stu_info[0],"Faculty :",\
                stu_info[1],"rank :",stu_info[2], "prediction :", pre
            #else:
            #    return "not find"

'''
create Echarts file
下列参数都是通过学号查询相应文件查询出来的 格式为列表
'''
def create_echarts(gauge, funnel, bar_1, bar_2, pie, polar, prediction, whole):
    page = Page()
    
    #定义整体显示风格
    style = Style(
        title_top='#fff',               #标题颜色
        title_pos='center',             #标题位置: 中心
        width=1300,                     #定义宽度
        height=600)                     #定义高度
        #background_color='#404a59')    #背景颜色

    #显示欢迎图表 " Welcome "
    scatter = Scatter(**style.init_style)
    v1, v2 = scatter.draw("data/welcome.png")
    scatter.add("Welcome", v1, v2, is_random=True)
    page.add(scatter)
    
	#Radar plot
    charts = Radar("消费行为与日常习惯", **style.init_style)
    schema = [
('library', 0.6),
('hospital', 04),
('shower',  0.04),
('academic_office', 0.008),
('washer',  0.03),
('canteen', 0.6),
('market', 0.3),
('bus',  0.2),
('printing', 0.01),
('water', 0.5),
('other', 0.003),
('06_00enterDiv',  0.5),
('06_00exitDiv',  0.5),
('09_00exitDiv',  0.3),
('09_00enterDiv',  0.3),
('12_50exitDiv', 0.5),
('12_50enterDiv', 0.5),
('11_20exitDiv', 0.4),
('11_20enterDiv', 0.4),
('16_50exitDiv', 0.6),
('16_50enterDiv', 0.6),
('19_00exitDiv', 0.5),
('19_00enterDiv', 0.5),
('22_00exitDiv', 0.4),
('22_00enterDiv', 0.4)
]
    
    charts.config(schema, shape='circle')
    charts.add('', [whole], 
        is_splitline=True, 
        is_axisline_show=True, 
        is_random=True, 
        line_width=4,
        is_area_show=True,
        area_opacity=0.65,
        area_color='#b3e4a1',
        label_text_size=17)
    page.add(charts)

    '''
    charts = EffectScatter("Whole_info", **style.init_style)
    x = ['library',
 'hospital',
 'market',
 'water',
 'canteen',
 'washer',
 'other',
 'academic_office',
 'printing',
 'bus',
 'shower',
 '06_00exitDiv',
 '06_00enterDiv',
 '09_00exitDiv',
 '09_00enterDiv',
 '12_50exitDiv',
 '12_50enterDiv',
 '11_20exitDiv',
 '11_20enterDiv',
 '16_50exitDiv',
 '16_50enterDiv',
 '19_00exitDiv',
 '19_00enterDiv',
 '22_00exitDiv',
 '22_00enterDiv']
    x1 = range(0, len(whole[0]))
    charts.add("", x1, whole[0], 
        symbol_size=20, 
        effect_scale=3.5,
        effect_period=3, 
        symbol="arrow", 
        is_label_show=True)
    page.add(charts)
	'''

    #应用仪表盘 显示该学生在此学院的排名情况
    charts = Gauge("成绩排名", **style.init_style)
    charts.add("", "学院排名", gauge[0], scale_range=[0, gauge[1]], 
               is_legend_show=True,
               is_random=True)
    page.add(charts)
    
    #应用漏斗图 显示该学生消费方式的概况
    charts = Funnel("消费方式概况", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1], is_label_show=True, 
               label_pos='outside', legend_pos='left',
               legend_orient='vertical',
               label_text_size=17,
               is_random=True)
    page.add(charts)
    
    #应用饼图 显示该学生消费方式的占比情况
    charts = Pie("消费方式占比", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1],  is_random=True,
            radius=[15, 70], rosetype='radius', is_label_show=True, 
            legend_orient='vertical',
            legend_pos='left',
            label_text_size=17)
    page.add(charts)

    #应用条形图 显示该学生在该学年每项消费方式额度的情况
    charts = Bar("消费方式(额度)展示", "全年 2013.9.1~2014.8.31", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1], 
               is_label_show=True, 
               legend_pos='left',
               legend_orient='vertical',
               mark_point=["max"],
               is_random=True
               )
    page.add(charts)    
    
    #应用折线图 显示该学生在该学年每项消费方式额度的情况
    charts = Line("消费情况折线图", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1], 
             mark_point=["average", "max", "min"],
         #mark_point_textcolor='#171717',
         #line_color='#EE9A49',
         is_label_show=True, 
         legend_pos='left',
         line_width='3',
         line_type='solid',
         is_random=True,
         is_smooth=True,
         mark_line=["max", "average"],
         is_fill=True,
         area_color='#000',
         area_opacity=0.3)
    page.add(charts)
    
    #应用条形图(可伸缩, 可移动) 显示该学生该学年 每个月各项消费的总花费额
    attr = [month[0] for month in bar_1]
    values = [value[1] for value in bar_1]
    charts = Bar("学生每月消费水平", "每月", **style.init_style)
    charts.add("每月各项消费总和", attr, values, 
               mark_point_textcolor='#171717',
               is_label_show=True, 
               is_datazoom_show=True,
               datazoom_type='both',
               legend_pos='left',
               legend_orient='vertical',
               mark_point=["max", "min"],
               mark_line=["average"],
               is_random=True)
    page.add(charts)

    #套用时间线 应用条形图和折线图 综合显示该学生每月按照消费方式的消费情况
    timeline = Timeline(is_auto_play=True, timeline_bottom=0,width=1300,height=600)
    for month in bar_2:
        #title =  'month ' + str(month[0])
        overlap = Overlap()
        each_labels, each_values = change2.separate(month[1])
        #each_line = [value+10 for value in each_values]
        bar = Bar("每月消费方式", "花费额", **style.init_style)
        bar.add("月消费", each_labels, each_values, 
                is_label_show=True, 
                legend_pos='left',
                legend_orient='vertical',
                is_random=True
                )
        line = Line()
        line.add("", each_labels, each_values,
                 mark_point=["average", "max", "min"],
         mark_line=["average", "max"],
         line_width='3',
         line_type='dashed',
         is_random=True,
         is_smooth=True,
         mark_point_symbol='arrow', mark_point_symbolsize=60)
        overlap.add(bar)
        overlap.add(line)        
        '''
        timeline.add(bar, 'month'+str(month[0]))
        timeline.add(line, '')
        '''
        timeline.add(overlap, 'month'+str(month[0]))
    page.add(timeline)

    #应用极坐标图 显示该学生12个月里 进入图书馆次数的情况
    po = [i for i in polar[1]]          #列表表达式 生成月份
    pi = [j for j in polar[0]]          #列表表达式 生成次数
    charts = Polar("进入图书馆的次数","2013.9 ~ 2014.8", **style.init_style)
    charts.add("", po, radius_data=pi,
          type='barRadius', is_random=True)
    page.add(charts)

    #应用饼图 显示该学生所有阅读过的书籍信息
    charts = Pie("阅读过的书籍", **style.init_style)
    charts.add("", pie[0], pie[1], radius=[40, 75], label_text_color=None,
        is_label_show=True, legend_orient='vertical',is_legend_show=True,
        legend_pos='left',
        label_text_size=17)
    page.add(charts)   

    '''
    missing a prediction of grants
    缺失正确的概率 需要套用模型计算
    '''
    #应用流体图 显示该学生获得助学金的概率大小
    liquid = Liquid("获得助学金的概率", **style.init_style)
    liquid.add("", [prediction])
    page.add(liquid)        
    
    return page
'''
    charts = Pie("pie chart", "test pie")
    charts.add("pie data", attr, v1)
    page.add(charts)

    charts = Line("pie chart", "test pie")
    charts.add("pie data", attr, v1)
    page.add(charts)
'''
#create_charts().render()

if __name__ == "__main__":
    app.run()
