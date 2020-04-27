#!/bin/python3

import time

from recalculation import Recalculation
from router import Router


router1 = Router('172.31.1.10', 'dranser', 'cisco')
routers = [router1]

recalculation = []
for router in routers:
    recalculation.append(Recalculation(router, 0.8, 10))

while True:
    for thread in recalculation:
        thread.start()

    for thread in recalculation:
        thread.join()

    time.sleep(Recalculation.TIMEOUT)
