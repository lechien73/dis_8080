import regex
import opcodes

ops = opcodes.lookup

for k, v in ops.items():
    opcode = regex.sub(
        "(?>\t|\s{2,})|(?>\,)|(?>\#\$|\$)", "", v[1]).strip()

    hexcode = k if len(k) == 4 else "0x0" + k[2:]

    if hexcode[2:] != opcode:
        line = f"\tdef op_{hexcode}(self):\n\t\t".lower()
        line += "pass" if v[0] == 1 else f"self.state[\"pc\"] += {v[0] - 1}"
        line += "\n"
        print(line)
