import sys
from types import SimpleNamespace
from VisitorCounter import main

class MockHttpRequest:
    def __init__(self):
        self.method = "GET"
        self.params = {}
        self.headers = {}
        self.route_params = {}
        self.body = None

    def get_json(self):
        return {}

req = MockHttpRequest()

for i in range(3):
    response = main(req)
    print(response.get_body().decode())
