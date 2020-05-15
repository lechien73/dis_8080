import sys
from tools import machine

cpu = machine.i8080()


def emulate8080():

    running = True

    while running:

        opcode = f"{cpu.state['memory'][cpu.state['pc']]:#0{4}x}"

        if opcode == "0x00":
            cpu.nop()
        elif opcode == "0x01":
            cpu.lxib()
        elif opcode == "0x02":
            cpu.staxb()
        elif opcode == "0x03":
            cpu.inxb()
        elif opcode == "0x04":
            cpu.inrb()
        elif opcode == "0x05":
            cpu.dcrb()
        elif opcode == "0x06":
            cpu.mvib()
        elif opcode == "0x07":
            cpu.rlc()
        elif opcode == "0x09":
            cpu.dadb()
        elif opcode == "0x0a":
            cpu.ldaxb()
        elif opcode == "0x0b":
            cpu.dcxb()
        elif opcode == "0x0c":
            cpu.inrc()
        elif opcode == "0x0d":
            cpu.dcrc()
        elif opcode == "0x0e":
            cpu.mvic()
        elif opcode == "0x0f":
            cpu.rrc()
        elif opcode == "0x11":
            cpu.lxid()
        elif opcode == "0x12":
            cpu.staxd()
        elif opcode == "0x13":
            cpu.inxd()
        elif opcode == "0x14":
            cpu.inrd()
        elif opcode == "0x15":
            cpu.dcrd()
        elif opcode == "0x16":
            cpu.mvid()
        elif opcode == "0x17":
            cpu.ral()
        elif opcode == "0x19":
            cpu.dadd()
        elif opcode == "0x1a":
            cpu.ldaxd()
        elif opcode == "0x1b":
            cpu.dcxd()
        elif opcode == "0x1c":
            cpu.inre()
        elif opcode == "0x1d":
            cpu.dcre()
        elif opcode == "0x1e":
            cpu.mvie()
        elif opcode == "0x1f":
            cpu.rar()
        elif opcode == "0x21":
            cpu.lxih()
        elif opcode == "0x22":
            cpu.shld()
        elif opcode == "0x23":
            cpu.inxh()
        elif opcode == "0x24":
            cpu.inrh()
        elif opcode == "0x25":
            cpu.dcrh()
        elif opcode == "0x26":
            cpu.mvih()
        elif opcode == "0x27":
            cpu.daa()
        elif opcode == "0x29":
            cpu.dadh()
        elif opcode == "0x2a":
            cpu.lhld()
        elif opcode == "0x2b":
            cpu.dcxh()
        elif opcode == "0x2c":
            cpu.inrl()
        elif opcode == "0x2d":
            cpu.dcrl()
        elif opcode == "0x2e":
            cpu.mvil()
        elif opcode == "0x2f":
            cpu.cma()
        elif opcode == "0x31":
            cpu.lxisp()
        elif opcode == "0x32":
            cpu.sta()
        elif opcode == "0x33":
            cpu.inxsp()
        elif opcode == "0x34":
            cpu.inrm()
        elif opcode == "0x35":
            cpu.dcrm()
        elif opcode == "0x36":
            cpu.mvim()
        elif opcode == "0x37":
            cpu.stc()
        elif opcode == "0x39":
            cpu.dadsp()
        elif opcode == "0x3a":
            cpu.lda()
        elif opcode == "0x3b":
            cpu.dcxsp()
        elif opcode == "0x3c":
            cpu.inra()
        elif opcode == "0x3d":
            cpu.dcra()
        elif opcode == "0x3e":
            cpu.mvia()
        elif opcode == "0x3f":
            cpu.cmc()
        elif opcode == "0x40":
            cpu.movbb()
        elif opcode == "0x41":
            cpu.movbc()
        elif opcode == "0x42":
            cpu.movbd()
        elif opcode == "0x43":
            cpu.movbe()
        elif opcode == "0x44":
            cpu.movbh()
        elif opcode == "0x45":
            cpu.movbl()
        elif opcode == "0x46":
            cpu.movbm()
        elif opcode == "0x47":
            cpu.movba()
        elif opcode == "0x48":
            cpu.movcb()
        elif opcode == "0x49":
            cpu.movcc()
        elif opcode == "0x4a":
            cpu.movcd()
        elif opcode == "0x4b":
            cpu.movce()
        elif opcode == "0x4c":
            cpu.movch()
        elif opcode == "0x4d":
            cpu.movcl()
        elif opcode == "0x4e":
            cpu.movcm()
        elif opcode == "0x4f":
            cpu.movca()
        elif opcode == "0x50":
            cpu.movdb()
        elif opcode == "0x51":
            cpu.movdc()
        elif opcode == "0x52":
            cpu.movdd()
        elif opcode == "0x53":
            cpu.movde()
        elif opcode == "0x54":
            cpu.movdh()
        elif opcode == "0x55":
            cpu.movdl()
        elif opcode == "0x56":
            cpu.movdm()
        elif opcode == "0x57":
            cpu.movda()
        elif opcode == "0x58":
            cpu.moveb()
        elif opcode == "0x59":
            cpu.movec()
        elif opcode == "0x5a":
            cpu.moved()
        elif opcode == "0x5b":
            cpu.movee()
        elif opcode == "0x5c":
            cpu.moveh()
        elif opcode == "0x5d":
            cpu.movel()
        elif opcode == "0x5e":
            cpu.movem()
        elif opcode == "0x5f":
            cpu.movea()
        elif opcode == "0x60":
            cpu.movhb()
        elif opcode == "0x61":
            cpu.movhc()
        elif opcode == "0x62":
            cpu.movhd()
        elif opcode == "0x63":
            cpu.movhe()
        elif opcode == "0x64":
            cpu.movhh()
        elif opcode == "0x65":
            cpu.movhl()
        elif opcode == "0x66":
            cpu.movhm()
        elif opcode == "0x67":
            cpu.movha()
        elif opcode == "0x68":
            cpu.movlb()
        elif opcode == "0x69":
            cpu.movlc()
        elif opcode == "0x6a":
            cpu.movld()
        elif opcode == "0x6b":
            cpu.movle()
        elif opcode == "0x6c":
            cpu.movlh()
        elif opcode == "0x6d":
            cpu.movll()
        elif opcode == "0x6e":
            cpu.movlm()
        elif opcode == "0x6f":
            cpu.movla()
        elif opcode == "0x70":
            cpu.movmb()
        elif opcode == "0x71":
            cpu.movmc()
        elif opcode == "0x72":
            cpu.movmd()
        elif opcode == "0x73":
            cpu.movme()
        elif opcode == "0x74":
            cpu.movmh()
        elif opcode == "0x75":
            cpu.movml()
        elif opcode == "0x76":
            cpu.hlt()
        elif opcode == "0x77":
            cpu.movma()
        elif opcode == "0x78":
            cpu.movab()
        elif opcode == "0x79":
            cpu.movac()
        elif opcode == "0x7a":
            cpu.movad()
        elif opcode == "0x7b":
            cpu.movae()
        elif opcode == "0x7c":
            cpu.movah()
        elif opcode == "0x7d":
            cpu.moval()
        elif opcode == "0x7e":
            cpu.movam()
        elif opcode == "0x7f":
            cpu.movaa()
        elif opcode == "0x80":
            cpu.addb()
        elif opcode == "0x81":
            cpu.addc()
        elif opcode == "0x82":
            cpu.addd()
        elif opcode == "0x83":
            cpu.adde()
        elif opcode == "0x84":
            cpu.addh()
        elif opcode == "0x85":
            cpu.addl()
        elif opcode == "0x86":
            cpu.addm()
        elif opcode == "0x87":
            cpu.adda()
        elif opcode == "0x88":
            cpu.adcb()
        elif opcode == "0x89":
            cpu.adcc()
        elif opcode == "0x8a":
            cpu.adcd()
        elif opcode == "0x8b":
            cpu.adce()
        elif opcode == "0x8c":
            cpu.adch()
        elif opcode == "0x8d":
            cpu.adcl()
        elif opcode == "0x8e":
            cpu.adcm()
        elif opcode == "0x8f":
            cpu.adca()
        elif opcode == "0x90":
            cpu.subb()
        elif opcode == "0x91":
            cpu.subc()
        elif opcode == "0x92":
            cpu.subd()
        elif opcode == "0x93":
            cpu.sube()
        elif opcode == "0x94":
            cpu.subh()
        elif opcode == "0x95":
            cpu.subl()
        elif opcode == "0x96":
            cpu.subm()
        elif opcode == "0x97":
            cpu.suba()
        elif opcode == "0x98":
            cpu.sbbb()
        elif opcode == "0x99":
            cpu.sbbc()
        elif opcode == "0x9a":
            cpu.sbbd()
        elif opcode == "0x9b":
            cpu.sbbe()
        elif opcode == "0x9c":
            cpu.sbbh()
        elif opcode == "0x9d":
            cpu.sbbl()
        elif opcode == "0x9e":
            cpu.sbbm()
        elif opcode == "0x9f":
            cpu.sbba()
        elif opcode == "0xa0":
            cpu.anab()
        elif opcode == "0xa1":
            cpu.anac()
        elif opcode == "0xa2":
            cpu.anad()
        elif opcode == "0xa3":
            cpu.anae()
        elif opcode == "0xa4":
            cpu.anah()
        elif opcode == "0xa5":
            cpu.anal()
        elif opcode == "0xa6":
            cpu.anam()
        elif opcode == "0xa7":
            cpu.anaa()
        elif opcode == "0xa8":
            cpu.xrab()
        elif opcode == "0xa9":
            cpu.xrac()
        elif opcode == "0xaa":
            cpu.xrad()
        elif opcode == "0xab":
            cpu.xrae()
        elif opcode == "0xac":
            cpu.xrah()
        elif opcode == "0xad":
            cpu.xral()
        elif opcode == "0xae":
            cpu.xram()
        elif opcode == "0xaf":
            cpu.xraa()
        elif opcode == "0xb0":
            cpu.orab()
        elif opcode == "0xb1":
            cpu.orac()
        elif opcode == "0xb2":
            cpu.orad()
        elif opcode == "0xb3":
            cpu.orae()
        elif opcode == "0xb4":
            cpu.orah()
        elif opcode == "0xb5":
            cpu.oral()
        elif opcode == "0xb6":
            cpu.oram()
        elif opcode == "0xb7":
            cpu.oraa()
        elif opcode == "0xb8":
            cpu.cmpb()
        elif opcode == "0xb9":
            cpu.cmpc()
        elif opcode == "0xba":
            cpu.cmpd()
        elif opcode == "0xbb":
            cpu.cmpe()
        elif opcode == "0xbc":
            cpu.cmph()
        elif opcode == "0xbd":
            cpu.cmpl()
        elif opcode == "0xbe":
            cpu.cmpm()
        elif opcode == "0xbf":
            cpu.cmpa()
        elif opcode == "0xc0":
            cpu.rnz()
        elif opcode == "0xc1":
            cpu.popb()
        elif opcode == "0xc2":
            cpu.jnz()
        elif opcode == "0xc3":
            cpu.jmp()
        elif opcode == "0xc4":
            cpu.cnz()
        elif opcode == "0xc5":
            cpu.pushb()
        elif opcode == "0xc6":
            cpu.adi()
        elif opcode == "0xc7":
            cpu.rst0()
        elif opcode == "0xc8":
            cpu.rz()
        elif opcode == "0xc9":
            cpu.ret()
        elif opcode == "0xca":
            cpu.jz()
        elif opcode == "0xcc":
            cpu.cz()
        elif opcode == "0xcd":
            cpu.call()
        elif opcode == "0xce":
            cpu.aci()
        elif opcode == "0xcf":
            cpu.rst1()
        elif opcode == "0xd0":
            cpu.rnc()
        elif opcode == "0xd1":
            cpu.popd()
        elif opcode == "0xd2":
            cpu.jnc()
        elif opcode == "0xd3":
            cpu.out()
        elif opcode == "0xd4":
            cpu.cnc()
        elif opcode == "0xd5":
            cpu.pushd()
        elif opcode == "0xd6":
            cpu.sui()
        elif opcode == "0xd7":
            cpu.rst2()
        elif opcode == "0xd8":
            cpu.rc()
        elif opcode == "0xda":
            cpu.jc()
        elif opcode == "0xdb":
            cpu.in()
        elif opcode == "0xdc":
            cpu.cc()
        elif opcode == "0xde":
            cpu.sbi()
        elif opcode == "0xdf":
            cpu.rst3()
        elif opcode == "0xe0":
            cpu.rpo()
        elif opcode == "0xe1":
            cpu.poph()
        elif opcode == "0xe2":
            cpu.jpo()
        elif opcode == "0xe3":
            cpu.xthl()
        elif opcode == "0xe4":
            cpu.cpo()
        elif opcode == "0xe5":
            cpu.pushh()
        elif opcode == "0xe6":
            cpu.ani()
        elif opcode == "0xe7":
            cpu.rst4()
        elif opcode == "0xe8":
            cpu.rpe()
        elif opcode == "0xe9":
            cpu.pchl()
        elif opcode == "0xea":
            cpu.jpe()
        elif opcode == "0xeb":
            cpu.xchg()
        elif opcode == "0xec":
            cpu.cpe()
        elif opcode == "0xee":
            cpu.xri()
        elif opcode == "0xef":
            cpu.rst5()
        elif opcode == "0xf0":
            cpu.rp()
        elif opcode == "0xf1":
            cpu.poppsw()
        elif opcode == "0xf2":
            cpu.jp()
        elif opcode == "0xf3":
            cpu.di()
        elif opcode == "0xf4":
            cpu.cp()
        elif opcode == "0xf5":
            cpu.pushpsw()
        elif opcode == "0xf6":
            cpu.ori()
        elif opcode == "0xf7":
            cpu.rst6()
        elif opcode == "0xf8":
            cpu.rm()
        elif opcode == "0xf9":
            cpu.sphl()
        elif opcode == "0xfa":
            cpu.jm()
        elif opcode == "0xfb":
            cpu.ei()
        elif opcode == "0xfc":
            cpu.cm()
        elif opcode == "0xfe":
            cpu.cpi()
        elif opcode == "0xff":
            cpu.rst7()
        else:
            print("Invalid operation")


def main():

    try:
        with open("../tools/invaders", "rb") as f:
            buffer = f.read()
    except IOError:
        sys.exit("File not found")

    for b in buffer:
        cpu.state["memory"].append(b)

    emulate8080()


main()
