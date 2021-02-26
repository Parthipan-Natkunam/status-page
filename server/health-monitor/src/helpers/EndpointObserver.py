class Servers:
  __endpoints__ = []

  def get_endpoints(self):
    return self.__endpoints__

  def set_endpoints(self,endpoints=[]):
    self.__endpoints__.extend(endpoints)
  
  def reset_endpoints(self):
    self.__endpoints__ = []

  def remove_endpoint(self,endpoint=""):
    if (endpoint in self.__endpoints__):
      self.__endpoints__ = [url for url in self.__endpoints__ if url is not endpoint]

