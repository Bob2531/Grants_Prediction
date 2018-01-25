# -*- coding: utf-8 -*-
import web  
import sys
sys.path.append(r'get_data/')
import score, card, change2, borrow, library, probability
from pyecharts import Page, Timeline, Style, Overlap, Scatter, Gauge, \
                      Funnel, Bar, Line, Pie, Polar, Liquid

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
                guage = score.get_score_data(stu_id)
                funnel = card.all_month(stu_id)
                bar_12month = card.month_sum(stu_id)
                bar_eachmonth = card.each_month(stu_id)
                pie = borrow.bookname(stu_id)
                polar = library.librarytime(stu_id)
                prediction = probability.prediction(stu_id)
                print "------------------"
                print guage ,funnel, bar_12month, bar_eachmonth, pie, polar, prediction
                print "------------------"
                #create Echarts file func
                create_echarts(guage, 
                               funnel, 
                               bar_12month,
                               bar_eachmonth,
                               pie,
                               polar,
                               prediction).render()

                return getid(stu_id, prediction)
            elif data['bt_type'] == "bt2":
                return open(r'render.html').read()

'''
find student's info from id.csv
'''
def getid(name, pre):
    with open('result.csv') as f:
        list_id = f.readlines()
        list_stu_id = [stu_id.strip().split(',') for stu_id in list_id]
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
'''
def create_echarts(gauge, funnel, bar_1, bar_2, pie, polar, prediction):
    page = Page()
    
    style = Style(
        title_top='#fff',
        title_pos='center',
        width=1300,
        height=600)
        #background_color='#404a59')    

    scatter = Scatter(**style.init_style)
    v1, v2 = scatter.draw("data/welcome.png")
    scatter.add("Welcome", v1, v2, is_random=True)
    page.add(scatter)
    
    charts = Gauge("成绩排名", **style.init_style)
    charts.add("", "学院排名", gauge[0], scale_range=[0, gauge[1]], 
               is_legend_show=True,
               is_random=True)
    page.add(charts)
    
    charts = Funnel("消费方式概况", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1], is_label_show=True, 
               label_pos='outside', legend_pos='left',
               legend_orient='vertical',
               is_random=True)
    page.add(charts)
    
    charts = Pie("消费方式占比", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1],  is_random=True,
            radius=[15, 70], rosetype='radius', is_label_show=True, 
            legend_orient='vertical',
            legend_pos='left',
            label_text_size=17)
    page.add(charts)

    charts = Bar("消费方式(额度)展示", "全年 2013.9.1~2014.8.31", **style.init_style)
    charts.add("消费方式", funnel[0], funnel[1], 
               is_label_show=True, 
               legend_pos='left',
               legend_orient='vertical',
               mark_point=["max"],
               is_random=True
               )
    page.add(charts)    
    
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

    po = [i for i in polar[1]]
    pi = [j for j in polar[0]]
    charts = Polar("进入图书馆的次数","2013.9 ~ 2014.8", **style.init_style)
    charts.add("", po, radius_data=pi,
          type='barRadius', is_random=True)
    page.add(charts)

    charts = Pie("阅读过的书籍", **style.init_style)
    charts.add("", pie[0], pie[1], radius=[40, 75], label_text_color=None,
        is_label_show=True, legend_orient='vertical',is_legend_show=True,
        legend_pos='left',
        label_text_size=17)
    page.add(charts)   

    '''
    missing a prediction of grants
    '''
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
