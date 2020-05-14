# Not working - trial code
# Don't look in here. It's ugly and scary!

state = {
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


def emulate8080(state):

    opcode = f"{state['memory'][state['pc']]:#0{4}x}"

    if opcode == "0x00":
        pass
    if opcode == "0x01":
        state["b"] = hex(state["memory"][state["pc"] + 2])
        state["c"] = hex(state["memory"][state["pc"] + 1])
        state["pc"] += 2
    if opcode == "0x02":
        mem_loc = int(state["b"] + state["c"][2:], 16)
        state["a"] = hex(state['memory'][memloc])
    if opcode == "0x03":
        state["b"] = hex(int(state["b"], 16) + 1)
        state["c"] = hex(int(state["c"], 16) + 1)

    else:
        print("Opcode not found")


def main():

    try:
        with open("../invaders", "rb") as f:
            buffer = f.read()
    except IOError:
        sys.exit("File not found")

    pc = 0
    while pc < len(buffer):
        state["memory"].append(buffer[pc])
        pc += 1

    emulate8080(state)


main()
