import tornado
import requests, json
from tornado import websocket, web, ioloop
clients = [] 

#whenever you want to broadcast to all connected call this function
def broadcast_message(msg):
    global clients 
    for client in clients:
        client.write_message(msg)


class Handler(tornado.web.RequestHandler):
    def check_origin(self, origin):
        return True


    def get(self):
        #self.write
        tag = self.get_argument('tag', True)
        url = "https://medium.com/_/api/tags/"+tag+"/stream?limit=10&sortBy=published-at"
        print(url)
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
        response = response.text
        response = response.replace('])}while(1);</x>','')
        response = json.loads(response)
        #print(response)
        for i in response["payload"]["references"]["Post"]:
            data = {}
            j = response["payload"]["references"]["Post"][str(i)]
            data["article_id"] = j["id"]
            data["name1"] = response["payload"]["references"]["User"][j["creatorId"]]["name"]
            data["time"] = j["createdAt"]
            data["readingTime"] = j["virtuals"]["wordCount"]
            data["title"] = j["title"]
            data = json.dumps(data)
            print(data)

            broadcast_message(data)
        #we don't need self.finish() because self.render() is fallowed by self.finish() inside tornado
        #self.finish()


class WSHandler(websocket.WebSocketHandler):
    #crossdomain connections allowed
    def check_origin(self, origin):
        return True
    #when websocket connection is opened
    def open(self):
       #here you can add clients to your client list if you want
        clients.append(self)
        print("Client connected ")

    def on_close(self):
        clients.remove(self)
        print("Client disconnected")

    def on_message(self,message):
        print(message)
        self.write_message(message)

app = tornado.web.Application([
    (r'/', Handler),
    (r'/ws', WSHandler),
])


if __name__ == '__main__':
    app.listen(5000) #listen on what port
    ioloop.IOLoop.instance().start()
