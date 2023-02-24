from flask import Flask,render_template,request,jsonify
from bs4 import BeautifulSoup as bs
from flask_cors import cross_origin,CORS
import requests
from urllib.request import urlopen as uReq


# app = Flask(__name__)

# @app.route("/",methods=['GET'])
# def ip_request():
#     if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
#         return(request.environ['REMOTE_ADDR'])
#     else:
#         return(request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy

# if __name__ == "__main__":
#     app.run(debug=True,host="0.0.0.0",port=5010)


def search_url(search_keywords,website=None):
    if website == None:
        website = "www.flipkart.com"
    website_url = f"https://{website}/"
    website_url_search = website_url + "search?q=" + search_keywords
    print(website_url_search)
    url_client = uReq(website_url_search)
    url_page_source = url_client.read()
    url_client.close()
    url_html = bs(url_page_source,'html.parser')
    # print(url_html)
    big_boxes = url_html.find_all("div",{'class':'col-12-12'})
    print(len(big_boxes)) # length is 33
    # big boxes starts from 8
    # print(big_boxes[6].find_all('a', 'href'))
    first_page_sub_urls = []
    for box in url_html.find_all("div",{'class':'col-12-12'}):
        for b in box.find_all("a"):
            first_page_sub_urls.append(b.get('href'))

    for i in range(len(first_page_sub_urls)):
        first_page_sub_urls[i] = "https://www.flipkart.com" + first_page_sub_urls[i]
    
    # print(first_page_sub_urls)
    print(requests.get(first_page_sub_urls[8]).text)
    
search_url("iphone11")
