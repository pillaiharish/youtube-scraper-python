from bs4 import BeautifulSoup
import requests
import argparse

# url =  "https://w3schools.com/python/demopage.htm"
# url =  "https://boston.craigslist.org/search/sof#search=1~thumb~0~0"




parser = argparse.ArgumentParser(description='Enter URL for scraping')
parser.add_argument('--url', metavar='--url', type=str, 
                    help='URL with http or https')
args = parser.parse_args()

if args.url:
    url = args.url
else:
    url = "https://www.youtube.com"

res = requests.get(url).text
# print(res)
soup = BeautifulSoup(res , 'html.parser')

arr =[]
for i in soup:
    arr.append(i)
with open("data.txt","w+") as file:
    for i in soup:
        file.write(str(i))
    file.close()
# print(soup.prettify())
list_urls = soup.find_all("a")
job_urls=[]
for list_url in list_urls:
    # print(list_url.get("href"))
    if "job-detail" in list_url.get("href"):
        # print(list_url.get("href").text)
        job_urls.append(list_url.get("href"))
# list_titles = soup.find_all("title")
# for list_title in list_urls:
#     print(list_title)

# print(job_urls)
print(len(job_urls))

list_title = soup.find_all("li",{"class":"clearfix joblistli"})
