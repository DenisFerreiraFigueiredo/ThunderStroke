#
#
# Object Quary Language
import sys
import os

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)
    
from Node import Words as _w

_w.Count = _w._i("Count")
_w.Sum = _w._i("Sum")
_w.Average = _w._i("Average")
_w.Avg = _w._i("Avg")    
_w.Max = _w._i("Max")    
_w.Min = _w._i("Min")
_w.Select = _w._i("Select")
_w.Update = _w._i("Update")
_w.Insert = _w._i("Insert")
_w.From = _w._i("From")
_w.Delete = _w._i("Delete")
_w.Where = _w._i("Where")
_w.Order = _w._i("Order")
_w.Limit = _w._i("Limit")
_w.Boolean = _w._i("Boolean")
_w.Create = _w._i("Create")
_w.Alter = _w._i("Alter")
_w.Output = _w._i("Output")
_w.Input = _w._i("Input")
_w.Explain = _w._i("Explain")
_w.Table = _w._i("Table")
_w.Collection = _w._i("Collection")
_w.Database = _w._i("Database")
_w.Catalog = _w._i("Catalog")
_w.View = _w._i("View")
_w.Drop = _w._i("Drop")
_w.By = _w._i("By")
_w.Having = _w._i("Having")
_w.Distinct = _w._i("Distinct")
_w.Top = _w._i("Top")
_w.Botton = _w._i("Botton")
_w.All = _w._i("All")    
_w.First = _w._i("First")
_w.Last = _w._i("Last")
_w.Into = _w._i("Into")
_w.Strict = _w._i("Strict")    
_w.Above = _w._i("Above")    
_w.Below = _w._i("Below")    
_w.Union = _w._i("Union")    
_w.Difference = _w._i("Difference")       
_w.Diff = _w._i("Diff")       
_w.As = _w._i("As")    
_w.Between = _w._i("Between") 
_w.Abs = _w._i("Abs")       
_w.Every = _w._i("Every")
_w.Any = _w._i("Any")        
_w.Unknow = _w._i("Unknow")       
_w.Some = _w._i("Some") 
_w.Date = _w._i("Date")    
_w.Time = _w._i("Time")             
_w.Set = _w._i("Set")    
_w.In = _w._i("In")    
_w.Inner = _w._i("Inner")
_w.Rigth = _w._i("Rigth")
_w.When = _w._i("When")
_w.Match = _w._i("Match")
_w.Matched = _w._i("Matched")
_w.Then = _w._i("Then")
_w.Else = _w._i("Else")
_w.Souce = _w._i("Sorce")
_w.Use = _w._i("Use")
_w.Using = _w._i("Using")
_w.Target = _w._i("Target")
_w.Option = _w._i("Option")
_w.With = _w._i("With")
_w.Index = _w._i("Index")
_w.Indexes = _w._i("Indexes")
_w.Full = _w._i("Full")
_w.Empty = _w._i("Empty")
_w.Join = _w._i("Join")
_w.On = _w._i("On")
_w.And = _w._i("And")
_w.Or = _w._i("Or")
_w.Not = _w._i("Not")
_w.Like = _w._i("Like")
_w.Merge = _w._i("Merge")
_w.Duplicate = _w._i("Duplicate")
_w.Dup = _w._i("Dup")
_w.Ascending = _w._i("Ascending")
_w.Asc = _w._i("Asc")
_w.Descending = _w._i("Descending")
_w.Desc = _w._i("Desc")
_w.Is = _w._i("Is")
_w.Expression = _w._i("Expression")

    
from Node.Io import DEBUG    
from Node.Tokenizer import Tokenizer
from Node.Types import Types


class _oql_(object):
    
    def __init__(self, parent):
        self.setParent(parent)        
        return
    
    def setParent(self, parent, key=None):
        self._Parent=parent        
        return self
    
    @property 
    def Name(self):
        return self.__class__.__name__ 
    
    @property 
    def Parent(self):
        return self._Parent
        
    @property 
    def Root(self):
        if self._Parent is not None:
            if hasattr(self._Parent, _w.Root):
                return self._Parent.Root
            else:
                return self._Parent
        return self
        
    def __getitem__(self, i):
        return object.__getattr__(self, "_"+i.capitalize(), None)
        
    def __setitem__(self, i, v):
       DEBUG.SETITEM(i, v, self.__dict__ )
       object.__setattr__(self, "_"+i.capitalize(), v)
       if isinstance(v, _oql_):
            v.setParent(self)
       return
     
    def __getattr__(self, i):
        DEBUG.GERATTR(i, self.__dict__ )
        if i.isupper():
            return self[i]
        return object.__getattr__(self, i)
        
    def __setattr__(self, i, v):
        if i.isupper():
            self[i]=v            
            return
        return object.__setattr__(self, i, v)
    
    def __repr__(self):
        s="<OQL:"+self.Name
        for e, v in self.__dict__.items():            
            if e[0]=="_" and e[1].isupper():
                if e!="_Parent":
                    s+=" "+e[1:]+"="+repr(v)
        s+=">"
        return s
    
    pass
       
class oqlElement(_oql_):
    pass
    
class oqlElement(oqlElement):
    
    _Functions = {
    	            _w.Count:   lambda tkz: None,
    	            _w.Sum:     lambda tkz: None,
    	            _w.Average: lambda tkz: None,
    	            _w.Avg:     lambda tkz: None,
    	            _w.Max:     lambda tkz: None,
    	            _w.Min:     lambda tkz: None,
    	            _w.Abs:     lambda tkz: None,
    	            }
    
    def __init__(self, parent, t1=None):
        super().__init__(parent)
        self.T1 = t1
        return
    
    class Func(oqlElement):
    	    pass
        
    class Variable(oqlElement):
        pass
    
    @classmethod 
    def Parse(cls, parent, tkz, _expect=False):
        DEBUG.ELEMENT()        
        if tkz.isNumeric():
            v=tkz.Next()
            DEBUG.ELEMENT.NUMERIC(v)
            return v.Value
        elif tkz.isString():
            return oqlElement(parent, tkz.Next().Value)
        elif tkz.Next(_w._True):
            return oqlElement(parent, True) 
        elif tkz.Next(_w._False):
            return oqlElement(parent, False)
        elif tks.isIdentifier():
            fn=cls._Functions.get(tkz.Current, None)
            if callable(fn):
                tkz.next()
                fn(tkz)
            else:
                nm=tkz.Next()
                if nm is None:
                    raise Error.SyntaxError()
                if tkz.Next("."):
                    nn=tkz.Next()
                    if nn is None:
                        raise Error.SystamError()   
                                                
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    
    pass
    
class oqlTerm(_oql_):
    
    def __init__(self, parent, t1=None, t2=None):
        super().__init__(parent)
        self.T1 = t1
        self.T2 = t2
        return
        
    pass
    
class oqlTerm(oqlTerm):
     
    class Neg(oqlTerm):
        pass
        
    class Pos(oqlTerm):
        pass    
    
    @classmethod 
    def Parse(self, parent, tkz, _expect=False):
        DEBUG.TERM()
        if tkz.Next("-"):            
            t1=oqlElement.Parse(None, tkz)
            return Term.Neg(parent, t1)
           
        elif tkz.Next("+"):            
            t1=oqlElement.Parse(None, tkz)
            return oqlTerm.Pos(parent)
              
        elif tkz.Next("("):
            	t1=oqlExpression.Parse(parent, tkz)
            	tkz.Expect(")")
            	return t1
            	
        else:
            return oqlElement.Parse(parent, tkz, _expect=_expect)
            
        return 
        
    pass
    
class oqlFactor(_oql_):
    
    def __init__(self, parent, t1=None, t2=None):
        super().__init__(parent)
        self.T1 = t1
        self.T2 = t2
        return    
        
    pass

class oqlFactor(oqlFactor):
    
    class Mult(oqlFactor):
        
        pass
        
    class Div(oqlFactor):
        
        pass
        
    class Pow(oqlFactor):
        
        pass
        
    class Mod(oqlFactor):
                
        pass
        
    
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        DEBUG.FACTOR()
        t1=oqlTerm.Parse(None, tkz)
        if tkz.Next("*"):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactor.Mult(parent, t1, t2)
        elif tkz.Next("/"):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactor.Div(parent, t1, t2)
        elif tkz.Next("%"):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactor.Mod(parent, t1, t2)
        elif tkz.Next(">>"):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactor.Shr(parent, t1, t2)
        elif tkz.Next("<<"):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactor.Shl(parent, t1, t2)
        elif tkz.Next(_w.In):
            t2oqlFactor.Parse(None, tkz)
            return oqlFactir.In(parent, t1, t2)
        elif tkz.Next(_w.Like):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactir.Like(parent, t1, t2)
        elif tkz.Next(_w.Between):
            t2=oqlFactor.Parse(None, tkz)
            return oqlFactor.Between(parent, t1, t2)    
        elif tkz.Next(_w.Is):
            t2=oqlFactor.Parse(None, tkz)   
            return oqlFactor.Is(parent, t1, t2)    
        else:
            return t1 
            
        if _expected:
            raise Error.SyntaxError()
               
        return None
        	
    pass
    
class oqlSubExpression(_oql_):
    
    def __init__(self, parent, t1, t2=None):
        super().__init__(parent)
        self.T1=t1
        self.T2=t2
        DEBUG.SUBEXPRESSION.INIT(self.__dict__)
        return    
    
    pass

class oqlSubExpression(oqlSubExpression):
    
    class Add(oqlSubExpression):
        pass
        
    class Sub(oqlSubExpression):
        pass
        
    class BAnd(oqlSubExpression):
        pass
        
    class BOr(oqlSubExpression):
        pass
    
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):   
        DEBUG.SUBEXPRESSION()     
        t1=oqlFactor.Parse(parent, tkz)        
        if t1 is not None:                                
            if tkz.Next("+"):
                t2=oqlSubExpression.Parse(None, tkz)
                return oqlSubExpression.Add(parent, t1, t2)
            elif tkz.Next("-"):
                t2=oqlSubExpression.Parse(None, tkz)
                return oqlSubExpression.Sub(parent, t1, t2)
            elif tkz.Next("&"):
                t2=oqlSubExpression.Parse(None, tkz)
                return oqlSubExpression.BAnd(parent, t1, t2)
            elif tkz.Next("|"):
                t2=oqlSubExpression.Parse(None, tkz)
                return oqlSubExpression.BOr(parent, t1, t2)          
         
            return t1
            
        if _expected:
            raise Error.SyntaxError()
            
        return None
           
    pass
    
    
class oqlExpression(_oql_):
    
    def __init__(self, parent=None, t1=None, t2=None):
        super().__init__(parent)
        self.T1=t1
        self.T2=t2
        return
        
    pass

class oqlExpression(oqlExpression):
    
    class And(oqlExpression):
        
        def __init__(self, parent, t1, t2=None):
            super().__init__(parent, t1, t2)
            return
            
        pass
        
    class Or(oqlExpression):        
        pass
        
    class Equal(oqlExpression):
        pass
           
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        DEBUG.EXPRESSION()
        if tkz.Next(_w.Not):
            pass
        t1=oqlSubExpression.Parse(parent, tkz)
        if tkz.Next(_w.And):
            t2=oqlExpression.Parse(None, tkz)
            return oqlExpression.And(parent, t1, t2)
        elif tkz.Next(_w.Or):
            t2=oqlExpression.Parse(None, tkz)
            return oqlExpression.Or(parent, t1, t2)        
        elif tkz.Next("=", "=="):
             t2=oqlExpression.Parse(None, tkz)
             return oqlExpression.Equal(parent, t1, t2)
        elif tkz.Next("!=", "<>"):
             t2=oqlExpression.Parse(None, tkz)
             return oqlExpression.notEqual(parent, t2)   
        elif tkz.Next(">"):
             t2=oqlExpression.Parse(None, tkz)
             return oqlExpression.Greater(parent, t1, t2)  
        elif tkz.Next("<"):
             t2=oqlExpression.Parse(None, tkz)
             return oqlExpression.Less(parent, t1, t2)
        elif tkz.Next(">="):
             t2=oqlExpression.Parse(None, tkz)
             return oqlExpression.GreaterEqual(pzrent, t1, t2)
        elif tkz.Next("<="):
             t2=oqlExpression.Parse(None, tkz)
             return oqlExpression.LessEqual(parent, t1, t2)
        elif tkz.Next(_w.Is):
            pass             
        
        if t1 is not None:
           return t1
           
        if _expected:
           raise Error.SyntaxError()    
       
        return None
    
    pass    
    
class oqlExpressionList(_oql_):
    pass
    
class oqlExpressionList(oqlExpressionList):
           
      
    class All(oqlExpressionList):
        pass
        
    def __init__(self, parent=None, t1=None):
        super().__init__(parent)
        self,T1=t1
        return
                
    @classmethod 
    def Parse(cls, name, parent, tkz, _expected=False):
        #DEBUG.EXPRESSIONLIST(tkz)
        
        if tkz.Next("*"):
            return oqlExpressionList.All(name, parent)
        
        rr=[]
        while True:
            DEBUG.EXPRESSIONLIST(tkz)
            e=oqlExpression.Parse(None, tkz)
            if not tkz.Next(","):
                break
        
        if _expected:
            raise Error.SyntaxError()
        
        return None
    
    pass
    
class oqlWhere(_oql_):
    
    def __init__(self, parent):
        super().__init__(parent)
        return
    
    @classmethod 
    def Parse(cls, name, parent, tkz, _expected=False):
        if tkz.Next(_w.Where):
                        
            e=oqlExpression.Parse(None, tkz)
            if e is not None:
                parent[name.upper]=e  
                return e
                
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    
    pass
    
    
class oqlGroup(_oql_):
   
    def __init__(self, parent):
        super().__init__(parent)    
    
    @classmethod 
    def Parse(cls, name, parent, tkz, _expected=False):
        if tkz.Next(_w.Group):
            if tkz.Next(_w.By):
                pass
            r=oqlGroup(parent)
            parent[name]=r
            rr=[]
            while True:
                e=oqlExpression.Parse(tkz, _expected=True)
                if tkz.Next(_w.Ascendig, _w.Asc):
                    pass
                elif tkz.Nexr(_w.Descending, _w.Desc):
                    pass
                if tkz.Next(_w.Null):
                    if tkz.Next(_w.First):
                        pass
                    elif tkz.Next(_w.Last):
                        pass
                rr.append("")
                if tkz.Next(","):
                    continue
                break
                        
            return r
                
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    
    pass
    
class oqlHaving(_oql_):
    
       
    def __init__(self, parent):
        super().__init__(parent)
    
    @classmethod 
    def Parse(cls, name, parent, tkz, _expected=False):
        if tkz.Next(_w.Having):
            e=oqlExpression.Parse(None, tkz)
            if e is not None:
                return oqlHaving(parent)
        return None
    
    
    pass
    
    
class oqlFrom(_oql_):
   
    def __init__(self, parent):
        super().__init__(parent)
    
    @classmethod 
    def Parse(cls, name, parent, tkz, _expected=False):
        if tkz.Next(_w.From):
            r=oqlFrom(parent)
            parent[name]=r
            while True:        
                al=_w.Collection      
                if tkz.Next("("):
                    er={}
                    sl=oqlSelect(er,tkz, _expected=True)
                    tkz.Expect(")")
                else:
                    nm = tkz.ExpectIdentifier()
                    er = nm.Value
                if tkz.Next(_w.As):
                   al= tk.ExpectIdentifier()
                r[al]=er
                if tkz.Next(","):
                    continue
                break           
            return r
            
        if _expected:
            raise Error.SyntaxError()
            
        return None
        
    pass
 
class oqlQualifier(_oql_):     
        
    def __init__(self, parent):
        super().__init__(parent)
     
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Distinct):
            pass
        elif tkz.Next(_w.Duplicate):
            pass
        
        return None
        
    pass
    
class oqlQuantifier(_oql_):
    
    
    def __init__(self, parent, quant=None):
        super().__init__(parent)
        self[_w.Value]=quant
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):        
        if tkz.Next(_w.All):
            return oqlQuantifier(parent, None)
            
        elif tkz.Next(_w.Top, _w.First):
            ex=oqlSubExpression.Parse(tkz)
            if tkz.Next(_w.Percent, "%"):
                ex=oqlFactor.Div(1, ex)
            return oqlQuantifier(parent, ex)        
        elif tkz.Next(_w.Botton, _w.Last):
            ex=oqlSubExpression.Parse(tkz)
            if tkz.Next(_w.Percent, "%"):
                ex=oqlFactor.Div(1, ex)
            ex=oqlTerm.Neg(ex)
            return oqlQuantifier(parent, ex)   
        return None
    
    pass
    
class oqlLimit(_oql_):
    
    def __init__(self, parent):
        super().__init__(parent)
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Limit):
            r=oqlLimit(parent)
            parent[_w.Limit]=r
            ex=oqlSubExpression.Parse(r, tkz)
            return r
            
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    pass
    
class oqlOutput(_oql_):
       
    def __init__(self, parent):
        super().__init__(parent)
        
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Output):
            
            while True:
                if tkz.Next(_w.Inserted, _w.insert):
                    pass
                elif tkz.Next(_w.Deleted, _w.Delete):
                    pass
                elif tkz.Next(_w.Updated, _w.Update):
                    pass
                elif tkz.Next(_w.Rejected, _w.Reject):
                    pass
                ex=oqlSubExpression.Parse(None, tkz, _expected=True)
                if tkz.Next(","):
                    continue
                break
            
            it= oqlInto(parent, tkz)
            
            return oqlOutput(parent)
            
        return None
        
    pass
    
class oqlSelect(_oql_):
       
    def __init__(self, parent):
        super().__init__(parent)
        
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        DEBUG.SELECT(tkz)
        if tkz.Next(_w.Select):   
            r=oqlSelect(parent)
            parent[_w.Select]=r
            
            lq=oqlQualifier.Parse(r, tkz)
            
            lz=oqlQuantifier.Parse(r, tkz)            
            
            fl=oqlExpressionList.Parse("Fields", r, tkz)
        
            tb=oqlFrom.Parse(_w.From, r, tkz, _expected=True)
            
            w=oqlWhere.Parse(_w.Where, r, tkz)
            
            w=oqlLimit.Parse(r, tkz)
            
            g=oqlGroup.Parse(_w.Group, r, tkz)
        
            h=oqlHaving.Parse(_w.Having, r, tkz)
            
            ot=oqlOutput.Parse(r, tkz) 
            
            return r
            
        if _expected:
            raise Error.SyntaxError()
                
        return None
        
    pass
    
class oqlUpdate(_oql_):
   
    def __init__(self, parent):
        super().__init__(parent)
            
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Updare):
            nm = tkz.ExpectIdentifier()
        
            st = oqlSet.Parse(tkz, _expected=True)
            vl = oqlValues.Parse(tkz)
            if vl is None:
                fr = oqlFrom(tkz)
            
            wh = oqlWhere.Parse(tkz)
            
            return oqlUpdate(parent)
        
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    pass
    
class oqlDelete(_oql_):
       
    def __init__(self, parent):
        super().__init__(parent)
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Delete):
            qt=oqlQuantifier.Parse(tkz)
            
            fr=oqlFrom(tkz, _expected=True)
            
            w=oqlWhere(tkz, _expected=True)
            
            return oqlDelete(parent)
            
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    pass
    
class oqlMerge(_oql_):
       
    def __init__(self, parent):
        super().__init__(parent)
        
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Merge):
            qt = oqlQuantifier(tkz)
            
            tkz.Expect(_w.Into)
            nm = tkz.ExpectIdentifier()
            
            return oqlMerger(parent)     
            
        if _expected:
            raise Error.SyntaxError()
               
        return None
    
    pass
    
class oqlInsert(_oql_):
       
    def __init__(self, parent):
        super().__init__(parent)
        
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Insert):
            
            it = oqlInto(tkz, _expected=True)
            
            st= oqlSet.Parse(tkz)
            vl= oqlValues.Parse(tkz)
            if st is None and vl is None:
                raise Error.SyntaxError()
            
            return oqlInsert(parent)
        
        if _expected:
            raise Error.SyntaxError()
            
        return None
    
    pass
    
class oqlCreateView():
    
    pass
    
class oqlCreateIndex():
    
    pass
   
class oqlCreateDatabase():
    
    pass

class oqlCreateCatalog():
    
    pass
    
class oqlCreateTable():
    
    pass

class oqlCreateCollection():
    
    pass
    
class oqlCreateDomain():
    
    pass    
    
class oqlCreate(_oql_):
   
    def __init__(self, parent):
        super().__init__(parent)
    
    _SubCommands = (
    	              oqlCreateView,
    	              oqlCreateIndex,
    	              oqlCreateDatabase,
    	              oqlCreateCatalog,
    	              oqlCreateTable,
    	              oqlCreateCollection,
    	              oqlCreateDomain,
    	               )
    
    @classmethod 
    def Parse(cls, parent,tkz, _expected=False):
        if tkz.Next(_w.Create):
            
            pass
        
        return None
    
    
    pass
    
class oqlExplain(_oql_):
    
       
    def __init__(self, parent):
        super().__init__(parent)
    
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.Explain):
            
            pass
        
        return None
    
    pass
    
class oqlWith(_oql_):
    
       
    def __init__(self, parent):
        super().__init__(parent)
        
    _Commands = (
    	            oqlSelect,
    	            oqlUpdate,
    	            oqlInsert,
    	            oqlDelete,
    	            oqlMerge,
    	            oqlCreate,
    	            oqlExplain,
    	            )
    	            
    @classmethod 
    def Parse(cls, parent, tkz, _expected=False):
        if tkz.Next(_w.With):
            
            nm = tkz.ExpectIdentifier()
            if tkz.Next(_w.Do):
                pass
            
            for fn in cls._Commands:
                r=fn.Parse(parent, tkz)
            if r is not None:
                return r
                  
            if _expected:
                raise Error.SyntaxError()    
                
            return oqlWith(parent)
        
        return None
        
    pass
    
class Error(Exception):
    pass
    
Error.SyntaxError = Error

class Oql(dict):
    
    Select = oqlSelect
    Update = oqlUpdate
    Delete = oqlDelete
    Insert = oqlInsert
    Create = oqlCreate
    Explain = oqlExplain
    With = oqlWith
    
    Error = Error
    
    
    _Words = (
    	        _w.Select,
    	        _w.From,
    	        _w.Update,
    	        _w.Delete,
    	        _w.Insert,
    	        _w.Where,
    	        _w.Order,
    	        _w.By,
    	        _w.Create,
    	        _w.Having,
    	        _w.Distinct,
    	        _w.Duplicate,
    	        _w.Top,
    	        _w.All,
    	        _w.First,
    	        _w.Merge,
    	        _w.Last,
    	        _w.Order,
    	        _w.Into,
    	        _w.Explain,
    	        _w.Strict,
    	        _w.Above,
    	        _w.Below,
    	        _w.Union,
    	        _w.As,
    	        _w.Between,
    	        _w.Count,
    	        _w.Average,
    	        _w.Min,
    	        _w.Max,
    	        _w.In,
    	        _w.Sum,
    	        _w.Inner,
    	        _w.Left,
    	        _w.Output,
    	        _w.Rigth,
    	        _w.Full,
    	        _w.Empty,
    	        _w.Null,
    	        _w.Join,
    	        _w.On,
    	        _w.And,
    	        _w.Or,
    	        _w.Not,
    	        _w.Like,
    	        _w.In,    	        
    	        )
    	        
    _Symbols = (
   	           "(",
    	          ")",
   	           )
    _Commands = (
    	            oqlSelect,
    	            oqlUpdate,
    	            oqlInsert,
    	            oqlDelete,
    	            oqlMerge,
    	            oqlCreate,
    	            oqlExplain,
    	            oqlWith,
    	            )
    
    @classmethod 
    def Parse(cls, tkz, _expected=False):
        tkz=Tokenizer.From(tkz, words=cls._Words, symbols=cls._Symbols)
        resp={}
        for fn in cls._Commands:
            r=fn.Parse(resp, tkz)
            if r is not None:
                if tkz.Next(";"):
                    pass
                return resp
                  
        if _expected:
            raise Error.SyntaxError()             
        
        return None
    
    pass

if __name__ =="__main__":
    
    s="1+1"
    tkz=Tokenizer.From(s, words=Oql._Words, symbols=Oql._Symbols)
    resp={}
    q=oqlExpression.Parse("t1", tkz)
    print(repr(q))
    sys.exit(0)
    
    s="select * from a"
    
    q=Oql.Parse(s)
    
    print(repr(q))
    
    pass




###