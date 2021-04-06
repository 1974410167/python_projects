import threading
import time
import asyncio


time1 = time.time()

t = 1
async def fun1():
    global t
    print(f"start {t} {time.time()-time1} ")
    await asyncio.sleep(1)
    print(f"end  {t} {time.time()-time1}")
    t += 1

async def main():
    m = 10
    event_loop = asyncio.get_event_loop()
    while m:
        task = event_loop.create_task(fun1())
        result = event_loop.run_until_complete(task)
        print(result)
        m-=1



# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
# asyncio.run(display_date())






# def s():
#     # 线程开始时间
#     print(f"start {time.time()-time1} ")
#     # 线程睡眠三秒，模拟网络等待
#     time.sleep(3)
#     # 线程结束时间
#     print(f"end {time.time()-time1}")
#
# # 创建三个线程
# for i in range(3):
#
#     # 传入函数名，函数参数
#     therad = threading.Thread(target=s,args=())
#     # 非阻塞启动线程
#     therad.start()



