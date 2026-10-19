#
# TRK RULES - 3
# 27.01.2016 ERTAN OZER
#
def post_rule_0(word):
    w=word[-3:]
    if w=='mek' or w=='mak':
        w0=word[:-3]
        return w0,w
    return word,''
#
def post_rule_1(word):
    e1=word[-3:]
    if e1=='mek' or e1=='mak':
        w1=word[:-3]
        return w1,[e1]
    if e1=='ler' or e1=='lar':
        w1=word[:-3]; e2=w1[-2:]
        if e2=='de' or e2=='da' or e2=='di' or e2=='dI' or e2=='du' or e2=='dU':
            w2=w1[:-2]
            return w2,[e2,e1]
        if e2=='ce' or e2=='ca' or e2=='ci' or e2=='cI' or e2=='cu' or e2=='cU':
            w2=w1[:-2]; e3=w2[-2:]
            if e3=='im' or e3=='in' or e3=='un' or e3=='In':
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='an' or e2=='en':
            w2=w1[:-2]
            return w2,[e2,e1]
        if e2=='ki':
            w2=w1[:-2]; e3=w2[-2:]
            if e3=='im' or e3=='in' or e3=='un' or e3=='In':
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1]
    if e1=='den' or e1=='dan' or e1=='din' or e1=='dIn':
        w1=word[:-3]; e2=w1[-3:]
        if e2=='miy' or e2=='mIy' or e2=='muy' or e2=='mUy':
            w2=w1[:-3]; e3=w2[-2:]
            if e3=='le' or e3=='la':
                w3=w2[:-2]; e4=w3[-2:]
                if e4=='im' or e4=='in' or e4=='un' or e4=='In':
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1] 
    if e1=='miS' or e1=='mIS' or e1=='muS' or e1=='mUS':
        w1=word[:-3]; e2=w1[-3:]
        if e2=='ler' or e2=='lar':
            w2=w1[:-3]; e3=w2[-3:]
            if e3=='yor':
                w3=w2[:-3]; e4=w3[-2:]
                if e4=='mi' or e4=='mI' or e4=='mu' or e4=='mU':
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1] 
    if e1=='niz' or e1=='nIz' or e1=='nuz':
        w1=word[:-3]; e2=w1[-2:]
        if e2=='si' or e2=='sI':
            w2=w1[:-2]; e3=w2[-2:]
            if e3=='mi' or e3=='mI' or e3=='mu' or e3=='mU':
                w3=w2[:-2]; e4=w3[-3:]
                if e4=='cek' or e4=='cak':
                    w4=w3[:-3]; c=w4[-1]
                    if c=='e':
                        w4=w3[:-4]
                        return w4,[c,e4,e3,e2,e1]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1]
    e1=word[-2:]
    if e1=='de' or e1=='da' or e1=='di' or e1=='dI' or e1=='du' or e1=='dU':
        w1=word[:-2]; e2=w1[-3:]
        if e2=='miy' or e2=='mIy' or e2=='muy' or e2=='mUy':
            w2=w1[:-3]; e3=w2[-2:]
            if e3=='le' or e3=='la':
                w3=w2[:-2]; e4=w3[-2:]
                if e4=='im' or e4=='in' or e4=='un' or e4=='In':
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        return w1,[e1]
    if e1=='ki':
        w1=word[:-2]; e2=w1[-3:]
        if e2=='miS' or e2=='mIS' or e2=='muS' or e2=='mUS':
            w2=w1[:-3]
            return w2,[e2,e1]
        if e2=='ler' or e2=='lar':
            w2=w1[:-3]; e3=w2[-2:]
            if e3=='di' or e3=='dI' or e3=='du' or e3=='dU':
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='dim' or e2=='dIm' or e2=='dum' or e2=='dUm':
            w2=w1[:-3]
            return w2,[e2,e1]
        e2=w1[-2:]
        if e2=='mi' or e2=='mI' or e2=='mu' or e2=='mU':
            w2=w1[:-2]; e3=w2[-3:]
            if e3=='ler' or e3=='lar':
                w3=w2[:-3]; e4=w3[-3:]
                if e4=='miS' or e4=='mIS' or e4=='muS' or e4=='mUS':
                    w4=w3[:-3]
                    return w4,[e4,e3,e2,e1]
                if e4=='yor':
                    w4=w3[:-3]; e5=w4[-2:]
                    if e5=='mi' or e5=='mI' or e5=='mu' or e5=='mU':
                        w5=w4[:-2]
                        return w5,[e5,e4,e3,e2,e1]
                    return w4,[e4,e3,e2,e1]
                e4=w3[-2:]    
                if e4=='de' or e4=='da' or e4=='di' or e4=='dI' or e4=='du' or e4=='dU':
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            if e3=='din' or e3=='dIn':
                w3=w2[:-3];
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='im' or e2=='Im':
            w2=w1[:-2];
            return w2,[e2,e1]
        if e2=='in' or e2=='un' or e2=='In':
            w2=w1[:-2];
            return w2,[e2,e1]
        return w1,[e1]
    if e1=='mi' or e1=='mI' or e1=='mu' or e1=='mU':
        w1=word[:-2]; e2=w1[-3:]
        if e2=='ler' or e2=='lar':
            w2=w1[:-3]; e3=w2[-3:]
            if e3=='miS' or e3=='mIS' or e3=='muS' or e3=='mUS':
                w3=w2[:-3]
                return w3,[e3,e2,e1]
            if e3=='yor':
                w3=w2[:-3]; e4=w3[-2:]
                if e4=='mi' or e4=='mI' or e4=='mu' or e4=='mU':
                    w4=w3[:-2]
                    return w4,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            if e3=='cek' or e3=='cak':
                w3=w2[:-3]; e4=w3[-1]
                if e4=='e':
                    w3=w2[:-4]
                    return w3,[e4,e3,e2,e1]
                return w3,[e3,e2,e1]
            e3=w2[-2:]    
            if e3=='de' or e3=='da' or e3=='di' or e3=='dI' or e3=='du' or e3=='dU':
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='niz' or e2=='nIz':
            w2=w1[:-3]; e3=w2[-2:]
            if e3=='de' or e3=='da' or e3=='di' or e3=='dI' or e3=='du' or e3=='dU':
                w3=w2[:-2]
                return w3,[e3,e2,e1]
            return w2,[e2,e1]
        if e2=='din' or e2=='dIn':
            w2=w1[:-3]
            return w2,[e2,e1]
        e2=w1[-2:]
        if e2=='de' or e2=='da' or e2=='di' or e2=='dI' or e2=='du' or e2=='dU':
            w2=w1[:-2]
            return w2,[e2,e1]
        return w1,[e1]
    if e1=='ce' or e1=='ca' or e1=='ci' or e1=='cI' or e1=='cu' or e1=='cU':
        w1=word[:-2]; e2=w1[-2:]
        if e2=='im' or e2=='in' or e2=='un' or e2=='In':
            w2=w1[:-2]
            return w2,[e2,e1]
        return w1,[e1]
    if e1=='ye' or e1=='ya':
        w1=word[:-2]
        return w1,[e1]
    if e1=='an' or e1=='en':
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