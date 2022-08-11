import requests
from bs4 import BeautifulSoup
import webbrowser
file1 = open("data.dat","r+")
title = ""
a = file1.read()
i = int(a)


while(True):
    print(str(i) + " deneniyor...")
    Link = 'https://dizipal'+str(i)+'.com'
    try:
        site = requests.get(Link)
        siteIcerigi = BeautifulSoup(site.text,"html.parser")
        for title in siteIcerigi.find_all('title'):
            title = title.get_text()
        if(title=="DiziPAL - dizi, film ve anime izle"):
            break
        else:
            i=i+1    
    except:
        i+=1  
print("Bulundu!! " + str(i))
webbrowser.open(Link, new=2)
file1.truncate(0)
file1.seek(0)
file1.write(str(i))
file1.close()        


