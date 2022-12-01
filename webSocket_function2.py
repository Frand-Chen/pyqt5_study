import asyncio
import websockets


async def init_sma_ws():
    uri = "ws://test.iot.bsphpro.com/aihm/ws/nettyPush"
    async with websockets.connect(uri) as websocket:
        while True:
            name = input("What's your name? ")
            if name == 'exit':
                break

            await websocket.send(name)
            print('Response:', await websocket.recv())


asyncio.run(init_sma_ws())


if __name__ == '__main__':
    url = "ws://test.iot.bsphpro.com/aihm/ws/nettyPush"
    request1 = '{"sendType":"registerChannel","iotUserId":"8168759234751299584","machineCode":"cda85993"}'
    request2 = '{"sendType":"deviceSubscription","iotUserId":"8121606254596784128","machineCode":"cda8599332","productKey":"a166RICfGAA","deviceName":"KYXB-0102202211180002"}'
    wst = init_sma_ws()

