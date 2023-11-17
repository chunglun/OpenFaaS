#from jinja2 import Template
import numpy as np
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    #return "Input: {}".format(req)
    #return "Hello OpenFaaS!"
    
    #input = json.loads(req)
    #t = Template("{{greeting}} {{name}}")
    #res = t.render(name=input["name"], greeting=input["greeting"])
    #return res

    a = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 3, 4])
    return a.dot(b)