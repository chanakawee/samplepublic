import pandas as pd
import numpy as np
import datetime as datetime
from sud_vs_block3 import sud_vs_block3

def read(blockname,params):
    blockname = str(blockname).replace("-","_")
    blockname = str(blockname).replace(" ","_")
    return {"data":sud_vs_block3(params)}

def sud_vs_block2(params):
    #This is a python Test for v-intigration
    testlist = []
    acclist = read("sud-vs-block3",{})["data"]
    testlist.append(acclist)
    testlist.append({"My Test Append"})
    #response["data"] = testlist
    return {"data":testlist}

print(sud_vs_block2({"a":1,"b":2}))