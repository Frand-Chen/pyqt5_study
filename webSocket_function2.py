import asyncio
import websockets

uri = "ws://test.iot.bsphpro.com/aihm/ws/nettyPush"
# websocket = websockets.connect(uri)

async def init_sma_ws():
    async with websockets.connect(uri) as websocket:
        while True:
            name = input("信息：")
            if name == 'exit':
                break
            await websocket.send(name)

        print('Response:', await websocket.recv())


asyncio.run(init_sma_ws())


if __name__ == '__main__':
    url = "ws://test.iot.bsphpro.com/aihm/ws/nettyPush"
    request1 = '{"sendType":"registerChannel","iotUserId":"8121606254596784128","machineCode":"cda85993111"}'
    request2 = \
'{"sendType":"deviceSubscription","iotUserId":"8121606254596784128","machineCode":"cda85993111","productKey":"a166RICfGAA","deviceName":"KYXB-0102202211180002"}'

    request3 = '{"sendType":"heartBeat","iotUserId":"8121606254596784128","machineCode":"cda85993111"}'
    wst = init_sma_ws()

