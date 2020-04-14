from pwn import *
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs

conn = remote('socket.cryptohack.org', 13377, level = 'debug')
for i in range(100):
    str = conn.recvline()
    js = eval(str)
    #print("The encryption is " + js['type'] + ' and the str is')  
    #print(js['encoded'])
    dict = {'decoded' : null}
    if(js['type'] == 'base64'): dict['decoded'] = base64.b64decode(js['encoded'])
    elif(js['type'] =='hex'): dict['decoded'] = js['encoded'].decode('hex')
    elif(js['type'] =='rot13'): dict['decoded'] = codecs.decode(js['encoded'], 'rot_13')
    elif(js['type'] =='bigint'): dict['decoded'] = (js['encoded'][2:].decode('hex'))
    else: 
        new = '' 
        dict['decoded'] = [chr(b) for b in js['encoded']]
        for x in dict['decoded']: new += x 
        dict['decoded'] = new
    #print('The decrypted string is ')
    #print(dict['decoded'])
    request = json.dumps(dict).encode()
    conn.sendline(request)
conn.recvline()
conn.close()