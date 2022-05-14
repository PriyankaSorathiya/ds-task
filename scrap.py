import requests
import bs4
import pandas as pd
import urllib
import json

URL = 'https://en.wikipedia.org/wiki/Google_Meet'
# Fetch all the HTML source from the url
response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.select('a')
result1 = {}
for link in links:
    # print(link.get_text())
    result1['Name'] =link.get_text()
    text = []
    base_url = link.get('href')
    if link.get('href') != None:
        if 'https://' in link.get('href'):
            continue
        else:
            # Convert relative URL to absolute URL
            base_url2 = f"https://en.wikipedia.org/{base_url}"
            result1['base_url'] = base_url2
            soup2 = bs4.BeautifulSoup(response.text, 'html.parser')
            for paragraph2 in soup2.find_all('p'):
                text.append(paragraph2.text)
                result1['text'] = text
        print(result1)
    # jsonfile = json.dumps(result1)
    # # print(type(jsonfile))
    # with open('app.json','a',encoding='utf-8') as fp:
    #   # json.dump(result1,fp,ensure_ascii=False,indent=4,skipkeys=True)
    #   fp.write(jsonfile)
else:
    print("none")

print("DONE")