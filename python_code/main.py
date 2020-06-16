#!/bin/python3

from recalculation import Recalculation
from router import Router


parser = argparse.ArgumentParser(description='EIGRP SDN prototype')

required = parser.add_argument_group('Required arguments')
required.add_argument('--router', required=True, action='append', help='Router IP addresses')
required.add_argument('--username', required=True, help='Username to login to routers')
required.add_argument('--password', required=True, help='Password to login to routers')

optional = parser.add_argument_group('Optional arguments')
optional.add_argument('--threshold', default='10', help='Threshold to trigger route topology updating')
optional.add_argument('--coefficient', default='0.8', help='Coefficient A')

args = parser.parse_args()

routers = []
for address in args.router:
    router = Router(address, args.username, args.password)
    routers.append(router)

recalculations = []
for router in routers:
    recalculations.append(Recalculation(router, args.coefficient, args.threshold))

for thread in recalculations:
    thread.start()

for thread in recalculations:
    thread.join()
