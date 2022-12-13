import queue

# 创建一个队列，容量10
Q = queue.Queue(10)
# print(Q)
# print(type(Q))
# 基本方法
# print(Q.queue) # 查看队列中所有元素
# print(Q.qsize()) # 返回队列的大小
# print(Q.empty()) # 判断队空
# print(Q.full()) # 判断队满

# 将对象放入队列中
for i in range(10):
    # 阻塞调用抛异常 block=Fales，timeout=None 无等待时间
    Q.put(i, block=False, timeout=None)
    # Q.put_nowait(i) # 相当于 put(item,Fales)

while not Q.empty():
    # while 1:
    # print(Q.get())
    print(Q.get_nowait())  # 相当于 get(False)，如果没有数据抛异常

# 等待排队的方法
Q.task_done()  # 在完成一项工作后，向任务已完成的队列发送一个信号
Q.join()  # 阻止知道队列的所有项目都被获取并处理，即等到队列为空再执行别的操作
