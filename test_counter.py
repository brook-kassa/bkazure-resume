import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'VisitorCounter'))

import __init__ as function_code  

for _ in range(3):
    response = function_code.main(None)
    print(response.get_body().decode())
