#
#
#

import os
import time


class Token():
    
    def __init__(self):
        self.Value=None
        return
    
    def __str__(self):
        return '<%s %s >' % (self.__class__.__name__, self.Value)
    
    __repr__ = __str__
    
    def __eq__(self, o):
        #print('equal ...', self, o)
        if self.Value is not None and o.Value is not None:
            if self.Value.upper()==o.Value.upper():
                return True
        return False
    
    def __hash__(self):
        return hash(self.Value)
    pass
    
    
class Token_Null(Token):
        
    def __str__(self):
        return '<%s>' % (self.__class__.__name__)
    
   
    @classmethod
    def Parse(cls, c, tkz):
        return cls()
    
    pass
    
class Token_Symbol(Token):
    
    def __init__(self, val=None):
        self.Value = val
        return
        
    pass
    
class Token_Separator(Token_Symbol):
    
    def __init__(self, val=None):
        self.Value = val
        return
    
    pass
    
    
class Token_Identifier(Token):
    
    def __init__(self, val=None):
        self.Value = val
        return
    
    @classmethod
    def Parse(cls, c, tkz):
        s = ''
        while tkz.notEof() and(c.isalpha() or c.isnumeric() or c=='-'):
            s = s + c
            c = tkz.read()
            
        w = tkz.isWord(s)            
        if w is None:
            r = cls(s)
        else:
            r = w
            
        return r
    
    pass
    
class Token_Word(Token_Identifier):
    
    pass
    
class Token_String(Token):
    
    def __init__(self, val=None):
        self.Value=val
        return
        
    @classmethod
    def Parse(cls, c, tkz):
        
        return
    
    pass
    
class Token_Numeric(Token):
    
    def __init__(self, val=None):
        if isinstance(val, str):
            val=int(val)
        self.Value=val
        return
    
    @classmethod
    def Parse(cls, c, tkz):
        
        s=c
        while tkz.notEof():
            c = tkz.read()
            if c.isnumeric():
                s += c
            else:
                tkz.unread()
                break
                    
        return Token_Numeric(s)
    
    pass
    
    
class Token_Comment(Token):
    
    @classmethod 
    def Parse(cls, c, tkz):
        
        
        
        return
    
    
    pass
    
class Token_Eof(Token_Null):    
    pass
    
class Tokenizer():
    
    def __init__(self, src, breaklines=False, firstcol=1, lastcol=132, words=None):
        if isinstance(src, str):
            self.Source = src
        elif isinstance(src, Path):
            with open(path, "r") as fd:
                self.Source = fd.read()
        elif isinstance(src, IoStream):
            self.Source = src.read()
        else:
            raise ValueError()
        self.BreakLines=breaklines                    
        self.FirstCol=firstcol
        self.LastCol=lastcol
        self.Eof = False
        self.Bol = False
        self.Words = words
        self.ParseAll()
        return
        
        
    def ParseAll(self):
        self.PosCc=0
        self.Tokens=list()
        self.PosTt=0
        while self.notEof():
            t=self.ReadToken()
            self.Tokens.append(t)
        return
        
    def notEof(self):
        return not self.Eof
        
    def readline(self):
        if self.Eof:
            r = None
            self.PosCc=0
            self.Ll=''
        else:
            r=self.Source.readline()
            if not r:
                self.Eof=True
            else:
                r = r.strip() + ' '
                if self.LastCol is not None:
                    r = r[:self.LastCol]
            self.Ll=r
            self.PosCc=0
        return r
    
    def read(self):
        if self.notEof():
            if self.PosCc<len(self.Source):
                cc = self.Source[self.PosCc]
                self.PosCc += 1
            else:
                self.Eof=True
                cc=""
            #print('cc="', cc, '"')
            return cc
        return None
        
    def unread(self):
        if self.PosCc>0:
            self.PosCc -= 1
        return
                
    def isWord(self, w):
        if self.Words is not None:
            for e in self.Words:
                if e.Value.upper()==w.upper():
                    return e   
        return None
        
    def skipSpaces(self):
        
        cc = self.read()
        while self.notEof() and cc in (' ', '\r', '\n', '\t'):
            cc = self.read()
            time.sleep(1)
            
        return cc  
        
    def unget(self):
        if self.PosTt>0:
            self.PosTt -= 1            	    
        return
        
    def get(self):
        if self.PosTt<len(self.Tokens):
            r = self.Tokens[self.PosTt]
            self.PosTt += 1
        return 
        
    def ReadToken(self):
        if self.notEof():
            r = Token_Null()
            
            cc = self.skipSpaces()
            print('cc=', cc)
            if self.Eof:
                r = Token_Eof()
            elif cc is None:
                r = Token_Null()
            elif cc.isalpha():
                r = Token_Identifier.Parse(cc, self)
            elif cc=='-':
                cc=self.skipSpaces()
                if cc.isnumeric():
                    r = Token_Numeric.Parse('-'+cc, self)
                else:
                    self.unread()
                    r = Token_Symbol('-')
            elif cc.isnumeric():
                r = Token_Numeric.Parse(cc, self)
            elif cc=="'" or cc=='"':
                r = Token_String.Parse(cc, self)
            elif cc in (',', '.', ';', '*', '/'):
               
                r = Token_Symbol(cc)
                
            print(r)
                
        return r
        
    def Is(self, t):
        c = self.get()
        self.unget(c)
        if isinstance(t, type):
            if isinstance(c, t):
                return True
        else:
            pass
            
        return False
        
    def Expect(self, t):
        c = self.get()
        if c != t:
            raise SyntaxError('expect '+t.Value)
        return True
        
    def Next(self, *w):
        
        tt =[]
        if self.notEof():
            for e in w:
                t = self.get()
                print('Next ... ', t, '--', e)
                tt.append(t)
                if e!=t:
                    print('.... not next')
                    while len(tt)>0:
                        p = tt.pop()
                        self.unget(p)
                    return False
            return True
            
        return False
        
    
    
    pass
    
    
if __name__=='__main__':
    print('starting')
    
    words = [ Token_Word("select")]
    
    source="select a* from tablea"

    tkz=Tokenizer(source, words=words)
    
    print(tkz.Tokens)
        
        
    
    


###