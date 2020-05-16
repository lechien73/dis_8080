import sys
import regex
from tools import machine
from tools import opcodes

cpu = machine.i8080()


def init_optable():
    """
    Uses the opcodes dictionary to build one for
    assembly instead of disassembly
    """

    ops_table = {}

    ops = opcodes.lookup

    for k, v in ops.items():
        opcode = regex.sub(
            "(?>\t|\s{2,})|(?>\,)|(?>\#\$|\$)", "", v[1]).strip()
        hexcode = k if len(k) == 4 else "0x0" + k[2:]
        ops_table[hexcode] = [opcode, v[0]]

    return ops_table


def emulate8080(ops_table, debug):

    running = True

    while running:

        opcode = f"{cpu.state['memory'][cpu.state['pc']]:#0{4}x}"

        if opcode in ops_table:
            print(f"{cpu.state['pc']}: {ops_table[opcode][0]}")
            eval(f"cpu.op_{opcode}()")
        else:
            print("Invalid operation")
            running = False

        cpu.state["pc"] += 1

        if debug and input("Continue? ").lower() != "y":
            with open("debugfile.txt", "w") as f:
                for k, v in cpu.state.items():
                    f.write(f"{k}: {v}\n")
            running = False


def main(debug):

    try:
        with open("../tools/invaders", "rb") as f:
            buffer = f.read()
    except IOError:
        sys.exit("File not found")

    for b in buffer:
        cpu.state["memory"].append(b)

    ops_table = init_optable()

    emulate8080(ops_table, debug)


if __name__ == "__main__":
    main("debug" in sys.argv)
