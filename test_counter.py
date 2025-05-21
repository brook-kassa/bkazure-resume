import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'VisitorsCounter'))

import visitor

class DummyResponse:
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code

    def get_body(self):
        return self.text.encode()

def main():
    for i in range(3):
        response = visitor.main(None)
        print(response.get_body().decode())

if __name__ == "__main__":
    main()
