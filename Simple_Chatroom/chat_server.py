import tornado.ioloop
import tornado.web
import tornado.websocket

class ChatWebSocketHandler(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        self.connections.add(self)

    def on_message(self, message):
        for conn in self.connections:
            conn.write_message(message)

    def on_close(self):
        self.connections.remove(self)

    def check_origin(self, origin):
        return True

def make_app():
    return tornado.web.Application([
        (r"/websocket", ChatWebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Chat server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
