#!/bin/python3

import time

from recalculation import Recalculation
from router import Router


csr = Router('172.31.1.10', 'dranser', 'cisco')
routers = [csr]
recalculation = Recalculation(0.8, 10)

while True:
    recalculation.recalculate(routers)
    time.sleep(Recalculation.TIMEOUT)
