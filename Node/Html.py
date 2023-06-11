#
#
#
import sys
import os

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w
from Node.File import File
from Node.Markup import Markup
from Node.Mime import Mime

from io import StringIO

_i = sys.intern

_w.Html = _i('Html')
_w.Script = _i('Script')
_w.Id = _i('Id')
_w.Body = _i('Body')
_w.Head = _i('Head')
_w.HEADER = _i('Header')
_w.AUTOPLAY = _i('Autoplay')
_w.SCHEME = _i('Scheme')
_w.SUB = _i('Sub')
_w.AUTOCOMPLETE = _i('Autocomplete')
_w.ABBR = _i('Abbr')
_w.ASIDE = _i('Aside')
_w.HREFLANG = _i('Hreflang')
_w.Area = _i('Area')
_w.TD = _i('Td')
_w.TH = _i('Th')
_w.TR = _i('Tr')
_w.Class = _i("Class")
_w.FOR = _i('For')
_w.LOOP = _i('Loop')
_w.BUTTON  = _i('Button')
_w.SORTED = _i('Sorted')
_w.METER = _i('Meter')
_w.Alt = _i('Alt')
_w.DETAILS = _i('Details')
_w.DEFER = _i('Defer')
_w.MULTIPLE = _i('Multiple')
_w.REVERSED = _i('Reversed')
_w.TRANSLATE = _i('Translate')
_w.NOSCRIPT = _i('Noscript')
_w.Span = _i('Span')
_w.STRONG = _i('Strong')
_w.BLOCKQUOTE = _i('Blockquote')
_w.ALT = _i('Alt')
_w.MAP = _i('Map')
_w.HR = _i('Hr')
_w.Stylesheet = _i("Stylesheet")
_w._OPTION_ = _i('Option')
_w.KIND = _i('Kind')
_w.TRACK = _i('Track')
_w.SUMMARY = _i('Summary')
_w.Dialog = _i('Dialog')
_w.NAV = _i('Nav')
_w.TEXTAREA = _i('Textarea')
_w.LEGEND = _i('Legend')
_w.COL = _i('Col')
_w.COLS = _i('Cols')
_w.SELECT = _i('Select')
_w._OBJECT_ = _i('Object')
_w.OPTGROUP = _i('Optgroup')
_w.HIDDEN = _i('Hidden')
_w.Scope = _i('Scope')
_w.PARAM = _i('Param')
_w.LABEL_ = _i('Label')
_w.CROSSRIGIN = _i('Crossorigin')
_w.REQUIRED = _i('Required')
_w.Left = _i('Left')
_w.RIGTH = _i('Rigth')
_w.Center = _i('Center')
_w.JUSTIFY = _i('Justify')
_w.VAR = _i('Var')
_w.Title = _i('Title')
_w.PRE = _i('Pre')
_w.ARTICLE = _i('Article')
_w.Style = _i('Style')
_w.CHECKED = _i('Checked')
_w.DEL = _i('Del')
_w.IMG = _i('Img')
_w.CLASS = _i('Class')
_w.Link = _i('Link')
_w.IMAGE = _i('Image')
_w.DIRNAME = _i('Dirname')
_w.Sizes = _i('Sizes')
_w.Br = _i('Br')
_w.TARGET = _i('Target')
_w.Meta = _i('Meta')
_w.Media = _i('Media')
_w.Div = _i('Div')
_w.ACCEPT = _i('Accept')
_w.EMBED = _i('Embed')
_w.Src = _i('Src')
_w.Figure = _i('Figure')
_w.PICTURE = _i('Picture')
_w.ACCESSKEY = _i('Accesskey')
_w._OL_ = _i('Ol')
_w._UL_ = _i('Ul')
_w.LI = _i('Li')
_w.A = _i('A')
_w.Align = _i('Align')
_w.MAIN = _i('Main')
_w.FORM = _i('Form')
_w.LANG = _i('Lang')
_w.Table = _i('Table')
_w.REL = _i('Rel')
_w.CODE = _i('Code')
_w.MAX = _i('Max')
_w.MIN = _i('Min')
_w.DRAGGABLE = _i('Draggable')
_w.BASE = _i('Base')
_w.AUTOFOCUS = _i('Autofocus')
_w.HEIGTH = _i('Heigth')
_w.CAPTION = _i('Caption')
_w.WIDTH = _i('Width')
_w.CITE = _i('Cite')
_w.VIDEO = _i('Video')
_w.CANVAS = _i('Canvas')
_w.HREF = _i('Href')
_w.DISABLED = _i('Disabled')
_w._ENABLED_ = _i('Enabled')
_w.FOOT = _i('Foot')
_w.FOOTER = _i('Footer')
_w.CHARSET = _i('Charset')
_w.RECT = _i('Rect')
_w.ALTERNATE = _i('Alternate')
_w.AUTHOR = _i('Author')
_w.DNS_PREFETCH = _i('Dns-Prefetch')
_w.HELP = _i('Help')
_w._ICON_ = _i('Icon')
_w._LICENSE_ = _i('License')
_w.NEXT = _i('Next')
_w._PINGBACK = _i('Pingback')
_w._PRECONNECT_ = _i('Preconnect')
_w._PREFETCH_ = _i('Prefetch')
_w._PRELOAD_ = _i('Preload')
_w.PRERENDER = _i('Prerender')
_w.Prev = _i('Prev')
_w.SEARCH = _i('Search')
_w.MARK = _i('Mark')
_w.CONTENTEDITABLE = _i('Contenteditable')
_w.COLGROUP = _i('Colgroup')
#
#
_w.__BLANK = _i('_Blank')
_w.__SELF = _i('_Self')
_w.__TOP = _i('_Top')
_w.__PARENT = _i('_Parent')


class _globalAttr():

    def _Id(self, s=None):
        return self(_Id=s)

    def _Class(self, s=None):
        return self(_Class=s)

    def _Lang(self, s=None):
        return self(_Lang=s)

    def _Accesskey(self, s=None):
        return self(_AccessKey=s)

    def _Contenteditable(self, s=None):
        return self(_ContentEditable=s)

    def _Dir(self, s=None):
        return self(_Dir, s)

    def _Draggable(self, s=None):
        return self(_Draggable=s)

    def _Hidden(self, s=None):
        return self(_Hidden=s)

    def _Spellcheck(self, s=None):
        return self(_Spellchexk= s)

    def _Style(self, s=None):
        return self(_Style=s)

    def _Tabindex(self, s=None):
		      return self(_TabIndex=s)

    def _Title(self, s=None):
        return self(_Title=s)

    def _Translate(self, s=None):
        return self(_Translate=s)

    pass
    
class _Type():
    
    def _Type(self, s=None):
        return self(_Type=s)

    
    pass

class _Src():

    def _Src(self, s=None):    
        return self(_Src=s)

    def _Srcset(self, s=None):
        return self(_Srcset=s)

    pass


class _Name():

    def _Name(self, s=None):
        return self(_Name=s)
         
    pass

class _Label():

    def _Label(self, s=None):
        return self(_Labek=s)
        
    pass


class _Ismap():

    def _Ismap(self, s=None):
        return self(_Ismap=s)

    pass


class _Charset():

    def _Charset(self, s=None):
        return self(_Charset=s)

    pass


class _Colspan():

    def _Colspan(self, s):
        return self(_Colspan=s)

    def _Rowspan(self, s):
        return self(_Rowspan=s)

    pass


class _Data():

    def _Data(self, s):
        return self(_Data=s)

    pass


class _Rel():

    def _Rel(self, s):
        return self(_Rel=s)

    pass


class _Open():

    def _Open(self, f=None):
        return self(_Open=f)
    
    pass


class _Media():

    def _Media(self, s):
        return self(_Medua=s)
     
    pass


class _Sizes():

    def _Sizes(self, s):
        return self(_Sizes=s)
 
    pass


class _Target():

    def _Target(self, s):
        return self.TARGET(s)

    def _TargetBlank(self):
        return self._Target(__BLANK)

    pass


class _Autofocus():

    def _Autofocus(self, s):
        return self(_Autofocus=s)

    pass


class _Href():

    def _Href(self, s):
        return self(_Href=s)

    def _Hreflang(self, s):
        return self(_Hreflang=s)

    pass


class _Value():

    def _Value(self, s):
        return self(_Value=s)
        
    pass


class _Valuetype():

    def _Valuetype(self, s):
        return self(_Valuetype=s)
                
    pass


class _Max():

    def _Max(self, s):
        return self(_Max=s)

    pass


class _Align():

    def _Align(self, s):
        return self(_Align=s)

    pass


class _Min():

    def _Min(self, s):
        return self(_Min=s)

    pass


class _Alt():

    def _Alt(self, s):
        return self(_Alt=s)

    pass


class _Content():

    def _Content(self, s):
        return self(_Content=s)

    pass


class _Crossorigin():

    def _Crossorigin(self, s):
        return self(_Crossorigin=s)

    pass


class _Width():

    def _Width(self, s):
        return self(_Width=s)

    def _Heigth(self, s):
        return self(_Heigth=s)

    pass


class _Form():

    def _Form(self, s):
        return self(_Form=s)

    def _Formaction(self, s):
        return self(_Formaction=s)

    def _Formenctype(self, s):
        return self(_formenctype=s)

    pass


class _Headers():

    def _Headers(self, s):
        return self.Attr(_w.Headers, s)

    pass
    
    
class _Event():
    
    
    pass   


class _Disabled():


    def _Enabled(self):
        self._Arguments.pop(_w.DISABLED)
        return self

    def _Disabled(self):
        return self(_Disabled=None)

    pass


class EmptyTag(_globalAttr, Markup.EmptyTag):

    def On(self, event, s):
        e = 'on' + event
        self[e] = s
        return self
    pass



class asText(list):
    
    
    pass


class asTag(list, _globalAttr):
    
    def __init__(self, parent, tag, sbreak=False, breakclose=False, single=None, empty=None, **attrs):
        self._Parent=parent
        self._Tag=tag
        self._Break=sbreak
        self._BreakClose= breakclose
        self._Single=single
        self._Empty= empty
        #self._BreakAfter= _breakafter
        #self._Indent=_indent
        #print("init indent", tag, _indent)
        self._Arguments = {}
        if hasattr(parent, "append") and callable(getattr(parent, "append")):
           parent.append(self)
        self(**attrs)
        return
        
    def prefix(self, out):
        return
        
    def Attr(self, i, v=None):
        if v is None:
            return self._Arguments.get(i, None)
        self._Arguments[i]= v        
        return self        
        
    def __call__(self, *s, **kvargs):
        for e in s:
            self.append(e)
        for e, v in kvargs.items():
            if e[0]=="_":
                e=e[1:]
            e=sys.intern(e.capitalize())
            self.Attr(e, v)
        return self
     
    def __setattr__(self, item, v):
        if isinstance(item, str):
           if item == item.upper():
              item = item.replace('_', '-')
              item = sys.intern(item.title())
              self._Arguments[item] = v
              return
#    raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

        return super().__setattr__(item, v)
        
    def __getattr__(self, i):
        if isinstance(i, str):
            if i.isupper():
                i = i.replace('_', '-')
                i = sys.intern(i.title())
                return self._Arguments.get(i, None)
        raise AttributeError("attibute not found %s in %s" % (i, self.__class__.__name__))

        return super().__getattr__(item)
        
    def writeout_open(self, out):
        self.prefix(out)
        out.write("<")
        out.write(self._Tag)
        if self._Arguments is not None:
            for a, v in self._Arguments.items():
                out.write(" ")
                out.write(a)
                out.write("=")
                if type(v) == int:
                    out.write(str(v))
                elif type(v)==float:
                    out.write(str(v))
                elif type(v)==bool:
                    if v==True:
                        out.write(_w._True)
                    else:
                        out.write(_w._False)
                elif v==None:
                    out.write("Null")
                elif type(v)==str:
                    out.write('"')
                    out.write(v)
                    out.write('"')
                    
        if self._Single:
            out.write("/>")
        else:
            out.write(">")
        return
        
    def writeout_close(self, out):
        out.write("</")
        out.write(self._Tag)
        out.write(">")
        return
    
    def writeout(self, out, _indent=0):
        #print("writeout i=",_indent)
        if _indent >0:
            out.write("\t"*_indent)
        self.writeout_open(out)
        
        if self._Break:
           out.write("\n")      
           if self._Tag is None:
               i= _indent+1
           else:
               i=_indent + 1 # len(self._Tag)+2
        else:
            i=0
        #print("writeout indent", self._Indent)   
        
        #print("---i=", i)
        ff=False            
        if (not self._Empty) and len(self)>0:
            for e in self:
                if isinstance(e, str):
                    if ff:
                        out.write(' ')
                    out.write(e )
                else:
                    e.writeout(out, _indent=i)
                ff=True
     
        #if self._Breakline and ff:
        #    out.write("\n")    
        
        if not(self._Single or self._Empty):
            if self._Break:
                if ff:
                    out.write("\n")
                out.write("\t"*_indent)
            self.writeout_close(out)
      
            if self._Break or self._BreakClose:
                out.write("\n")
            
        return
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, tb=None):
        if tb is None:
            pass # no exception
        else:
            # Exception occurred, so rollback.
            pass
        return False  
        
    def __str__(self):
        s = StringIO()
        self.writeout(s)
        return s.getvalue()
        
    def bytes(self, encode="utf-8"):
        return bytes(str(self), encode)
    
    pass


class asComment(asTag):
    
    def __init__(self, parent):
        asTag.__init__(self, parent, None, sbreak=True)       
        return
        
        
    def writeout_open(self, out):
        out.write("<!-- ")
        return
                
    def writeout_close(self, out):
        out.write(" -->")
        return
                     
    pass
    
class asTitle(asTag):
    
    def __init__(self, parent, *s, **attrs):
        asTag.__init__(self, parent, _w.Title, breakclose=True, **attrs)  
        self(*s)    
        return
        
        
    pass
    
class asStyle(asTag, _Media, _Type, _Event):
    
    def __init__(self, parent, *s, **attrs):
        asTag.__init__(self, parent, _w.Style, sbreak=True, **attrs)  
        for e in s:
            self.append(e)    
        
        return
    
    pass
    
class asLink(asTag):
    
    def __init__(self, parent, rel, href, type=None):
        asTag.__init__(self, parent, _w.Link, sbreak=True, empty=True, single=True)   
        self(rel=rel, href=href, type=type)    
        return
        
    pass
    
class asScript(asTag):
    
    def __init__(self, parent, src=None, type=None, 
    	            language=None,
    	            async=False,
    	            crossorigin=None, 
    	            defer=None, 
    	            fetchpriority=None,
    	            integrity=None, 
    	            nomodule=None,
    	            nonce=None, 
    	            referrerpolicy=None
    	            ):
        
        asTag.__init__(self, parent, _w.Script, sbreak=True)   
        self(src=src,
        	     language=language,
        	     defer=defer
        	    )    
        return
    
    pass
    
class asMeta(asTag):
    
    def __init__(self, parent, **attrs):
        asTag.__init__(self, parent, _w.Meta, sbreak=True, sempty=True, **attrs)
        return
    
    pass

class asHead(asTag):
    
    def __init__(self, parent):
        asTag.__init__(self, parent, _w.Head, sbreak=True)       
        return
        
    def Title(self, *s):
        return asTitle(self, *s)
        
    def Comment(self):
        return asComment(self)
        
    def Meta_Charset(self, charset=None):
        return asMeta(self, charset=charset)
    
    def Meta_Item(self, name=None, content=None):
        return asMeta(self, name=name, content=content)
    
    def Meta_HttpEquiv(self, http_equiv=None, content=None):
        return asMeta(self, http_equiv=http_equiv, content=content)
        
    def Script(self, src=None, type= None, 
    	            language=None,
    	            async=False, crossorigin=None, 
    	            defer=None, fetchpriority=None,
    	            integrity=None, nomodule=None,
    	            nonce=None, referrerpolicy=None):
        	return asScript(self, src=src, 
        		                    type=type,
        		                    language=language,
        		                    async=async,
        		                    crossorigin=crossorigin,
        		                    defer=defer,
        		                    fetchpriority=fetchpriority,
        		                    integrity=integrity,
        		                    nomodule=nomodule,
        		                    nonce=nonce, 
        		                    referrerpolicy=referrerpolicy
        		                )
        		                
        		              
    	            
    def Style(self, *s, **attrs):
        return asStyle(self, *s, **attrs)
        
    def Link(self, rel, href, type=None):
        return asLink(self, rel=rel, href=href, type=type)
        
    def Stylesheet(self, href):
        return self.Link(rel=_w.Stylesheet, type=Mime.TextCss, href=href)
        
    def Javascript(self, src=None):
        return self.Script(language="JavaScript", src=src)
        
    pass
    
    
class asButton(asTag, _Autofocus):
    
    def __init__(self, parent, **attrs):
        asTag.__init__(self, parent, _w.Button, sbreak=True, **attrs)       
        return
        
    def _Type(self, s=None):
        if s is not None:
            s=e.capitalize()
            if s==_w.Button:
                return self.Attr(_w.Type, _w.Button)
            elif s==_w.Reset:
                return self.Attr(_w.Type, _w.Reset)
            elif s==_w.Submit:
                return self.Attr(_w.Type, _w.Submit)
        return self.Attr(_w.Type, s)
    
    pass

class asImgage(asTag):
    
    def __init__(self, parent, src,
    	                 width=None,
    	                 heigth=None,
    	                 **attrs
    	             ):
        asTag.__init__(self, parent, _w.Img, sbreak=True, **attrs)       
        return
        
    pass
    
class asDiv(asTag):
    
    def __init__(self, parent,
    	                   **attrs    	                 
    	             ):
        asTag.__init__(self, parent, _w.Div, sbreak=True, **attrs)       
        return
        
    pass
    
class _Content_():
    
    def Button(self, type=None, 
    	        ):
    	    return asButton(self, type=type)
    	    
    def Form(self):
        return asForm(self)
      
    def Img(self, src, width=None, heigth=None, **attrs):
        return asImgage(self, src=src,
        	                width=width,
        	                heigth=heigth,
        	                **attrs
        	                )
        
        
    def Div(self, **attrs):
        return asDiv(self, **attrs)
        
    pass
    
class asBody(asTag, _Content_):
    
    def __init__(self, parent):
        asTag.__init__(self, parent, _w.Body, sbreak=True)       
        return
        
         
    pass
    
    

class Html(asTag):
    
    
    def __init__(self, lang="en"):
        asTag.__init__(self, None, _w.Html, sbreak=True)   
        self(lang=lang)    
        return
    
    def prefix(self, out):
        out.write("<!DOCTYPE Html>\n")   
        return
            
    def Head(self):
        return asHead(self)
        
    def Body(self):
        return asBody(self)
    
    pass



if __name__ == "__main__":
    
    css = File.Input.Load(("Styles/","Node.css"), pwd=__file__)
    
    with Html() as pg:
        h=pg
        pg._Id("23")
        with pg.Head() as hd:
            hd.Comment()
            hd.Meta_Charset(_w.UTF_8)
            hd.Meta_HttpEquiv(http_equiv=_w.Description, content="teste de pagina")
            hd.Title("xxx")
            hd.Style(css)
            hd.Stylesheet("Styles/Node.css")
        with pg.Body() as bd:
            bd("xxxxxxxx")
            bd.Div(_class="s")
            pass

   # h.writeout(sys.stdout)
    
    print(str(h))



####