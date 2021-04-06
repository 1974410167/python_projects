import time
def fbis(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-1]+result[-2])
    return result
def main():
    result=fbis(10)
    fobj=open("result.txt","w+")
    for i,num in enumerate(result):
        print("{0}-  {1}".format(i,num))
        fobj.write("%d"%num)
        time.sleep(1)
if __name__=="__main__":
    main()










