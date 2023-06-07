from pypresence import Presence
from time import time
import sys
import os
try:
    RPC = Presence('1115928203115114557')
    RPC.connect()
    RPC.update(details=f"Editing {sys.argv[1]}",large_image='micro',large_text='micro',start=int(time()))
except:
    pass
os.system(f"micro {sys.argv[1]}")
