#
# HECE ALGO ( TURKCE )
# ------------------------------
# Ertan OZER (c) 
# Python adaptation - 23.01.2016
# Corrections       - 24.01.2016
#
sesli="aeiIuUoO"
sessiz="bcCdfgGhjklmnprstyz"
endc=',;.'
#
def code(c):
    if c in sessiz: return 1
    if c in sesli : return 2
    if c in endc  : return 0
    else          : return 3 # error

def code1(p):
    if p=='': return 0
    #print ">",p
    k=code(p[0])
    if k==0: return 0
    if k==1:  # [0 
        k=code(p[1])
        if k==0: return -1 # [0]
        if k==1: # [00 
            k=code(p[2])
            if k==0: return -1 # [00]  # 1 ???    
            if k==1: return -1 # [000
            if k==2: # [001 
                k=code(p[3])
                if k==0: return -1 # [001] # 9 ???
                if k==1: # [0010
                    k=code(p[4]) 
                    if k==0: return  7 # [0010]
                    if k==1: return  7 # [00100
                    if k==2: return  9 # [00101
                    if k==3: return -1 # [0010?
                if k==2: return  0 # [0011
                if k==3: return -1 # [001?
            if k==3: return -1     # [002
        if k==2: # [01
            k=code(p[2]) 
            if k==0:  return 2 # [01]
            if k==1: # [010
                k=code(p[3]) 
                if k==0: return 3 # [010]
                if k==1: # 0100
                    k=code(p[4])
                    if k==0:  return  8 # [0100]
                    if k==1:  return -1 # [01000 # 8 ??? 
                    if k==2:  return  3 # [01001
                    if k==3:  return -1 # [0100?
                if k==2: return  2      # [0101
                if k==3: return -1      # [010?
            if k==2: return  2 # [011
            if k==3: return -1 # [01?
        if k==3:     return -1 # [0?
    if k==2:  # [1
        k=code(p[1])
        if k==0: return 4 # [1]
        if k==1: # [10 
            k=code(p[2])
            if k==0: return 5 # [10] 
            if k==1: # [100
                k=code(p[3])
                if k==0: return  6 # [100]
                if k==1: return -1 # [1000
                if k==2: return  5 # [1001
                if k==3: return -1 # [100?
            if k==2: return  4     # [101
            if k==3: return -1     # [10?
        if k==2: return  4 # [11
        if k==3: return -1 # [1?
    if k==3: return -1 # [?

def code2(p,n):
    c=code1(p)
    if   c==0 or c==-1: # -
        return 0
    elif c==1: # 00
        if n==0:
            n=1; p=p[2:]
    elif c==2: # 01
        if n==0 or n==2 or n==3 or n==4 or n==5 or n==7 or n==8 or n==9: 
            n=2; p=p[2:]
    elif c==3: # 010
        if n==0 or n==2 or n==3 or n==4 or n==5 or n==7 or n==8 or n==9: 
            n=3; p=p[3:]
    elif c==4: # 1
        if n==0 or n==2 or n==4 or n==5:  
            n=4; p=p[1:]
    elif c==5: # 10
        if n==0 or n==4 or n==2: 
            n=5; p=p[2:]
        elif n==1: 
            n=7; p=p[2:]
    elif c==6: # 100
        if n==0 or n==2: 
            n=6; p=p[3:]
    elif c==7: # 0010
        if n==0: 
            n=7; p=p[4:]
    elif c==8: # 0100
        if n==0 or n==2 or n==3 or n==5: 
            n=8; p=p[4:]
    elif c==9: # 001
        if n==0: 
            n=9; p=p[3:]
    return n

def code3(p):
    cod=[]; n=0
    while 1:
        c=code1(p)
        cod.append(c)
        if c==0 or c==-1: # -    */
            break
        elif c==1: # 00   */
            if n==0:
                n=1; p=p[2:]; continue
            break;
        elif c==2: # 01   */
            if n==0 or n==2 or n==3 or n==4 or n==5 or n==7 or n==8 or n==9: 
                n=2; p=p[2:]; continue
            break
        elif c==3: # 010  */
            if n==0 or n==2 or n==3 or n==4 or n==5 or n==7 or n==8 or n==9: 
                n=3; p=p[3:]; continue
            break
        elif c==4: # 1    */
            if n==0 or n==2 or n==4 or n==5:  
                n=4; p=p[1:]; continue
            break
        elif c==5: # 10   */
            if n==0 or n==4 or n==2: 
                n=5; p=p[2:]; continue
            elif n==1: 
                n=7; p=p[2:]; continue
            break
        elif c==6: # 100  */
            if n==0 or n==2: 
                n=6; p=p[3:]; continue
            break
        elif c==7: # 0010 */
            if n==0: 
                n=7; p=p[4:]; continue
            break
        elif c==8: # 0100 */
            if n==0 or n==2 or n==3 or n==5: 
                n=8; p=p[4:]; continue
            break
        elif c==9: # 001 */
            if n==0: 
                n=9; p=p[3:]; continue
            break
        else: 
            break
        #
    return cod

def code4(p):
    n=o=0
    while 1:
        c=code1(p)
        if c==-1:
            return 1
        if c==0: # -    */
            if o==0 and n==1: return 1
            break
        elif c==1: # 00   */
            if n==0:
                o=n; n=1; p=p[2:]; continue
            break;
        elif c==2: # 01   */
            if n==0 or n==2 or n==3 or n==4 or n==5 or n==7 or n==8 or n==9: 
                o=n; n=2; p=p[2:]; continue
            break
        elif c==3: # 010  */
            if n==0 or n==2 or n==3 or n==4 or n==5 or n==7 or n==8 or n==9: 
                o=n; n=3; p=p[3:]; continue
            break
        elif c==4: # 1    */
            if n==0 or n==2 or n==4 or n==5:  
                o=n; n=4; p=p[1:]; continue
            break
        elif c==5: # 10   */
            if o==0 and n==4: return 1 
            if n==0 or n==4 or n==2:
                o=n; n=5; p=p[2:]; continue
            elif n==1: 
                o=n; n=7; p=p[2:]; continue
            break
        elif c==6: # 100  */
            if n==0 or n==2: 
                o=n; n=6; p=p[3:]; continue
            break
        elif c==7: # 0010 */
            if n==0: 
                o=n; n=7; p=p[4:]; continue
            break
        elif c==8: # 0100 */
            if n==0 or n==2 or n==3 or n==5: 
                o=n; n=8; p=p[4:]; continue
            break
        elif c==9: # 001 */
            if n==0: 
                o=n; n=9; p=p[3:]; continue
            elif n==7: return 1
            break    
        else: 
            break
        #
    return 0

def hece(w):
    s=[]; n=0
    for _ in range(len(w)):
        n=code2(w,n)
        if   n==0: break
        if   n==8 or n==7:         i=4 # XXXX */
        elif n==9 or n==6 or n==3: i=3 # XXX  */
        elif n==1 or n==2 or n==5: i=2 # XX   */
        elif n==4:                 i=1 # X    */
        else:                      i=0
        s.append(w[:i])
        w=w[i:]
    return s

def kodla(s):
    kod=[]
    for i in range(len(s)):
        c=s[i]
        if   c in sessiz: kod.append(0)
        elif c in sesli : kod.append(1)
        elif c in endc  : kod.append(2)
        else:             kod.append(3)
    return kod
#
#print(hece("aldIlarmIki."))
#print(hece("trendekilermiki."))
#print(hece("ertan."))
print(hece("memleketimdenmisinki."))
