import http.client

def datetrans(datestr=''):
    year,month, day=datestr.split('-')
    month=('0'+month)[-2:]
    day=('0'+day)[-2:]
    return year+month+day

host='www.gvchina.com'
videourl='/gwebinardemo'
coursevideo='/jiangke.flv'
question='/tiwen.flv'
indexurl='/course.aspx?pageno=1'

conn=http.client.HTTPConnection(host)
conn.request('GET', indexurl)
r1=conn.getresponse()
a=r1.read().decode('utf-8')
courselist=dict()
for i in a.split('\r\n'):
    if i.find('clearfix i0') != -1:
        for j in i.strip().rstrip().split('</li>'):
            k=j.split('</div>')
            if k != ['']:
                coursename=k[0].split('"')[5]
                courseurl=k[0].split('"')[7]
                date=datetrans(k[2].split('>')[1])
                courselist[date]=(coursename, courseurl)
        break
    
for i in courselist.keys():
    print(i)

conn.request('GET', '/gwebinardemo/20151027/jiangke.flv')
r1=conn.getresponse()
print(r1.status, r1.reason)
print(r1.getheader('content-length'))

