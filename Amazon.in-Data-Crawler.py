from bs4 import BeautifulSoup
from urllib import urlopen
import requests
import re

def count(url):
    id=url.split('=')[4]
    print id
    new_url="http://www.amazon.in/s?ie=UTF8&me="+id
    print new_url
    r = requests.get(new_url)
    t=r.content
    soup=BeautifulSoup(t)
    for section in soup.findAll('div',{'class':'s-first-column'}):
        y= section.findChildren()[0].renderContents()
        x=y.split('<')[0]
        a=x.replace(",","")
        y=re.findall(r'\b\d+\b',a)
        y=map(int,y)
        ss=max(y)
        s2=str(ss)
        fd = open('document.txt','a')
        fd.write(s2+"\n")
        fd.close()
        print "Collected"

def feedback(url):
    print "Collecting Feedback"
    alpha=url
    response = requests.get(url)
    prod = response.content
    soup=BeautifulSoup(prod)
    fd = open('document.txt','a')
    for section in soup.findAll('td',{'class':'feedback30Days'}):
        t= section.renderContents()
        x=t.replace(",","")
        y=x.replace(" ","")
        z=x.replace("\n","")
        a=z.replace(" ","")
        if (a[0]!="<"):
            f=a
        if (a[0]=="<"):
            id=a.split('<')[1]
            f=id.split('>')[1]     
        fd.write(f+",")
    for section in soup.findAll('td',{'class':'feedback90Days'}):
        t= section.renderContents()
        x=t.replace(",","")
        y=x.replace(" ","")
        z=x.replace("\n","")
        a=z.replace(" ","")
        if (a[0]!="<"):
            f=a
        if (a[0]=="<"):
            id=a.split('<')[1]
            f=id.split('>')[1]
        fd.write(f+",")
    for section in soup.findAll('td',{'class':'feedback365Days'}):
        t= section.renderContents()
        x=t.replace(",","")
        y=x.replace(" ","")
        z=x.replace("\n","")
        a=z.replace(" ","")
        if (a[0]!="<"):
            f=a
        if (a[0]=="<"):
            id=a.split('<')[1]
            f=id.split('>')[1]
        fd.write(f+",")
    for section in soup.findAll('td',{'class':'feedbackLifetime ie8hax'}):
        t= section.renderContents()
        x=t.replace(",","")
        y=x.replace(" ","")
        z=x.replace("\n","")
        a=z.replace(" ","")
        if (a[0]!="<"):
            f=a
        if (a[0]=="<"):
            id=a.split('<')[1]
            f=id.split('>')[1]
        fd.write(f+",")
    print "Collected"
    print "Collecting Product Count"
    fd.close()
    print alpha
    count(alpha)
        
       
def a(abc):
    response = requests.get(abc)
    prod = response.content
    soup=BeautifulSoup(prod)
    print "Collecting Offer Link" 
    for section in soup.findAll('span',{'class':'olp-padding-right'}):
        offer= section.findChildren()[0]
        offer_link=offer['href']
        offer_link="http://www.amazon.in"+offer_link
        print "Collected"  
    for section in soup.findAll('h1',{'class':'a-size-large a-spacing-none'}):
        name= section.findChildren()[0].renderContents()
        print "Collecting Product Name"
        fd = open('document.txt','a')
        fd.write("\n\n"+name+"\n\n")
        print name
        print "Collected"
        fd.close()
    response = requests.get(offer_link)
    html = response.content
    soup=BeautifulSoup(html)
    seller_link = ["" for x in range(50)]
    i=0
    for section in soup.findAll('p',{'class':'a-spacing-small'}):
        u=section.findChildren()[2]
        q="http://www.amazon.in"+u['href']
        seller_link[i]=q
        i=i+1
    i=0        
    for section in soup.findAll('h3',{'class':'a-spacing-none olpSellerName'}):
        seller= section.findChildren()[1].renderContents()    
        if seller=="":
            t=section.findChildren()[1]
            seller=t['alt']    
        print "For the seller "+seller+":"
        fd = open('document.txt','a')
        fd.write(seller+",")
        fd.close()
        feedback(seller_link[i])
        i=i+1

pr=open('input.txt','r')
t=pr.read()
for line in t.splitlines():
    a(line)
    
    
        
            
             
   
    
             
    
     
    


     
     
     
