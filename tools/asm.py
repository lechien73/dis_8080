import opcodes
import regex
import sys

ops = opcodes.lookup

ops_table = {}

for k, v in ops.items():
    opcode = regex.sub("(?>\t|\s{2,})|(?>\,)|(?>\#\$|\$)", "", v[1]).strip()
    hexcode = k[2:] if len(k) == 4 else "0" + k[2:]
    ops_table[opcode] = [hexcode, v[0]]


def char_convert(character):

    new_char = int("0x" + character, 0)
    return new_char


def assemble(line):

    line = regex.sub("(?>\t|\s{2,})|(?>\,)", "", line)
    line = regex.sub("(?>\#\$|\$)", " ", line).split(" ")

    op = char_convert(ops_table[line[0]][0]) if line[0] in ops_table else 0

    if len(line) > 1:
        data = [char_convert(line[1])] if len(line[1]) == 2 else [char_convert(
            line[1][2:]), char_convert(line[1][:2])]
    else:
        data = []

    if data:
        data.insert(0, op)
        code = data
    else:
        code = [op]

    return code


def main(input_file, output_file):

    try:
        with open(input_file, "r") as i:
            lines = i.read().split("\n")
    except IOError:
        sys.exit("Error: Input file does not exist")

    with open(output_file, "wb") as o:
        count = 0
        for line in lines:
            count += 1
            print(f"Line: {count}")
            o.write(bytearray(assemble(line)))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 asm.py input_file output_file")
    else:
        main(sys.argv[1], sys.argv[2])
