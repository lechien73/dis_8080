lookup = {
    "0x0": [1, "NOP", 0],
    "0x1": [3, "LXI\tB,#$", 1],
    "0x2": [1, "STAX\tB", 0],
    "0x3": [1, "INX\tB", 0],
    "0x4": [1, "INR\tB", 0],
    "0x5": [1, "DCR\tB", 0],
    "0x6": [2, "MVI\tB,#$", 1],
    "0x7": [1, "RLC", 0],
    "0x8": [1, "", 0],
    "0x9": [1, "DAD\tB", 0],
    "0xa": [1, "LDAX\tB", 0],
    "0xb": [1, "DCX\tB", 0],
    "0xc": [1, "INR\tC", 0],
    "0xd": [1, "DCR\tC", 0],
    "0xe": [2, "MVI\tC,#$", 1],
    "0xf": [1, "RRC", 0],
    "0x10": [1, "", 0],
    "0x11": [3, "LXI\tD,#$", 1],
    "0x12": [1, "STAX\tD", 0],
    "0x13": [1, "INX\tD", 0],
    "0x14": [1, "INR\tD", 0],
    "0x15": [1, "DCR\tD", 0],
    "0x16": [2, "MVI\tD,#$", 1],
    "0x17": [1, "RAL", 0],
    "0x18": [1, "", 0],
    "0x19": [1, 'DAD\tD', 0],
    "0x1a": [1, 'LDAX\tD', 0],
    "0x1b": [1, 'DCX\tD', 0],
    "0x1c": [1, 'INR\tE', 0],
    "0x1d": [1, 'DCR\tE', 0],
    "0x1e": [2, 'MVI\tE,#$', 1],
    "0x1f": [1, 'RAR', 0],
    "0x20": [1, "", 0],
    "0x21": [3, 'LXI\tH,#$', 1],
    "0x22": [3, 'SHLD\t$', 1],
    "0x23": [1, 'INX\tH', 0],
    "0x24": [1, 'INR\tH', 0],
    "0x25": [1, 'DCR\tH', 0],
    "0x26": [2, 'MVI\tH,#$', 1],
    "0x27": [1, 'DAA', 0],
    "0x28": [1, "", 0],
    "0x29": [1, 'DAD\tH', 0],
    "0x2a": [3, 'LHLD\t$', 1],
    "0x2b": [1, 'DCX\tH', 0],
    "0x2c": [1, 'INR\tL', 0],
    "0x2d": [1, 'DCR\tL', 0],
    "0x2e": [2, 'MVI\tL,#$', 1],
    "0x2f": [1, 'CMA', 0],
    "0x30": [1, "", 0],
    "0x31": [3, 'LXI\tSP,#$', 1],
    "0x32": [3, 'STA\t$', 1],
    "0x33": [1, 'INX\tSP', 0],
    "0x34": [1, 'INR\tM', 0],
    "0x35": [1, 'DCR\tM', 0],
    "0x36": [2, 'MVI\tM,#$', 1],
    "0x37": [1, 'STC', 0],
    "0x38": [1, "", 0],
    "0x39": [1, 'DAD\tSP', 0],
    "0x3a": [3, 'LDA\t$', 1],
    "0x3b": [1, 'DCX\tSP', 0],
    "0x3c": [1, 'INR\tA', 0],
    "0x3d": [1, 'DCR\tA', 0],
    "0x3e": [2, 'MVI\tA,#$', 1],
    "0x3f": [1, 'CMC', 0],
    "0x40": [1, 'MOV\tB,B', 0],
    "0x41": [1, 'MOV\tB,C', 0],
    "0x42": [1, 'MOV\tB,D', 0],
    "0x43": [1, 'MOV\tB,E', 0],
    "0x44": [1, 'MOV\tB,H', 0],
    "0x45": [1, 'MOV\tB,L', 0],
    "0x46": [1, 'MOV\tB,M', 0],
    "0x47": [1, 'MOV\tB,A', 0],
    "0x48": [1, 'MOV\tC,B', 0],
    "0x49": [1, 'MOV\tC,C', 0],
    "0x4a": [1, 'MOV\tC,D', 0],
    "0x4b": [1, 'MOV\tC,E', 0],
    "0x4c": [1, 'MOV\tC,H', 0],
    "0x4d": [1, 'MOV\tC,L', 0],
    "0x4e": [1, 'MOV\tC,M', 0],
    "0x4f": [1, 'MOV\tC,A', 0],
    "0x50": [1, 'MOV\tD,B', 0],
    "0x51": [1, 'MOV\tD,C', 0],
    "0x52": [1, 'MOV\tD,D', 0],
    "0x53": [1, 'MOV\tD,E', 0],
    "0x54": [1, 'MOV\tD,H', 0],
    "0x55": [1, 'MOV\tD,L', 0],
    "0x56": [1, 'MOV\tD,M', 0],
    "0x57": [1, 'MOV\tD,A', 0],
    "0x58": [1, 'MOV\tE,B', 0],
    "0x59": [1, 'MOV\tE,C', 0],
    "0x5a": [1, 'MOV\tE,D', 0],
    "0x5b": [1, 'MOV\tE,E', 0],
    "0x5c": [1, 'MOV\tE,H', 0],
    "0x5d": [1, 'MOV\tE,L', 0],
    "0x5e": [1, 'MOV\tE,M', 0],
    "0x5f": [1, 'MOV\tE,A', 0],
    "0x60": [1, 'MOV\tH,B', 0],
    "0x61": [1, 'MOV\t H,C', 0],
    "0x62": [1, 'MOV\tH,D', 0],
    "0x63": [1, 'MOV\tH,E', 0],
    "0x64": [1, 'MOV\tH,H', 0],
    "0x65": [1, 'MOV\tH,L', 0],
    "0x66": [1, 'MOV\tH,M', 0],
    "0x67": [1, 'MOV\tH,A', 0],
    "0x68": [1, 'MOV\tL,B', 0],
    "0x69": [1, 'MOV\tL,C', 0],
    "0x6a": [1, 'MOV\tL,D', 0],
    "0x6b": [1, 'MOV\tL,E', 0],
    "0x6c": [1, 'MOV\tL,H', 0],
    "0x6d": [1, 'MOV\tL,L', 0],
    "0x6e": [1, 'MOV\tL,M', 0],
    "0x6f": [1, 'MOV\tL,A', 0],
    "0x70": [1, 'MOV\tM,B', 0],
    "0x71": [1, 'MOV\tM,C', 0],
    "0x72": [1, 'MOV\tM,D', 0],
    "0x73": [1, 'MOV\tM,E', 0],
    "0x74": [1, 'MOV\tM,H', 0],
    "0x75": [1, 'MOV\tM,L', 0],
    "0x76": [1, 'HLT', 0],
    "0x77": [1, 'MOV\tM,A', 0],
    "0x78": [1, 'MOV\tA,B', 0],
    "0x79": [1, 'MOV\tA,C', 0],
    "0x7a": [1, 'MOV\tA,D', 0],
    "0x7b": [1, 'MOV\tA,E', 0],
    "0x7c": [1, 'MOV\tA,H', 0],
    "0x7d": [1, 'MOV\tA,L', 0],
    "0x7e": [1, 'MOV\tA,M', 0],
    "0x7f": [1, 'MOV\tA,A', 0],
    "0x80": [1, 'ADD\tB', 0],
    "0x81": [1, 'ADD\tC', 0],
    "0x82": [1, 'ADD\tD', 0],
    "0x83": [1, 'ADD\tE', 0],
    "0x84": [1, 'ADD\tH', 0],
    "0x85": [1, 'ADD\tL', 0],
    "0x86": [1, 'ADD\tM', 0],
    "0x87": [1, 'ADD\tA', 0],
    "0x88": [1, 'ADC\tB', 0],
    "0x89": [1, 'ADC\tC', 0],
    "0x8a": [1, 'ADC\tD', 0],
    "0x8b": [1, 'ADC\tE', 0],
    "0x8c": [1, 'ADC\tH', 0],
    "0x8d": [1, 'ADC\tL', 0],
    "0x8e": [1, 'ADC\tM', 0],
    "0x8f": [1, 'ADC\tA', 0],
    "0x90": [1, 'SUB\tB', 0],
    "0x91": [1, 'SUB\tC', 0],
    "0x92": [1, 'SUB\tD', 0],
    "0x93": [1, 'SUB\tE', 0],
    "0x94": [1, 'SUB\tH', 0],
    "0x95": [1, 'SUB\tL', 0],
    "0x96": [1, 'SUB\tM', 0],
    "0x97": [1, 'SUB\tA', 0],
    "0x98": [1, 'SBB\tB', 0],
    "0x99": [1, 'SBB\tC', 0],
    "0x9a": [1, 'SBB\tD', 0],
    "0x9b": [1, 'SBB\tE', 0],
    "0x9c": [1, 'SBB\tH', 0],
    "0x9d": [1, 'SBB\tL', 0],
    "0x9e": [1, 'SBB\tM', 0],
    "0x9f": [1, 'SBB\tA', 0],
    "0xa0": [1, 'ANA\tB', 0],
    "0xa1": [1, 'ANA\tC', 0],
    "0xa2": [1, 'ANA\tD', 0],
    "0xa3": [1, 'ANA\tE', 0],
    "0xa4": [1, 'ANA\tH', 0],
    "0xa5": [1, 'ANA\tL', 0],
    "0xa6": [1, 'ANA\tM', 0],
    "0xa7": [1, 'ANA\tA', 0],
    "0xa8": [1, 'XRA\tB', 0],
    "0xa9": [1, 'XRA\tC', 0],
    "0xaa": [1, 'XRA\tD', 0],
    "0xab": [1, 'XRA\tE', 0],
    "0xac": [1, 'XRA\tH', 0],
    "0xad": [1, 'XRA\tL', 0],
    "0xae": [1, 'XRA\tM', 0],
    "0xaf": [1, 'XRA\tA', 0],
    "0xb0": [1, 'ORA\tB', 0],
    "0xb1": [1, 'ORA\tC', 0],
    "0xb2": [1, 'ORA\tD', 0],
    "0xb3": [1, 'ORA\tE', 0],
    "0xb4": [1, 'ORA\tH', 0],
    "0xb5": [1, 'ORA\tL', 0],
    "0xb6": [1, 'ORA\tM', 0],
    "0xb7": [1, 'ORA\tA', 0],
    "0xb8": [1, 'CMP\tB', 0],
    "0xb9": [1, 'CMP\tC', 0],
    "0xba": [1, 'CMP\tD', 0],
    "0xbb": [1, 'CMP\tE', 0],
    "0xbc": [1, 'CMP\tH', 0],
    "0xbd": [1, 'CMP\tL', 0],
    "0xbe": [1, 'CMP\tM', 0],
    "0xbf": [1, 'CMP\tA', 0],
    "0xc0": [1, 'RNZ', 0],
    "0xc1": [1, 'POP\tB', 0],
    "0xc2": [3, 'JNZ\t$', 1],
    "0xc3": [3, 'JMP\t$', 1],
    "0xc4": [3, 'CNZ\t$', 1],
    "0xc5": [1, 'PUSH\tB', 0],
    "0xc6": [2, 'ADI\t#$', 1],
    "0xc7": [1, 'RST\t0', 0],
    "0xc8": [1, 'RZ', 0],
    "0xc9": [1, 'RET', 0],
    "0xca": [3, 'JZ\t$', 1],
    "0xcb": [1, "", 0],
    "0xcc": [3, 'CZ\t$', 1],
    "0xcd": [3, 'CALL\t$', 1],
    "0xce": [2, 'ACI\t#$', 1],
    "0xcf": [1, 'RST\t1', 0],
    "0xd0": [1, 'RNC', 0],
    "0xd1": [1, 'POP\tD', 0],
    "0xd2": [3, 'JNC\t$', 1],
    "0xd3": [2, 'OUT\t#$', 1],
    "0xd4": [3, 'CNC\t$', 1],
    "0xd5": [1, 'PUSH\tD', 0],
    "0xd6": [2, 'SUI\t#$', 1],
    "0xd7": [1, 'RST\t2', 0],
    "0xd8": [1, 'RC', 0],
    "0xd9": [1, "", 0],
    "0xda": [3, 'JC\t$', 1],
    "0xdb": [2, 'IN\t#$', 1],
    "0xdc": [3, 'CC\t$', 1],
    "0xdd": [1, "", 0],
    "0xde": [2, 'SBI\t#$', 1],
    "0xdf": [1, 'RST\t3', 0],
    "0xe0": [1, 'RPO', 0],
    "0xe1": [1, 'POP\tH', 0],
    "0xe2": [3, 'JPO\t$', 1],
    "0xe3": [1, 'XTHL', 0],
    "0xe4": [3, 'CPO\t$', 1],
    "0xe5":	[1, "PUSH\tH", 0],
    "0xe6": [2, 'ANI\t#$', 1],
    "0xe7": [1, 'RST\t4', 0],
    "0xe8": [1, 'RPE', 0],
    "0xe9": [1, 'PCHL', 0],
    "0xea": [3, 'JPE\t$', 1],
    "0xeb": [1, 'XCHG', 0],
    "0xec": [3, 'CPE\t$', 1],
    "0xed": [1, "", 0],
    "0xee": [2, 'XRI\t#$', 1],
    "0xef": [1, 'RST\t5', 0],
    "0xf0": [1, 'RP', 0],
    "0xf1": [1, 'POP\tPSW', 0],
    "0xf2": [3, 'JP\t$', 1],
    "0xf3": [1, 'DI', 0],
    "0xf4": [3, 'CP\t$', 1],
    "0xf5": [1, 'PUSH\tPSW', 0],
    "0xf6": [2, 'ORI\t#$', 1],
    "0xf7": [1, 'RST\t6', 0],
    "0xf8": [1, 'RM', 0],
    "0xf9": [1, 'SPHL', 0],
    "0xfa": [3, 'JM\t$', 1],
    "0xfb": [1, 'EI', 0],
    "0xfc": [3, 'CM\t$', 1],
    "0xfd": [1, "", 0],
    "0xfe": [2, 'CPI\t#$', 1],
    "0xff": [1, 'RST\t7', 0]
}
