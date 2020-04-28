#!/bin/python3

from recalculation import Recalculation
from router import Router


router1 = Router('172.31.1.10', 'dranser', 'cisco')
routers = [router1]

recalculations = []
for router in routers:
    recalculations.append(Recalculation(router, 0.8, 10))

for thread in recalculations:
    thread.start()

for thread in recalculations:
    thread.join()
