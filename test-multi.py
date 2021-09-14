# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import re
import os

plocalpath= 'test-aaa'
phead='com.sss:'
pData={'aaa-api',
'aaa-bill',
'aaa-channel',
'aaa-clearing',
'aaa-common',
'aaa-job',
'aaa-mq',
'aaa-rest',
'aaa-user'}
#http://10.77.32.78:9000/api/measures/component_tree?ps=100&s=qualifier%2Cname&baseComponentKey=tf56%3AuserCenter-rest&metricKeys=ncloc%2Ccode_smells%2Cbugs%2Cvulnerabilities%2Ccoverage%2Cduplicated_lines_density%2Calert_status&strategy=children
def printOutCode(xpath,filename,url):
    if not os.path.exists(xpath):
        os.makedirs(xpath)
    print(url)
    data = urlopen(url).read().decode('utf-8')
    res = json.loads(data)
    code = ""
    for codeline in res['sources']:
        code = code + codeline['code'] + '\r'
    xcode = re.sub(r'<\/?span.*?>', "", code)
    f = open(xpath + filename, "wb")
    f.write(xcode.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').encode('utf-8'))
    f.close()
for p in pData:
    pUrl = "http://10.77.32.78:9000/api/measures/component_tree?ps=200&s=qualifier%2Cname&baseComponentKey="+phead+p+"&metricKeys=ncloc%2Ccode_smells%2Cbugs%2Cvulnerabilities%2Ccoverage%2Cduplicated_lines_density%2Calert_status&strategy=children";
    jsondata = urlopen(pUrl).read().decode('utf-8')
    pres = json.loads(jsondata)
    wData = pres['components']
    for dw in wData:
        if dw['path'] == 'pom.xml' or dw['path'] == '/':
            pompath="D:/JobProjects/_LEARN/" + plocalpath + "/" + p + "/"
            pomUrl = "http://10.77.32.78:9000/api/sources/lines?key="+phead+p + ':pom.xml'
            printOutCode(pompath,'pom.xml',pomUrl)
            continue
        currentUrl = "http://10.77.32.78:9000/api/measures/component_tree?ps=200&s=qualifier,name&baseComponentKey="+phead+p+":"+dw['path']+"&metricKeys=ncloc,code_smells,bugs,vulnerabilities,coverage,duplicated_lines_density,alert_status&strategy=children"
        data = urlopen(currentUrl).read().decode('utf-8')
        res=json.loads(data)
        coss=res['components']
        for cos in coss :
            #print(cos['name'])
            print(cos['path'])
            #print(cos['key'])
            finalUrl="http://10.77.32.78:9000/api/sources/lines?key="+cos['key']
            #print(xcode)
            xpath = "D:/JobProjects/_LEARN/" + plocalpath + "/" + p + "/" + re.match(r'sr.*\/', cos['path']).group()
            filename=cos['name']
            printOutCode(xpath,filename,finalUrl)




