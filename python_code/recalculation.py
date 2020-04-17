from router import Router


class Recalculation:
    TIMEOUT = 5

    def __init__(self, coefficient, threshold):
        self.coefficient = coefficient
        self.threshold = threshold

    def recalculate(self, routers):
        for router in routers:
            interfaces = router.get_interfaces()
            for interface in interfaces:
                name = interface.get_name()
                old_txload = interface.get_txload()
                current_txload = router.get_interface_txload(name)

                new_txload = round(self.coefficient * old_txload + (1 - self.coefficient) * current_txload)

                if abs(new_txload - old_txload) > self.threshold:
                    interface.set_txload(current_txload)
                    router.restart_eigrp()
                    print('Metric is recalculated for router: {router}'.format(router=router.get_host()))
                    print('Old Load: {old_load}; New Load: {new_load}'.format(old_load=old_txload, new_load=current_txload))
                    break
                else:
                    print('Load change on {interface_name} is less than threshold'.format(interface_name=name))
                    print('New Load: {new_load}; Old Load: {old_load}'.format(new_load=new_txload, old_load=old_txload))
