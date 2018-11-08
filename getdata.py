

import requests
from lxml import html

url = 'https://medium.com/tag/india/latest'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
tree = html.fromstring(response.content)

name = tree.xpath('//div[@class="js-tagStream"]/div/div/div/div[3]/a/@href')
print(name)