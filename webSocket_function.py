from websocket import create_connection
import websocket


class WebSocket(object):

    def __init__(self, url):
        self.url = url
        self.request = None
        self.ws = None

    def on_message(self, ws, message):
        print(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("链接断开")

    def on_open(self, ws):
        self.request = input(">>")
        ws.send(self.request)

    def webSocketConnect(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.url, on_message=self.on_message, on_error=self.on_error,
                                         on_close=self.on_close)

        while True:
            self.ws.on_open = self.on_open

            self.ws.run_forever(ping_timeout=30)


if __name__ == '__main__':
    url = "ws://test.iot.bsphpro.com/aihm/ws/nettyPush"
    request1 = '{"sendType":"registerChannel","iotUserId":"8121606254596784128","machineCode":"cda85993111"}'
    request2 = '{"sendType":"heartBeat","iotUserId":"8121606254596784128","machineCode":"cda85993111"}'

    wst = WebSocket(url)
    wst.webSocketConnect()
    # print(wst.ws.send(request2))
    # ws
