import time

class StatusReader:
  def stream_data(self,status_source):
    while True:
      current_status = status_source.subscribe()
      yield "event: {event}\ndata: {data}\n\n".format(data=current_status, event="serverStatus")
      time.sleep(2)