import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'VisitorCounter'))

import visitor  

for _ in range(3):
    result = visitor.main(None)
    print(result.get_body().decode())
