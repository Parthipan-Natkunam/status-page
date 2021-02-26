import threading
import time
import requests

class HealthCheck:
  def __init__(self):
    self.endpoints = []

  def __poll():

  def endpoints(self):
    return self.endpoints

  def endpoints(self,endpointsList):
    self.endpoints.extend(endpointsList)

  def poll_endpoints():
    while True:
      try:
        req = requests.get("http://127.0.0.1:4567/ping")
        logging.info(req.status_code)
      except:
        logging.info("ping Failed")
      time.sleep(60)