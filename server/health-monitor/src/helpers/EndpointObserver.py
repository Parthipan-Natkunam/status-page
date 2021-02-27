class Servers:
  __endpoints__ = []

  def __init__(self,observer):
    self.__observer__ = observer

  def changeObserver(self,observer):
    self.__observers__= observer

  def get_endpoints(self):
    return self.__endpoints__

  def add_endpoints(self,endpoints=[]):
    self.__endpoints__.extend(endpoints)
    self.__observer__.notify(self.__endpoints__)
  
  def reset_endpoints(self):
    self.__endpoints__ = []
    self.__observer__.notify(self.__endpoints__)

  def remove_endpoint(self,endpoint=""):
    if (endpoint in self.__endpoints__):
      self.__endpoints__ = [url for url in self.__endpoints__ if url is not endpoint]
      self.__observer__.notify(self.__endpoints__)

class Observer:
  def notify(self,endpoints):
    pass

