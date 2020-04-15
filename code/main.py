#!/bin/python3

from deviceSetup import DeviceSetup

csr = DeviceSetup('172.31.1.10', 'dranser', 'cisco')
#interfaces = csr.get_interfaces()
#for interface in interfaces:
#    print(interface, csr.get_interface_txload(interface))

csr.restart_eigrp()
