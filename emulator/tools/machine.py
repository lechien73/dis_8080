class i8080():

    def __init__(self):

        self.state = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "h": 0,
            "l": 0,
            "sp": 0,
            "pc": 0,
            "memory": [],
            "int_enable": 0,
            "cc": {
                "z": 1,
                "s": 1,
                "p": 1,
                "cy": 1,
                "ac": 1,
                "pad": 3
            }
        }

    def nop(self):
        return

    def lxib(self):
        self.state["b"] = hex(self.state["memory"][self.state["pc"] + 2])
        self.state["c"] = hex(self.state["memory"][self.state["pc"] + 1])
        self.state["pc"] += 2

    def staxb(self):
        mem_loc = int(self.state["b"] + self.state["c"][2:], 16)
        self.state["a"] = hex(self.state['memory'][memloc])

    def inxb(self):
        self.state["b"] = hex(int(self.state["b"], 16) + 1)
        self.state["c"] = hex(int(self.state["c"], 16) + 1)
