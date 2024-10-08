import random
dic = {0:"0",1:"1",2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

# negate bits in ASCII hexadecimal value
def random_int():
    r1 = random.randint(0,7)
    r2 = random.randint(0,7)
    while r1 == r2:
        r2 = random.randint(0, 7)
    return [r1,r2]

# add before and after cryptogram usless characters and return it
def add_garbage(x):
    text=""
    front = random.randint(2,15)
    back = random.randint(2,15)
    for i in range(front):
        if i == 1:
            text+=dic[front]
            continue
        r = random.randint(0,15)
        text+=dic[r]

    text += str(x)
    for i in range(back):
        if i == (back-2):
            text+=dic[back]
            continue
        r = random.randint(0,15)
        text+=dic[r]

    print(str(front)+" "+str(back))
#    print(text)
    return text

# convert and negate bits
def bin_hex(bin_str,rand):
    bin_str=bin_str[::-1]
    pot=0
    value=0
    char = ""
    for i in bin_str:
        if i == "1":
            value+=2**pot
        pot+=1
    hex_str = hex(value)
    hex_str = hex_str[2:].upper()
    hex_str = hex_str.zfill(2)
    char+=str(rand[0])
    char += str(rand[1])
    char+=hex_str
    return char

# reverse binary string of ASCII value
def swap(rev,val):
    iterator=0
    result = ""
    for i in rev:
        if iterator == val:
            if i == "0":
                result+="1"
            elif i == "1":
                result+="0"
        else:
            result+=i
        iterator+=1
    return result

def encrypt(text):
    cryptogram = ""
    for i in text:
#        print(i + " In ASCII DEC= " + str(ord(i)))
        dec = str(ord(i))   #zamiana na postać decymalna w ASCII
        b1 = bin(int(dec))  #zamiana na postac binarna
        str(b1)
        b1 = b1[2:]
        b1 = b1.zfill(8)
#        print(b1)
        rev = b1[::-1]      #odwocenie ciagu
#        print("Reverse: " + rev)

        val = random_int()  #losowanie pozycji do zmiany
#        print("wylosowane: " + str(val))
        r1 = swap(rev, val[0])  #negacja bitu
        r2 = swap(r1,val[1])    #negacja bitu
#        print("Final: "+r2)
        bin_hex(r2,val)         #zamiana bin na hex
        cryptogram+=bin_hex(r2,val)
#    print("crypt: "+cryptogram)
    cryptogram = add_garbage(cryptogram)
    return cryptogram