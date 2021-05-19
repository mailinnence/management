

def makeCodebook() :
    decbook = {'5': 'a',  '2':'b',  '#':'d',  '8':'e',  '1':'f',  '3':'g', '4':'h',  '6':'i',  'O':'1',  '9':'m',  '*': 'n',  '%':'0',  '=':'p',        '(':'r',')':'s',  ';':'t',  '?': 'u',  '@':'v',  ':' : 'y',  '7':" "}

    encbook = { }
    for k in decbook:
        val = decbook[k]
        encbook[val] = k

    return encbook, decbook

def encrypt(msg, encbook) :
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook [c])

    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook [c])

    return msg

if __name__ == "__main__":

    plaintext = "암호화시킬 문장"
    encbook, decbook = makeCodebook ()

    ciphertext= encrypt (plaintext, encbook)
    print (ciphertext)

    deciphertext = decrypt (ciphertext, decbook)
    print(deciphertext)

## 파일 입출력
##  f=open(" .txt","wt+")
##  f.write("")
##  content=f.read()
##  print(content)
