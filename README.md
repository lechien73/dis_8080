# 8080 Disassembler in Python

This is the first part of a project to emulate the 8080 chip. To be followed, hopefully, by emulation of the Z80 processor. I'm storing the Space Invaders ROMs here as an example of how the disassembly works.

## Usage

There are no dependencies for this project. To use it, simply clone or download this repository and run:

```
python3 dis.py <file_name>
```

Where `<file_name>` is the name of the file you wish to disassemble. So, to disassemble `invaders.h`, type:

```
python3 dis.py roms/invaders.h
```

You can redirect the output to a file like this:

```
python3 dis.py roms/invaders.h > invaders_h.asm
```

## Limitations

The disassembler only works with 8080 code. It is a work-in-progress, which means that it might behave unexpectedly or not at all. If it sets your house on fire or chases your cat around the living room, that's not my fault!

No guarantees are given regarding the quality of the disassembled code, although I have compared it with other disassemblies of the Space Invaders ROMs that are available online, and the output is identical.

## License

The Python code for this project is released under the MIT license. I don't know about the Space Invaders ROMS, they're not mine, and are provided here for educational purposes.

---

Matt Rudge
