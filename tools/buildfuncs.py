import regex
import opcodes

ops = opcodes.lookup

for k, v in ops.items():
    opcode = regex.sub(
        "(?>\t|\s{2,})|(?>\,)|(?>\#\$|\$)", "", v[1]).strip()

    hexcode = k if len(k) == 4 else "0x0" + k[2:]

    print(f"elif opcode == \"{hexcode}\":\n\tcpu.{opcode}()".lower())
