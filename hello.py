import web  
          
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

                #create Echarts file func
                
                return getid(data['id'])
            elif data['bt_type'] == "bt2":
                return open(r'render.html').read()

'''
find student's info from id.csv
'''
def getid(name):
    with open('/home/bob/Desktop/web/result.csv') as f:
        list_id = f.readlines()
        list_stu_id = [stu_id.strip().split(',') for stu_id in list_id]
        print "*******************"
        print "list_stu_id is", list_stu_id
        print "*******************"
        print "-------------------"
        print "student ID is :", name
        print "-------------------"

        #print "type: ", type(name),"type_: ", type(list_stu_id[0][2])

        for stu_info in list_stu_id:
            print "name: ", str(name) ," stu_info :" ,stu_info, "stu[0] ", stu_info[0]
            if str(name) == stu_info[0]:
                return "name :", stu_info[0],"Faculty :",stu_info[1],"rank :",stu_info[2] 
            #else:
            #    return "not find"

'''
get data with ID
'''
#def get_data(stu_id):


'''
create Echarts file

def create_echarts():
    page = Page()

    charts = Bar("Bar chart", "precipitation and evaporation one year")
    charts.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    page.add(charts)

    charts = Pie("pie chart", "test pie")
    charts.add("pie data", attr, v1)
    page.add(charts)

    

    charts = Line("pie chart", "test pie")
    charts.add("pie data", attr, v1)
    page.add(charts)
    return page
#create_charts().render()
'''

if __name__ == "__main__":
    app.run()
