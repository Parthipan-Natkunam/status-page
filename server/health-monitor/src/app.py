import threading
import time
from flask import Flask, request, abort, Response
from service import HealthCheck, StatusReader
from helpers import Servers, StatusPubSub


app = Flask(__name__)


@app.route('/')
def root_handler():
    return "Flask Server Online"

@app.route('/initMonitoring',methods=["POST"])
def init_server_monitoring():
    payload = request.get_json()
    if payload is not None:
        endpoints = payload["endpoints"]
        if endpoints and len(endpoints) > 0:
            healthCheckService = HealthCheck()
            servers = Servers(healthCheckService)
            servers.add_endpoints(endpoints)
            polling_thread = threading.Thread(target=healthCheckService.poll, args=(10,),daemon=True)
            polling_thread.start()
            return "success",201
    abort(400)

@app.route('/getStatus',methods=["GET"])
def get_status_stream():
    status_source = StatusPubSub.get_instance()
    statusReader = StatusReader()
    return Response(statusReader.stream_data(status_source), mimetype='text/event-stream', headers={"Access-Control-Allow-Origin": "http://127.0.0.1:5500","Access-Control-Allow-Credentials": "true"})

if __name__ == '__main__':
    app.run()

   
    
