import threading

from one import bot1
from two import bot2


p1 = bot1.polling
p2 = bot2.polling


non_stop = {"non_stop": True}


th1 = threading.Thread(target=p1, args=non_stop)
th2 = threading.Thread(target=p2, args=non_stop)


th1.start()

th2.start()
