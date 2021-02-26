# import logging
from flask import Flask
from helpers import Servers


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=format, level=logging.INFO,
    #                     datefmt="%H:%M:%S")
    # service_polling_thread = threading.Thread(target=check_service_health, args=(), daemon=True)
    # service_polling_thread.start()
    # app.run()
    servers = Servers()
    print(servers.get_endpoints())
    servers.set_endpoints(["123","456","789"])
    print(servers.get_endpoints())
    servers.remove_endpoint("456")
    print(servers.get_endpoints())
    servers.reset_endpoints()
    print(servers.get_endpoints())
