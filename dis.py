"""
Disassembler for Intel 8080 code
Usage: python3 dis.py <file_name>

(c) Matt Rudge
May, 2020
MIT License
"""

import sys
import opcodes

ops = opcodes.lookup


def dis8080(buffer, pc):
    """
    Takes the buffer and current program counter as input
    Tries to generate an opcode from the dictionary
    Prints a formatted line with address and code
    Returns the number of opcode bytes
    """

    try:
        opcode, opbytes = ops[hex(buffer[pc])][1], ops[hex(buffer[pc])][0]
    except KeyError:
        sys.exit(f"Error reading opcode: {hex(buffer[pc])}")

    # Start the line of assembly, format as 4 digit hex

    asm_line = f"{pc:#0{6}x}\t"[2:]

    if opbytes == 1:
        asm_line += opcode
    elif opbytes == 2:
        # Format the operand and pad with zero if needed
        operand = f"{buffer[pc + 1]:#0{4}x}"[2:]
        asm_line += f"{opcode}{operand}"
    elif opbytes == 3:
        # Swap the bytes around and pad with zero if needed
        operand1 = f"{buffer[pc + 2]:#0{4}x}"[2:]
        operand2 = f"{buffer[pc + 1]:#0{4}x}"[2:]

        asm_line += f"{opcode}{operand1}{operand2}"

    print(asm_line.upper())

    return opbytes


def main(filename):
    """
    Open the ROM file for reading as binary
    initialise program counter and start the
    read loop
    """

    try:
        with open(filename, "rb") as f:
            buffer = f.read()
    except IOError:
        sys.exit("File not found")

    pc = 0
    while pc < len(buffer):
        pc += dis8080(buffer, pc)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Usage: python3 dis.py <file_name>")
    else:
        main(sys.argv[1])
