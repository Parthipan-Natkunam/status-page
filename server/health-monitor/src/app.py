import threading
from flask import Flask, request, abort
from service import HealthCheck
from helpers import Servers


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

if __name__ == '__main__':
    app.run()
   
    
