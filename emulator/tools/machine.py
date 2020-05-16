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

    def _flag_zero(self, check):
        self.state["cc"]["z"] = int(check == 0)

    def _flag_sign(self, check):
        self.state["cc"]["s"] = int((0x80 == (check & 0x80)))

    def _flag_parity(self, check, size):
        p = 0
        check = (check & ((1 << size) - 1))
        for i in range(size):
            if (x & 0x1):
                p += 1

            check = check >> 1

        self.state["cc"]["p"] = int((p & 0x1) == 0)

    def op_0x00(self):
        return

    def op_0x01(self):
        self.state["b"] = hex(self.state["memory"][self.state["pc"] + 2])
        self.state["c"] = hex(self.state["memory"][self.state["pc"] + 1])
        self.state["pc"] += 2

    def op_0x02(self):
        mem_loc = int(self.state["b"] + self.state["c"][2:], 16)
        self.state["a"] = hex(self.state['memory'][memloc])

    def op_0x03(self):
        self.state["b"] = hex(int(self.state["b"], 16) +
                              1) if int(self.state["b"], 16) + 1 <= 255 else 0
        self.state["c"] = hex(int(self.state["c"], 16) +
                              1) if int(self.state["c"], 16) + 1 <= 255 else 0

    def op_0x04(self):
        self.state["b"] = hex(int(self.state["b"], 16) +
                              1) if int(self.state["b"], 16) + 1 <= 255 else 0
        self._flag_zero(self.state["b"])
        self._flag_sign(self.state["b"])
        self._flag_parity(self.state["b"], 8)

    def op_0x05(self):
        self.state["b"] = hex(int(self.state["b"], 16) - 1)
        self._flag_zero(self.state["b"])
        self._flag_sign(self.state["b"])
        self._flag_parity(self.state["b"], 8)

    def op_0x06(self):
        self.state["b"] = hex(self.state["memory"][self.state["pc"] + 1])
        self.state["pc"] += 1

    def op_0x07(self):
        self.state["cc"]["c"] = int(bin(self.state["a"])[2:3])
        rotate = bin(self.state["a"])[3:] + bin(self.state["a"])[2:3]
        self.state["a"] = hex(int("0b" + rotate))

    def op_0x09(self):
        pass

    def op_0x0a(self):
        pass

    def op_0x0b(self):
        pass

    def op_0x0c(self):
        pass

    def op_0x0d(self):
        pass

    def op_0x0e(self):
        self.state["pc"] += 1

    def op_0x0f(self):
        pass

    def op_0x11(self):
        self.state["pc"] += 2

    def op_0x12(self):
        pass

    def op_0x13(self):
        pass

    def op_0x14(self):
        pass

    def op_0x15(self):
        pass

    def op_0x16(self):
        self.state["pc"] += 1

    def op_0x17(self):
        pass

    def op_0x19(self):
        pass

    def op_0x1a(self):
        pass

    def op_0x1b(self):
        pass

    def op_0x1c(self):
        pass

    def op_0x1d(self):
        pass

    def op_0x1e(self):
        self.state["pc"] += 1

    def op_0x1f(self):
        pass

    def op_0x21(self):
        self.state["pc"] += 2

    def op_0x22(self):
        self.state["pc"] += 2

    def op_0x23(self):
        pass

    def op_0x24(self):
        pass

    def op_0x25(self):
        pass

    def op_0x26(self):
        self.state["pc"] += 1

    def op_0x27(self):
        pass

    def op_0x29(self):
        pass

    def op_0x2a(self):
        self.state["pc"] += 2

    def op_0x2b(self):
        pass

    def op_0x2c(self):
        pass

    def op_0x2d(self):
        pass

    def op_0x2e(self):
        self.state["pc"] += 1

    def op_0x2f(self):
        pass

    def op_0x31(self):
        self.state["pc"] += 2

    def op_0x32(self):
        self.state["pc"] += 2

    def op_0x33(self):
        pass

    def op_0x34(self):
        pass

    def op_0x35(self):
        pass

    def op_0x36(self):
        self.state["pc"] += 1

    def op_0x37(self):
        pass

    def op_0x39(self):
        pass

    def op_0x3a(self):
        self.state["pc"] += 2

    def op_0x3b(self):
        pass

    def op_0x3c(self):
        pass

    def op_0x3d(self):
        pass

    def op_0x3e(self):
        self.state["pc"] += 1

    def op_0x3f(self):
        pass

    def op_0x40(self):
        pass

    def op_0x41(self):
        pass

    def op_0x42(self):
        pass

    def op_0x43(self):
        pass

    def op_0x44(self):
        pass

    def op_0x45(self):
        pass

    def op_0x46(self):
        pass

    def op_0x47(self):
        pass

    def op_0x48(self):
        pass

    def op_0x49(self):
        pass

    def op_0x4a(self):
        pass

    def op_0x4b(self):
        pass

    def op_0x4c(self):
        pass

    def op_0x4d(self):
        pass

    def op_0x4e(self):
        pass

    def op_0x4f(self):
        pass

    def op_0x50(self):
        pass

    def op_0x51(self):
        pass

    def op_0x52(self):
        pass

    def op_0x53(self):
        pass

    def op_0x54(self):
        pass

    def op_0x55(self):
        pass

    def op_0x56(self):
        pass

    def op_0x57(self):
        pass

    def op_0x58(self):
        pass

    def op_0x59(self):
        pass

    def op_0x5a(self):
        pass

    def op_0x5b(self):
        pass

    def op_0x5c(self):
        pass

    def op_0x5d(self):
        pass

    def op_0x5e(self):
        pass

    def op_0x5f(self):
        pass

    def op_0x60(self):
        pass

    def op_0x61(self):
        pass

    def op_0x62(self):
        pass

    def op_0x63(self):
        pass

    def op_0x64(self):
        pass

    def op_0x65(self):
        pass

    def op_0x66(self):
        pass

    def op_0x67(self):
        pass

    def op_0x68(self):
        pass

    def op_0x69(self):
        pass

    def op_0x6a(self):
        pass

    def op_0x6b(self):
        pass

    def op_0x6c(self):
        pass

    def op_0x6d(self):
        pass

    def op_0x6e(self):
        pass

    def op_0x6f(self):
        pass

    def op_0x70(self):
        pass

    def op_0x71(self):
        pass

    def op_0x72(self):
        pass

    def op_0x73(self):
        pass

    def op_0x74(self):
        pass

    def op_0x75(self):
        pass

    def op_0x76(self):
        pass

    def op_0x77(self):
        pass

    def op_0x78(self):
        pass

    def op_0x79(self):
        pass

    def op_0x7a(self):
        pass

    def op_0x7b(self):
        pass

    def op_0x7c(self):
        pass

    def op_0x7d(self):
        pass

    def op_0x7e(self):
        pass

    def op_0x7f(self):
        pass

    def op_0x80(self):
        pass

    def op_0x81(self):
        pass

    def op_0x82(self):
        pass

    def op_0x83(self):
        pass

    def op_0x84(self):
        pass

    def op_0x85(self):
        pass

    def op_0x86(self):
        pass

    def op_0x87(self):
        pass

    def op_0x88(self):
        pass

    def op_0x89(self):
        pass

    def op_0x8a(self):
        pass

    def op_0x8b(self):
        pass

    def op_0x8c(self):
        pass

    def op_0x8d(self):
        pass

    def op_0x8e(self):
        pass

    def op_0x8f(self):
        pass

    def op_0x90(self):
        pass

    def op_0x91(self):
        pass

    def op_0x92(self):
        pass

    def op_0x93(self):
        pass

    def op_0x94(self):
        pass

    def op_0x95(self):
        pass

    def op_0x96(self):
        pass

    def op_0x97(self):
        pass

    def op_0x98(self):
        pass

    def op_0x99(self):
        pass

    def op_0x9a(self):
        pass

    def op_0x9b(self):
        pass

    def op_0x9c(self):
        pass

    def op_0x9d(self):
        pass

    def op_0x9e(self):
        pass

    def op_0x9f(self):
        pass

    def op_0xa0(self):
        pass

    def op_0xa1(self):
        pass

    def op_0xa2(self):
        pass

    def op_0xa3(self):
        pass

    def op_0xa4(self):
        pass

    def op_0xa5(self):
        pass

    def op_0xa6(self):
        pass

    def op_0xa7(self):
        pass

    def op_0xa8(self):
        pass

    def op_0xa9(self):
        pass

    def op_0xaa(self):
        pass

    def op_0xab(self):
        pass

    def op_0xac(self):
        pass

    def op_0xad(self):
        pass

    def op_0xae(self):
        pass

    def op_0xaf(self):
        pass

    def op_0xb0(self):
        pass

    def op_0xb1(self):
        pass

    def op_0xb2(self):
        pass

    def op_0xb3(self):
        pass

    def op_0xb4(self):
        pass

    def op_0xb5(self):
        pass

    def op_0xb6(self):
        pass

    def op_0xb7(self):
        pass

    def op_0xb8(self):
        pass

    def op_0xb9(self):
        pass

    def op_0xba(self):
        pass

    def op_0xbb(self):
        pass

    def op_0xbc(self):
        pass

    def op_0xbd(self):
        pass

    def op_0xbe(self):
        pass

    def op_0xbf(self):
        pass

    def op_0xc0(self):
        pass

    def op_0xc1(self):
        pass

    def op_0xc2(self):
        self.state["pc"] += 2

    def op_0xc3(self):
        mem_loc1 = int(hex(self.state["memory"][self.state["pc"] + 2]), 16)
        mem_loc2 = int(hex(self.state["memory"][self.state["pc"] + 1]), 16)
        self.state["pc"] = (mem_loc1 << 8) | mem_loc2 - 1

    def op_0xc4(self):
        self.state["pc"] += 2

    def op_0xc5(self):
        pass

    def op_0xc6(self):
        self.state["pc"] += 1

    def op_0xc7(self):
        pass

    def op_0xc8(self):
        pass

    def op_0xc9(self):
        pass

    def op_0xca(self):
        self.state["pc"] += 2

    def op_0xcc(self):
        self.state["pc"] += 2

    def op_0xcd(self):
        self.state["pc"] += 2

    def op_0xce(self):
        self.state["pc"] += 1

    def op_0xcf(self):
        pass

    def op_0xd0(self):
        pass

    def op_0xd1(self):
        pass

    def op_0xd2(self):
        self.state["pc"] += 2

    def op_0xd3(self):
        self.state["pc"] += 1

    def op_0xd4(self):
        self.state["pc"] += 2

    def op_0xd5(self):
        pass

    def op_0xd6(self):
        self.state["pc"] += 1

    def op_0xd7(self):
        pass

    def op_0xd8(self):
        pass

    def op_0xda(self):
        self.state["pc"] += 2

    def op_0xdb(self):
        self.state["pc"] += 1

    def op_0xdc(self):
        self.state["pc"] += 2

    def op_0xde(self):
        self.state["pc"] += 1

    def op_0xdf(self):
        pass

    def op_0xe0(self):
        pass

    def op_0xe1(self):
        pass

    def op_0xe2(self):
        self.state["pc"] += 2

    def op_0xe3(self):
        pass

    def op_0xe4(self):
        self.state["pc"] += 2

    def op_0xe5(self):
        pass

    def op_0xe6(self):
        self.state["pc"] += 1

    def op_0xe7(self):
        pass

    def op_0xe8(self):
        pass

    def op_0xe9(self):
        pass

    def op_0xea(self):
        self.state["pc"] += 2

    def op_0xeb(self):
        pass

    def op_0xec(self):
        self.state["pc"] += 2

    def op_0xee(self):
        self.state["pc"] += 1

    def op_0xef(self):
        pass

    def op_0xf0(self):
        pass

    def op_0xf1(self):
        pass

    def op_0xf2(self):
        self.state["pc"] += 2

    def op_0xf3(self):
        pass

    def op_0xf4(self):
        self.state["pc"] += 2

    def op_0xf5(self):
        pass

    def op_0xf6(self):
        self.state["pc"] += 1

    def op_0xf7(self):
        pass

    def op_0xf8(self):
        pass

    def op_0xf9(self):
        pass

    def op_0xfa(self):
        self.state["pc"] += 2

    def op_0xfb(self):
        pass

    def op_0xfc(self):
        self.state["pc"] += 2

    def op_0xfe(self):
        self.state["pc"] += 1

    def op_0xff(self):
        pass
