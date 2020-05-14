"""
Simple Intel 8080 assembler

Usage: python3 asm.py source_file binary_file

Part of my project to see if I really understand the
8080 architecture and assembly language.

(c) Matt Rudge
May, 2020
MIT License
"""

import opcodes
import regex
import sys


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
        hexcode = k[2:] if len(k) == 4 else "0" + k[2:]
        ops_table[opcode] = [hexcode, v[0]]

    return ops_table


def char_convert(character):
    """
    Returns the ASCII character code for the opcode
    and data.
    I could have done this in the assemble function
    but separated it for readability.
    """

    new_char = int("0x" + character, 0)
    return new_char


def clean_line(line):
    """
    Funky bits of regex to clean the lines. It means that
    a line like this: MOV   A, #$16BF
    will become this: ["MOVA", "16BF"]
    """

    line = regex.sub("(?>\t|\s{2,})|(?>\,)", "", line)
    line = regex.sub("(?>\#\$|\$)", " ", line).split(" ")

    return line


def assemble(line, ops_table):
    """
    Cleans the line, gets the corresponding hex code for
    the opcode from the dictionary.
    Processes any operands and returns the hex for writing
    """

    line = clean_line(line)

    op = char_convert(ops_table[line[0]][0]) if line[0] in ops_table else 0

    # memory addresses and values are stored big endian, but are coded
    # little endian

    data = []
    if len(line) > 1:
        data = [char_convert(line[1])] if len(line[1]) == 2 else \
               [char_convert(line[1][2:]), char_convert(line[1][:2])]

    data.insert(0, op)

    return data


def main(input_file, output_file):
    """
    Initialises the opcodes table, opens the source
    file and the binary file.
    Calls the assembly procedure.
    """

    ops_table = init_optable()

    try:
        print(f"Opening source file: {input_file}")
        with open(input_file, "r") as i:
            lines = i.read().split("\n")
    except IOError:
        sys.exit("Error: Input file does not exist")

    with open(output_file, "wb") as o:
        print(f"Creating binary file: {output_file}")
        count = 0
        for line in lines:
            count += 1
            if len(line.strip()) > 1:
                o.write(bytearray(assemble(line, ops_table)))

        print(f"{count} lines processed")


if __name__ == "__main__":
    version = 0.8
    print(f"Intel 8080 Assembler v{version}")
    print("Matt Rudge, May 2020")
    print("--------------------")
    if len(sys.argv) < 3:
        sys.exit("Usage: python3 asm.py input_file output_file")
    else:
        main(sys.argv[1], sys.argv[2])
