import requests

def search():
    proxy_page='https://www.ip-adress.com/proxy-list'
    res=requests.get(proxy_page)
    res=res.text
    x=res.find('<table')
    y=res.find('</table>')
    res=res[x:y]

    list_ip=[]
    for i in range(len(res)-29):
        if res[i:i+29]=='title="More information about':
            x=res.find('>',i+29)
            y=res.find('<',x)
            z=res.find('<',y+3)
            list_ip.append('http://'+res[x+1:y]+res[y+4:z])
    return list_ip
