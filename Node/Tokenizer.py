#
#
#

import os
import time

from Io import DEBUG

class Token():
    
    def __init__(self):
        self.Value=None
        return
    
    def __str__(self):
        return '<%s %s >' % (self.__class__.__name__, self.Value)
    
    __repr__ = __str__
    
    def __eq__(self, o):
        DEBUG.TOKEN.EQUAL(self, "=", o)
        if o is None:
            return False
        elif isinstance(o, str):
             if isinstance(self.Value, str):
                 if self.Value.upper()==o.upper():
                    return True
        elif self.Value is not None and o.Value is not None:
            if self.Value.upper()==o.Value.upper():
                return True
        return False
    
    def __hash__(self):
        return hash(self.Value)
        
    @classmethod 
    def Dropable(cls):
        return False
        
    @classmethod 
    def Check(cls, tkz):
        return False
        
    @classmethod 
    def Parse(cls, tkz):
        return None
        
    pass
    
    
class Token_Null(Token):
        
    def __str__(self):
        return '<%s>' % (self.__class__.__name__)
    
   
    @classmethod
    def Parse(cls, tkz):
        return cls()
    
    pass
    
class Token_Symbol(Token):
    
    def __init__(self, val=None):
        self.Value = val
        return
        
    _SymbolChars = "_+/@#$%^&*():;!?,.~\|<>{}[]" 
                
    @classmethod 
    def Check(cls, tkz):
        if not tkz._Eof:
            cc=tkz.read()
            tkz.unread()
            if not tkz._Eof and cc in cls._SymbolChars:
                return True
                
        return False
        
        
    @classmethod 
    def Parse(cls, tkz):
        if cls.Check(tkz):
            s=tkz.read()
            return cls(s)            
            
        return None
        
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
    def Check(cls, tkz):
        if not tkz._Eof:
            cc=tkz.read()
            tkz.unread()
            if not tkz._Eof and (cc.isalpha() or cc=="_"):
                return True
        return False
        
    @classmethod
    def Parse(cls, tkz):
        if cls.Check(tkz):
            s = ''
            c=tkz.read()
            while not tkz._Eof and(c.isalpha() or c.isnumeric() or c=='-'):
                s = s + c
                c = tkz.read()
            tkz.unread()
            
            return Token_Identifier(s)
                  
        return None
   
    
    pass
    
class Token_Word(Token_Identifier):
        
    @classmethod
    def Parse(cls, tkz):
        s=super().Parse(tkz)
        if s is not None:
                  
            w = tkz.isWord(s.Value)            
            if w is not None:
                r = w
            else:
                r = s
            
            return r
            
        return None
        
    def __eq__(self, s):
        if isinstance(s, str):
            return self.Value.upper()==s.upper()
        elif isinstance(s, (Token_Word, Token_Identifier)):
            return self.Value.upper()==s.Value.upper()
        return False
        
        
    pass
    
class Token_String(Token):
    
    def __init__(self, val=None):
        self.Value=val
        return
        
    @classmethod 
    def Check(cls, tkz):
        if not tkz._Eof:
            cc=tkz.read()
            tkz.unread()
            if cc=="'" or cc=='"':
                return True
        return False
        
        
    @classmethod
    def Parse(cls, tkz):
        if cls.Check(tkx):
            dl=tkz.read()
            c=tkz.read()        
            while not tkz._Eof() and c!=dl:
                s += c
                c=tkz.read()
                
            return Token_Strinf(s)
            
        return None
    
    pass
    
class Token_Numeric(Token):
    
    def __init__(self, val=None):
        if isinstance(val, str):
            val=int(val)
        self.Value=val
        return
        
    _NumericChars = ".0123456789"
    
    @classmethod 
    def Check(cls, tkz):
        if not tkz._Eof:
            cc=tkz.read()
            tkz.unread()
            if not tkz._Eof and cc in cls._NumericChars:
               return True 
            
        return False
    
    @classmethod
    def Parse(cls, tkz):
        if cls.Check(tkz):
            s=""
            while not tkz._Eof:
                c = tkz.read()
                if c.isnumeric() or (c=="." and not c in s):
                    s += c
                else:
                    tkz.unread()
                    break                    
                    
            return Token_Numeric(s)
            
        return None
    
    pass
    
    
class Token_Comment(Token):
    
    @classmethod 
    def Parse(cls, c, tkz):
        
        
        
        return
    
    
    pass
    
class Token_Eof(Token_Null): 

    @classmethod 
    def Check(cls, tkz):
        if tkz._Eof:
            return True
        return False
        
    @classmethod 
    def Parse(cls, tkz):
        return cls()
        
    pass
    
class Token_Space(Token_Null):
    
    _SpaceChars = (' ', '\r', '\n', '\t')
    
    @classmethod 
    def Dropable(cls):
        return True
    
    @classmethod 
    def Check(cls, tkz):
        if not tkz._Eof:
            cc = tkz.read()
            tkz.unread()
            if not tkz._Eof and cc in cls._SpaceChars:
                return True
        return False
        
    @classmethod 
    def Parse(cls, tkz):
        if cls.Check(tkz):
            cc = tkz.read()
            while not tkz._Eof and cc in cls._SpaceChars:
                #DEBUG.TOKENSPAGES()
                cc = tkz.read()
            tkz.unread()
            return cls()
        return None
    
    
    pass
    
class TokenizerStream():
        
        def __init__(self, src, breaklines=False, firstcol=1, lastcol=132, words=None, symbols=None):
            if isinstance(src, str):
                self._Source = src
            elif isinstance(src, Path):
                with open(path, "r") as fd:
                    self._Source = fd.read()
            elif isinstance(src, IoStream):
                self._Source = src.read()
            else:
                raise ValueError()
            self._BreakLines=breaklines                    
            self._FirstCol=firstcol
            self._LastCol=lastcol
            self._Eof = False
            self._Bol = False
            self._Words = words
            self._Symbols=symbols
            return
            
        def ParseAll(self):
            self._PosCc=0
            tt=list()
            while not self._Eof:
                t=self.ReadToken()
                tt.append(t)
            return tt
               
        def read(self):
            if not self._Eof:
                if self._PosCc<len(self._Source):
                    cc = self._Source[self._PosCc]
                    self._PosCc += 1
                else:
                    self._Eof=True
                    cc=""
                #print('cc="', cc, '"')
                return cc
            return None
        
        def unread(self):
            if self._PosCc>0:
                self._PosCc -= 1
            return
            
        def readline(self):
            if self._Eof:
                r = None
                self.PosCc=0
                self.Ll=''
            else:
                r=self.Source.readline()
                if not r:
                    self._Eof=True
                else:
                    r = r.strip() + ' '
                    if self.LastCol is not None:
                        r = r[:self.LastCol]
                self.Ll=r
                self.PosCc=0
            return r
            
        _TokenTypes = (
    	              Token_Eof,
    	              Token_Null,
    	              Token_Space,
    	              Token_Numeric,
    	              Token_String,
    	              Token_Word,
    	              Token_Identifier,
    	              Token_Symbol,
    	              Token_Separator,
    	             )
        
        def ReadToken(self):
            if not self._Eof:
                r = None           
            
                while not self._Eof:
                    for fn in self._TokenTypes:
                        #DEBUG.READTOKEN(fn) 
                        if fn.Check(self):
                            r=fn.Parse(self)
                            #DEBUG.READTOKEN("--", r.Dropable())
                            if r.Dropable():
                                continue
                            break
                    if r is not None:
                        break
                    
                print(r)
                
            return r
            
        def isWord(self, w):
            if self._Words is not None:
                w=w.upper()
                for e in self._Words:
                    if isinstance(e, str):
                        if e.upper()==w:
                            return Token_Word(e)
                    elif isinstance(e, Token):
                        if e.Value.upper()==w:
                            return e   
            return None
        
        def isSymbol(self, w):
            if self._Symbols is not None:
                w=w.upper()
                for e in self._Symbols:
                    if isinstance(e, str):
                        if e.upper()==w:
                            return Token_Symbol(e)
                    elif isinstance(e, Token):
                        if e.Value.upper()==w:
                            return e   
            return None   
            
            
        pass    
    
class Tokenizer():
    
    Token = Token
    Identifier = Token_Identifier 
    Word = Token_Word
    String = Token_String
    Numeric = Token_Numeric
    Symbol = Token_Symbol
    Separator = Token_Separator
    
    @classmethod 
    def From(cls, s, words=None, symbols=None):
        if not isinstance(s, Tokenizer):
            s=Tokenizer(s, words=words, symbols=symbols)
        return s    
    
    def __init__(self, src, breaklines=False, firstcol=1, lastcol=132, words=None, symbols=None):
        sm=TokenizerStream(src, breaklines, firstcol, lastcol, words, symbols)
        self._Tokens=sm.ParseAll()
        self._PosTt=0
        return
                    
    def __str__(self):       
        return str(self._Tokens[self._PosTt:]) 
              
    def unget(self):
        if self._PosTt>0:
            self._PosTt -= 1            	    
        return
        
    @property 
    def isEot(self):
        return self._PosTt>=len(self._Tokens)
        
    @property 
    def isNotEot(self):
        return self._PosTt<len(self._Tokens)
        
    def get(self):
        #DEBUG.POSTT(self.PosTt)
        if self.isNotEot:
            r = self._Tokens[self._PosTt]
            self._PosTt += 1
            return r
        return None
        
    
    def Is(self, t):
        c = self.get()
        self.unget()
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
        
    def ExpectIdentifier(self):
        c=self.get()
        if isinstance(c, Token_Identifier):
            return c
        raise SyntaxError("expect identifier")
        return None
        
    def Next(self, *w):
        if self.isNotEot:
            t = self.get()
            if len(w)>0:
                for e in w:              
                    DEBUG.NEXT(t, '--', e)
                    if e==t:
                        return e                    
                self.unget()
            else:
                return t
                
        return False
        
    def isString(self):
        t=self.get()
        self.unget()
        return isinstance(t, Token_String)
    
    def isNumeric(self):
        t=self.get()
        self.unget()
        return isinstance(t, Token_Numeric)
        
    def isWord(self):
        t=self.get()
        self.unget()
        return isinstance(t, Token_Word)
        
    def isIdentifier(self):
        t=self.get()
        self.unget()
        return isinstance(t, Token_Identifier)
        
    def isSymbol(self):
        t=self.get()
        self.unget()
        return isinstance(t, Token_Symbol)
   
    pass
    
    
if __name__=='__main__':
    print('starting')
    
    words = [ Token_Word("select"), "From"]
    
    source="+ select a* from tablea"

    tkz=Tokenizer(source, words=words)
    
    if tkz.Next("+"):
        print("ok")
    
    print(str(tkz))
        
    t=tkz.Next("select")
        
    
    


###