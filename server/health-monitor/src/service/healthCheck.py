import threading
import time
import requests
from .context import helpers

class HealthCheck(helpers.Observer):
  __endpoints = []
  __tmpList = []
  __thread_lock = threading.Lock()
  __locked_resource_retry_count = 0
  __exponential_backoff_base = 20

  def poll(self,interval):
    while True:
      self.__thread_lock.acquire()
      urls = self.__endpoints
      self.__thread_lock.release()
      print("polling...")
      for url in urls:
        try:
          req = requests.get(url)
          if(req.status_code == 200):
            print(url+ " : 1\n")
            continue
          raise Exception()
        except:
          print(url+ " : 0\n")
      time.sleep(interval)

  def notify(self,endpoints):
    self.__tmpList = endpoints
    if(self.__thread_lock.locked()):
     if(self.__locked_resource_retry_count<4):
       self.__locked_resource_retry_count += 1
       self.notify(self.__tmpList)
       time.sleep(self.__exponential_backoff_base*self.__locked_resource_retry_count)
     return
    self.__locked_resource_retry_count = 0
    self.__endpoints = self.__tmpList
    self.__tmpList = []

  def start_polling(self):
    polling_thread = threading.Thread(target=self.__poll__, args=(10,),daemon=True)
    polling_thread.start()
    # polling_thread.join()