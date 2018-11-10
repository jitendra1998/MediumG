

import requests
from lxml import html

url = 'https://medium.com/tag/india/latest'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})

tree = html.fromstring(response.content)

name = tree.xpath('//div[@class="js-tagStream"]/div/div/div/div[3]/a/@href')
name = ["https://medium.com/@jacksoncunningham/digital-exile-how-i-got-banned-for-life-from-airbnb-615434c6eeba"]
for i in name:

	response = requests.get(i, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
	tree = html.fromstring(response.content)
	name1 = ''.join(tree.xpath('//div[@class="u-lineHeightTightest"]/a/text()'))
	article_id = ''.join(tree.xpath('//div/main/article/div/@data-post-id'))
	print(article_id)
	time = ''.join(tree.xpath('//time/text()'))
	readingTime = ''.join(tree.xpath('//span[@class="readingTime"]/@title'))
	title = ''.join(tree.xpath('//h1/text()'))
	if title == "":
		title = ''.join(tree.xpath('//h1/strong/text()'))

	article = tree.xpath('//section/div[2]/div/p/text()')
	tags = tree.xpath('//div[@class="u-paddingBottom10"]/ul/li/a/text()')
	url = "https://medium.com/_/api/posts/" + article_id + "/responses?limit=250"
	response = requests.get(url)
	