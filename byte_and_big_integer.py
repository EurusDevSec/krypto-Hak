from Crypto.Util.number import *

base10_str = '11515195063862318899931685488813747395775516287289682636499965282714637259206269'
base10_num = int(base10_str)
base10_long = long_to_bytes(base10_num)


print(base10_long)