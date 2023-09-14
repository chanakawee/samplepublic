import pandas as pd
import numpy as np
import datetime as datetime

def sud_vs_block1(params):
    #This is a python Test for v-intigration
    a = 0
    b = 0
    if(params.__len__()>0):
        a = int(params["a"])
        b = int(params["b"])
    return {"data":{"Multiply":a*b}}

print(sud_vs_block1({"a":1,"b":2}))