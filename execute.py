import threading
import maths
def main_task():
    x=2
    y=2
    t1=threading.Thread(target=maths.add,args=(x,y))
    t2=threading.Thread(target=maths.sub,args=(x,y))
    t3=threading.Thread(target=maths.mul,args=(x,y))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print("Task Completed Successfully")
main_task()
