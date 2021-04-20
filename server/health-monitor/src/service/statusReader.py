import time

class StatusReader:
  def stream_data(self,status_source):
    while True:
      current_status = status_source.subscribe()
      yield "data: {data}\n\n".format(data=current_status)
      time.sleep(2)