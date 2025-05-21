import sys
import os

# Add VisitorsCounter directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'VisitorsCounter'))

import visitor
from azure.functions import HttpRequest

def create_dummy_request():
    return HttpRequest(
        method='GET',
        url='/',
        headers={},
        params={},
        body=None
    )

def main():
    for i in range(3):
        req = create_dummy_request()
        response = visitor.main(req)
        print(response.get_body().decode())

if __name__ == "__main__":
    main()
