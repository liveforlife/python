import requests
from bs4 import BeautifulSoup

def getWebContent(url,data = None):
  header = {
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
    'Connection': 'Keep-Alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
  }
  rep = requests.get(url,headers = header)
  rep.Encoding = 'utf-8'
  return rep.text

def getData(html_text):
  res =[]
  bs = BeautifulSoup(html_text,"html.parser")
  body = bs.body
  # data = body.find_all("ul","nav-content")
  data = body.find("ul",{"class":"nav-content"})
  lis= data.find_all("li")

  for a in lis:
    aStr = a.find("a")
    res.append(aStr.string)
  
  return res

if __name__ == '__main__':
  url='http://www.youkawallet.com/'
  html = getWebContent(url)
  result = getData(html)
  print(result,'result')