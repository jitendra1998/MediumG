from flask import Flask, request
import requests
from lxml import html
import json

from flask_cors import CORS, cross_origin


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/')
@cross_origin()
def index():
	url = 'https://medium.com/tag/'+ request.args.get("tag") + '/latest'
	list1 = []
	print(url)
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
	tree = html.fromstring(response.content)
	name = tree.xpath('//div[@class="js-tagStream"]/div/div/div/div[3]/a/@href')
	print(request.args.get("tag"))
	for i in name:
		data = {}
		response = requests.get(i, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
		tree = html.fromstring(response.content)
		data["name1"] = ''.join(tree.xpath('//div[@class="u-lineHeightTightest"]/a/text()'))
		data["article_id"] = ''.join(tree.xpath('//div/main/article/div/@data-post-id'))
		data["time"] = ''.join(tree.xpath('//time/text()'))
		data["readingTime"] = ''.join(tree.xpath('//span[@class="readingTime"]/@title'))
		data["title"] = ''.join(tree.xpath('//h1/text()'))
		if data["title"] == "":
			data["title"] = ''.join(tree.xpath('//h1/strong/text()'))

		data["article"] = tree.xpath('//section/div[2]/div/p/text()')
		data["tags"] = tree.xpath('//div[@class="u-paddingBottom10"]/ul/li/a/text()')
		list1.append(data)
	list1 = json.dumps(list1)
	print(list1)
	return list1
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')