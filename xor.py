import random


enc_msg = "sifrelenecek metin "
xor_msg = ""

encryption_level = 128 // 8#anahtar uzunluğunu belirleme
key_char_pool = ''
for i in range(0x00, 0xFF): #karekter havuzu oluşturma
    key_char_pool += chr(i)
len_key_char_pool = len(key_char_pool)

#key oluşturma
key = ''
for i in range(encryption_level):
    key += key_char_pool[random.randint(0,len_key_char_pool)]

key_index = 0
max_key_index = encryption_level-1
#encryption
for c in enc_msg:
    xor_char = ord(c) ^ ord(key[key_index])
    xor_msg += chr(xor_char)

    if key_index == max_key_index:
        key_index=0
    else:
        key_index += 1

#decryption
key_index = 0
dcrp_msg = ""
for c in xor_msg:
    dxor_char = ord(c) ^ ord(key[key_index])
    dcrp_msg += chr(dxor_char)

    if key_index == max_key_index:
        key_index = 0
    else:
        key_index += 1



print(enc_msg,xor_msg,dcrp_msg,sep="\n")
