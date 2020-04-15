class Interface:
    def __init__(self, name, txload):
        self.name = name
        self.txload = txload

    def get_name(self):
        return self.name

    def get_txload(self):
        return self.txload

    def set_txload(self, txload):
        self.txload = txload
