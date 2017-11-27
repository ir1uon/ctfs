
import string
import codecs


pswd = "zf760ow4l4X407}4bX;X~3w7~|T@WO@"
flag = ""
plen = len(pswd)

for i in pswd:
	t= chr(ord(i) ^ 0x7)
	flag += codecs.encode(t,'rot_13')

print flag[::-1]