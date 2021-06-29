#���̽� cmd�� ����� ��

ENC=0
DEC=1

def parseKey(key):
    tmp=[]
    key=key.upper()
    
    for i,k in enumerate(key):
        tmp.append((i,k))
        
    tmp=sorted(tmp,key=lambda x:x[1])
    
    enc_table={}
    dec_table={}
    
    for i,r in enumerate(tmp):
        enc_table[r[0]]=i
        dec_table[i]=r[0]

    return enc_table,dec_table

def transposition(msg,key,mode):
    msgsize=len(msg)
    keysize=len(key)
    ret=''
    
    filler=" "
    if msgsize%keysize != 0:
        filler="0"*(keysize-msgsize%keysize) # msg�� �߰��� "0"
        
             
    msg=msg.upper()
    msg += filler
    
    enc_table, dec_table=parseKey(key)
    
    
    if mode == ENC:
        table = enc_table        
    else:
        table = dec_table
        
    
    if mode == ENC:
        buf =[" "]*keysize 
        for i,c in enumerate(msg):
            col =i%keysize
            index =table[col]
            buf[index] += c

        for text in buf:
            ret +=text
            
            
    else:
        blocksize= int(msgsize/keysize)
        buf =[" "]*keysize
        pos=0
        for i in range(keysize):
            text=msg[pos:pos+blocksize]
            index=table[i]
            buf[index] += text
            pos += blocksize

        for i in range(blocksize):
            for j in range(keysize):
                if buf [j][i] != "0":
                    ret += buf[j][i]

    return ret


def main():
    key ="BRAIN"
    msg="SFFZANJLTENJBEQFOAJDCKSEHFUQHO"
    print("Original:\t%s" %msg.upper())
    
    ciphertext = transposition(msg,key,ENC)
    print("Ciphertext:\t%s" %ciphertext)
     
    decophertext = transposition(ciphertext,key,DEC)
    print("Decophertext:\t%s" %decophertext)
    
if __name__=="__main__":
    main()
     
    
    



       
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    