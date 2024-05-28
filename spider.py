import requests
import re
import urllib.parse as urlparse


target_url = "http://192.168.202.87/mutillidae"
target_link = []



def extract_links_from(url):
   response = requests.get(url)
   href_links = re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))
   return href_links
def crawl(url):
    result = extract_links_from(url)
    print(result)
    for link in result:
        link = urlparse.urljoin(target_url,link)

        if "#" in link:
            link = link.split("#")[0]

        if link not in target_link:
            target_link.append(link)
            print(link)
            crawl(link)

crawl(target_url)





