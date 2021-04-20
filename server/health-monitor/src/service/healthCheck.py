import threading
import time
import requests
from .context import helpers

class HealthCheck(helpers.Observer):
  __endpoints = []
  __tmpList = []
  __status_dict = {}
  __thread_lock = threading.Lock()
  __locked_resource_retry_count = 0
  __exponential_backoff_base = 20
  __pub_sub = helpers.StatusPubSub.get_instance()

  def poll(self,interval):
    while True:
      self.__thread_lock.acquire()
      urls = set(map( lambda urlData: urlData["url"],self.__endpoints))
      self.__thread_lock.release()
      print("polling...")
      for url in urls:
        try:
          req = requests.get(url)
          if(req.status_code == 200):
            self.__status_dict[url] = "Available"
            continue
          raise Exception()
        except:
          self.__status_dict[url] = "Unavailable"
      self.__pub_sub.publish(self.__status_dict)
      time.sleep(interval)
  
  def notify(self,endpoints):
    self.__tmpList = endpoints
    if(self.__thread_lock.locked()):
     if(self.__locked_resource_retry_count<3):
       self.__locked_resource_retry_count += 1
       self.notify(self.__tmpList)
       time.sleep(self.__exponential_backoff_base*self.__locked_resource_retry_count)
     return
    self.__locked_resource_retry_count = 0
    self.__endpoints = self.__tmpList
    self.__tmpList = []
