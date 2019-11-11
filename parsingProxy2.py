from lxml.html import fromstring
from bs4 import BeautifulSoup as b
import urllib.request as urllib
import numpy as np

array_define = ['1','2','3','4','5','6','7','8','9','0','.',':']

def get_proxies():
    site = 'https://free-proxy-list.net/'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(site,headers=hdr) #sending requests with headers
    url = urllib.urlopen(req).read() #opening and reading the source code
    html = b(url,"lxml")                #structuring the source code in proper format
    rows = html.findAll("tr")       #finding all rows in the table if any.
    proxies = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        try:
            ipaddr = cols[0]        #ipAddress which presents in the first element of cols list
            portNum = cols[1]       #portNum which presents in the second element of cols list
            proxy = ipaddr+":"+portNum  #concatinating both ip and port
            portName = cols[6]          #portName variable result will be yes / No

            if portName == "no":
                pass # proxies.append(str(proxy)) #if yes then it appends the proxy with https
            else:


                proxies.append(str(proxy)) #if no then it appends the proxy with http
        except:
            pass
    return proxies

###################################################

def sort_proxy():
    print('Number of proxies:',len(get_proxies()))
    # print(get_proxies())

    proxies = get_proxies()
    to_del = []
    for n in range(len(proxies)):
        prov = 0

        for i in range(len(proxies[n])):

            if proxies[n][i]== '.' :
                prov +=1

        if(prov==0):
            # proxies.pop(n)
            to_del.append(n)
    # print(to_del)

    for n in reversed(to_del):
        proxies.pop(n)


    return proxies

def search():
    proxies = sort_proxy()
    proxies_to =[]
    for ip in proxies:

        ip= 'http://'+ip

        proxies_to.append(ip)
    return proxies_to
