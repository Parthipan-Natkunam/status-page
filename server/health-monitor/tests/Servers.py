import unittest
from context import src

class ServersTest(unittest.TestCase):
  __servers = src.Servers()  

  def test_initial_endpoints(self):
    self.assertEqual(self.__servers.get_endpoints(),[])
  
  def test_set_endpoints(self):
    endpoints = ["http://myserver.com","http://yourserver.io"]
    self.__servers.set_endpoints(endpoints)
    self.assertEqual(self.__servers.get_endpoints(),endpoints)

if __name__ == "__main__":
  unittest.main()
