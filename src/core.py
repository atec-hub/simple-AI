#from trk_hece import hece
from trk_rule import post_rule_1
from data import data
#
class SEGMENT:
    back=None
    next=None
    name=None
    scop1={}
    scop2={}
    scop3={}
    indk1={}
#
class CORE(object):
    root=SEGMENT
    def __init__(self):
        self.segment=self.root
        self.word=''
        self.sentence=''
        self.ques=''
        self.answer=''
        self.w=0 # word len
        self.s=0 # sentence len

    def clr(self):
        self.root.back=None
        self.root.next=None
        self.root.name=None
        self.root.scop1={}
        self.root.scop2={}
        self.root.scop3={}
        self.root.indk1={}

    def new(self,ref):
        if ref:
            segment=SEGMENT
            segment.name=ref
            segment.back=self.segment
            self.segment.next=segment
            self.segment=segment
            return segment
        return None

    def set(self,a):
        self.segment.indk1[a]=1
    def get(self,a):
        try:    return self.segment.indk1[a]
        except: return 0

    def set_scop1(self,a,b):
        self.segment.scop1[a]=b
    def set_scop2(self,a,b):
        self.segment.scop2[a]=b
    def set_scop3(self,a,b):
        self.segment.scop3[a]=b
    
    def get_scop1(self,a):
        try:    return self.segment.scop1[a]
        except: return None
    def get_scop2(self,a):
        try:    return self.segment.scop2[a]
        except: return None
    def get_scop3(self,a):
        try:
            w=self.segment.scop3[a]
            try: 
                [k,p]=w
                return [k,''.join([_ for _ in p]),p[-1]]
            except:
                return [w,'','']
        except: 
            return ['','','']
        
    def parse(self,sentence,len_):
        if len_:
            f,b=1,0
            for i in range(len_):
                c=sentence[i]
                if f:
                    if c==' ' or c==',' or c==';' or c=='.' or c=='?' or c=='!':
                        continue
                    f,b=0,i
                else:
                    if c==' ' or c==',' or c==';' or c=='.' or c=='?' or c=='!':
                        if   c=='.': self.set('end')
                        elif c=='?': self.set('soru') 
                        i-=1; break
            if f:
                return '',0
            j=i+1
            self.w=j-b
            self.s=len_-j
            self.word=sentence[b:j]
            self.sentence=sentence[j:]
            return self.word,self.sentence,self.w,self.s
        return '','',0,0

    def next(self):
        if self.s:
            f,b=1,0
            for i in range(self.s):
                c=self.sentence[i]
                if f:
                    if c==' ' or c==',' or c==';' or c=='.' or c=='?' or c=='!':
                        continue
                    f,b=0,i
                else:
                    if c==' ' or c==',' or c==';' or c=='.' or c=='?' or c=='!':
                        if   c=='.': self.set('son')
                        elif c=='?': self.set('soru'); self.set('son') 
                        i-=1; break
            if f:
                return '',0
            j=i+1
            self.w=j-b
            self.s=self.s-j
            self.word=self.sentence[b:j]
            self.sentence=self.sentence[j:]
            return self.word,self.w
        return '',0

    def think1(self,sentence):
        wo,se,w,s=self.parse(sentence,len(sentence))
        #print "[%s]-[%s]"%(wo,se),w,s
        while w:
            #print "[%s]"%wo,w
            if wo in ['ben','sen','o','biz','siz','onlar']:
                self.set_scop2('kim',wo)
            elif wo in ['beni','seni','onu','bizi','sizi','onlari']:
                self.set_scop2('kimi',wo)
            elif wo in ['bana','sana','ona','bize','size','onlara']:
                self.set_scop2('kime',wo)
            elif wo in ['benim','senin','onun']:
                self.set_scop2('kimin',wo)
            elif wo in ['az','cok']:
                self.set_scop2('nekadar',wo)
            elif wo in ['bu','su','o']:
                self.set_scop2('hangisi',wo)
            elif wo in ['zor','kolay']:
                self.set_scop2('nasil',wo)
            elif wo in data['soru']:
                self.set('soru')
                self.set_scop3('soru',wo)
            else:
                ko,po=post_rule_1(wo); 
                if po: p0=po[0]
                else:  p0=''
                #print ko,po
                if ko=='on' and p0=='lar':
                    self.set_scop2('kim','onlar')
                    if po[-1]=='mi':
                        self.set('soru')
                elif ko=='ad' and p0=='im':
                    self.set_scop1('ben','???')
                elif ko=='es' and p0=='im':
                    self.set_scop2('kim',wo)
                    self.set_scop1('es','???')
                elif ko in data['fiil_kok']:
                    self.set_scop3('fiil',[ko,po])
                elif ko in data['sayi']:
                    self.set_scop3('sayi',[ko,po])
                else:
                    self.set_scop3('???',[ko,po])
            wo,w=core.next()

    def think2(self):
        [k,p,e]=self.get_scop3('fiil')
        if self.get_scop2('kim') is None:
            if e=='um':
                self.set_scop2('kim','ben')
            elif e=='di':
                [k2,_,_]=self.get_scop3('soru')
                if k2=='kimler': self.set_scop2('kim','onlar')
                else:            self.set_scop2('kim','o')
            elif p=='dimi' or p=='dImI':
                self.set_scop2('kim','o')
                self.set('soru')
            elif p=='dilermi' or p=='dIlarmI':
                self.set_scop2('kim','onlar')
                self.set('soru')
            elif e=='ler':
                self.set_scop2('kim','onlar')
        else:
            if e=='mi':
                self.set('soru')
        
        w=self.get_scop2('ne')
        if w is None:
            if e=='im':
                self.set_scop2('ne',k)
        elif w in ['bu','su','o','bunlar','sunlar','onlar']:
            if e=='im':
                self.set_scop2('nedir',k)

        w=self.get_scop1('ben')
        if w=='???':
            [k,p,e]=self.get_scop3('???')
            if k: self.set_scop1('ben',k+p)
 
        w=self.get_scop1('es')
        if w=='???':
            w=self.get_scop2('hangisi')
            if w in ['bu','su','o']:
                self.set_scop1('es',w)

    def think(self,sentence):
        self.think1(sentence)
        self.think2()

    def ques(self):
        scop=self.segment.scop2
        for a in scop:
            b=scop[a]
            if b=='':
                if a=='kimi':
                    try:    k=scop['kim']
                    except: k=''
                    if k=='':
                        self.ques=''

    def word(self):
        self.word

    def segment(self):
        return self.segment
#
core=CORE()
#