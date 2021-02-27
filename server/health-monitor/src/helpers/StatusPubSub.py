class StatusPubSub:
  __instance = None
  __recent_data = {}

  def __init__(self):
    if StatusPubSub.__instance != None:
      raise Exception("An instance of StatusPubSub already exists")
    else:
      StatusPubSub.__instance = self

  def get_instance():
    if StatusPubSub.__instance == None:
      StatusPubSub()
    return StatusPubSub.__instance
  
  def publish(self,data):
    self.__recent_data = data

  def subscribe(self):
    return self.__recent_data

    