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
	url = "https://medium.com/_/api/tags/"+request.args.get("tag")+"/stream?limit=15&sortBy=published-at"
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
	response = response.text
	response = response.replace('])}while(1);</x>','')
	response = json.loads(response)
	list1 = []
	for i in response["payload"]["references"]["Post"]:
		list1.append(i)
	list1 = json.dumps(list1)
	print(list1)
	return list1


@app.route('/data1')
@cross_origin()
def data1():
	url = "https://medium.com/_/api/tags/"+request.args.get("tag")+"/stream?limit=15&sortBy=published-at"
	print(url)
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
	response = response.text
	response = response.replace('])}while(1);</x>','')
	response = json.loads(response)
	i = request.args.get('i')
	data = {}
	j = response["payload"]["references"]["Post"][str(i)]
	data["article_id"] = j["id"]
	data["name1"] = response["payload"]["references"]["User"][j["creatorId"]]["name"]
	data["time"] = j["createdAt"]
	data["readingTime"] = j["virtuals"]["wordCount"]
	data["title"] = j["title"]
	data["slug"] = j["slug"] + "-" + j["id"]
	data["username"] = response["payload"]["references"]["User"][j["creatorId"]]["username"]

	data = json.dumps(data)
	print(data)
	return data

@app.route('/data')
@cross_origin()
def data():
	data = {}
	i = request.args.get("artid")
	j = request.args.get("uname")
	url = "https://medium.com/@"+j+"/" + i
	response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})

	tree = html.fromstring(response.content)
	data["name1"] = ''.join(tree.xpath('//div[@class="u-lineHeightTightest"]/a/text()'))
	data["article_id"] = ''.join(tree.xpath('//div/main/article/div/@data-post-id'))
	data["time"] = ''.join(tree.xpath('//time/text()'))
	data["readingTime"] = ''.join(tree.xpath('//span[@class="readingTime"]/@title'))
	data["title"] = ''.join(tree.xpath('//h1/text()'))
	if data["title"] == "":
		data["title"] = ''.join(tree.xpath('//h1/strong/text()'))

	data["arti"] = tree.xpath('//section/div[2]/div/p/text()')
	data["tags"] = tree.xpath('//div[@class="u-paddingBottom10"]/ul/li/a/text()')
	url = "https://medium.com/_/api/posts/" + data["article_id"] + "/responses?limit=25"
	response = requests.get(url)
	response = response.text
	response = response.replace('])}while(1);</x>','')
	response = json.loads(response)
	data["res"] = []
	for i in response["payload"]["value"]:
		data1 = {}
		url = "https://medium.com/_/api/users/" + i["creatorId"]
		res = requests.get(url)
		res = res.text
		res = res.replace('])}while(1);</x>','')
		res = json.loads(res)
		data1["name"] = res["payload"]["value"]["name"]
		data1["title"] = i["title"]
		data["res"].append(data1)
	data = json.dumps(data)
	print(data)
	return data

if __name__ == '__main__':
    app.run(debug=True)
