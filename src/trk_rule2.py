#
# TRK RULES - 3
# 27.01.2016 ERTAN OZER
# 17.03.2018 ERTAN OZER - UPDATE
#
ek_1 =('mek','mak')
ek_2 =('ler','lar')
ek_3 =('de','da','di','dI','du','dU')
ek_4 =('ce','ca','ci','cI','cu','cU')
ek_5 =('im','Im','in','un','In')
ek_6 =('an','en')
ek_7 =('den','dan','din','dIn')
ek_8 =('miy','mIy','muy','mUy')
ek_9 =('le','la')
ek_10=('miS','mIS','muS','mUS')
ek_11=('mi','mI','mu','mU')
ek_12=('niz','nIz','nuz','nUz')
ek_13=('si','sI')
ek_14=('cek','cak')
ek_15=('dim','dIm','dum','dUm')
ek_16=('din','dIn')
ek_17=('ye','ya')
#
def post_rule_0(word):
    w=word[-3:]
    if w in ek_1:
        w0=word[:-3]
        return w0,w
    return word,''
#
def post_rule_1(word):
    e1=word[-3:]
    if e1 in ek_1:
        w1=word[:-3]
        return w1,[e1]
    if e1 in ek_2:
        w1=word[:-3]; e2=w1[-2:]
        if e2 in ek_3:
            w2=w1[:-2]
            return w2,[e2,e1]
        if e2 in ek_4:
            w2=w1[:-2]; e3=w2[-2:]
            if e3 in ek_5:
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2 in ek_6:
            w2=w1[:-2]
            return w2,[e2,e1]
        if e2=='ki':
            w2=w1[:-2]; e3=w2[-2:]
            if e3 in ek_5:
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1]
    if e1 in ek_7:
        w1=word[:-3]; e2=w1[-3:]
        if e2 in ek_8:
            w2=w1[:-3]; e3=w2[-2:]
            if e3 in ek_9:
                w3=w2[:-2]; e4=w3[-2:]
                if e4 in ek_5:
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1] 
    if e1 in ek_10:
        w1=word[:-3]; e2=w1[-3:]
        if e2 in ek_2:
            w2=w1[:-3]; e3=w2[-3:]
            if e3=='yor':
                w3=w2[:-3]; e4=w3[-2:]
                if e4 in ek_11:
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1] 
    if e1 in ek_12:
        w1=word[:-3]; e2=w1[-2:]
        if e2 in ek_13:
            w2=w1[:-2]; e3=w2[-2:]
            if e3 in ek_11:
                w3=w2[:-2]; e4=w3[-3:]
                if e4 in ek_14:
                    w4=w3[:-3]; c=w4[-1]
                    if c=='e':
                        w4=w3[:-4]
                        return w4,[c,e4,e3,e2,e1]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1]
    e1=word[-2:]
    if e1 in ek_3:
        w1=word[:-2]; e2=w1[-3:]
        if e2 in ek_8:
            w2=w1[:-3]; e3=w2[-2:]
            if e3 in ek_9:
                w3=w2[:-2]; e4=w3[-2:]
                if e4 in ek_5:
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1]
    if e1=='ki':
        w1=word[:-2]; e2=w1[-3:]
        if e2 in ek_10:
            w2=w1[:-3]
            return w2,[e2,e1]
        if e2 in ek_2:
            w2=w1[:-3]; e3=w2[-2:]
            if e3 in ek_3:
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2 in ek_15:
            w2=w1[:-3]
            return w2,[e2,e1]
        e2=w1[-2:]
        if e2 in ek_11:
            w2=w1[:-2]; e3=w2[-3:]
            if e3 in ek_2:
                w3=w2[:-3]; e4=w3[-3:]
                if e4 in ek_10:
                    w4=w3[:-3]
                    return w4,[e4,e3,e2,e1]
                if e4=='yor':
                    w4=w3[:-3]; e5=w4[-2:]
                    if e5 in ek_11:
                        w5=w4[:-2]
                        return w5,[e5,e4,e3,e2,e1]
                    return w4,[e4,e3,e2,e1]
                e4=w3[-2:]    
                if e4 in ek_3:
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            if e3 in ek_16:
                w3=w2[:-3]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2 in ek_5:
            w2=w1[:-2]
            return w2,[e2,e1]
        return w1,[e1]
    if e1 in ek_11:
        w1=word[:-2]; e2=w1[-3:]
        if e2 in ek_2:
            w2=w1[:-3]; e3=w2[-3:]
            if e3 in ek_10:
                w3=w2[:-3]
                return w3,[e3,e2,e1]
            if e3=='yor':
                w3=w2[:-3]; e4=w3[-2:]
                if e4 in ek_11:
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            if e3 in ek_14:
                w3=w2[:-3]; e4=w3[-1]
                if e4=='e':
                    w3=w2[:-4]
                    return w3,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            e3=w2[-2:]    
            if e3 in ek_3:
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='niz' or e2=='nIz':
            w2=w1[:-3]; e3=w2[-2:]
            if e3 in ek_3:
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='din' or e2=='dIn':
            w2=w1[:-3]
            return w2,[e2,e1]
        e2=w1[-2:]
        if e2 in ek_3:
            w2=w1[:-2]
            return w2,[e2,e1]
        return w1,[e1]
    if e1 in ek_4:
        w1=word[:-2]; e2=w1[-2:]
        if e2 in ek_5:
            w2=w1[:-2]
            return w2,[e2,e1]
        return w1,[e1]
    if e1 in ek_17:
        w1=word[:-2]
        return w1,[e1]
    if e1 in ek_6:
        w1=word[:-2]
        return w1,[e1]
    if e1=='um' or e1=='im':
        w1=word[:-2]; e2=w1[-4:]
        if e2=='iyor':
            w2=w1[:-5]
            c=w1[-5]
            if c=='d': c='t'
            return w2+c,[e2,e1]
        return w1,[e1]
    return word,[]
#