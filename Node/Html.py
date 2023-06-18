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

from Node.System import System
from Node.File import File
from Node.Markup import Markup
from Node.Mime import Mime
from Node.Io import DEBUG

from io import StringIO
import json

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
_w.Pre = _i('Pre')
_w.ARTICLE = _i('Article')
_w.Style = _i('Style')
_w.CHECKED = _i('Checked')
_w.Del = _i('Del')
_w.Img = _i('Img')
_w.Class = _i('Class')
_w.Link = _i('Link')
_w.Image = _i('Image')
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
_w.Form = _i('Form')
_w.LANG = _i('Lang')
_w.Table = _i('Table')
_w.REL = _i('Rel')
_w.CODE = _i('Code')
_w.MAX = _i('Max')
_w.MIN = _i('Min')
_w.DRAGGABLE = _i('Draggable')
_w.Base = _i('Base')
_w.AUTOFOCUS = _i('Autofocus')
_w.HEIGTH = _i('Heigth')
_w.Caption = _i('Caption')
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
_w.Module = _i('Module')
_w.JQuery = _i('JQuery')

#
#
_w.__BLANK = _i('_Blank')
_w.__SELF = _i('_Self')
_w.__TOP = _i('_Top')
_w.__PARENT = _i('_Parent')

__Sequence= 0

def next_id(): 
    global __Sequence 
    __Sequence +=1
    return "Id"+str(__Sequence )


class _globalAttr():

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

class _Src():

    def _Src(self, s=None):    
        return self(_Src=s)

    def _Srcset(self, s=None):
        return self(_Srcset=s)

    pass

class _Colspan():

    def _Colspan(self, s):
        return self(_Colspan=s)

    def _Rowspan(self, s):
        return self(_Rowspan=s)

    pass

class _Target():

    def _Target(self, s):
        return self.TARGET(s)

    def _TargetBlank(self):
        return self._Target(__BLANK)

    pass




class _Href():

    def _Href(self, s):
        return self(_Href=s)

    def _Hreflang(self, s):
        return self(_Hreflang=s)

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
        #DEBUG("init indent", tag, _indent)
        self._Arguments = {}
        if hasattr(parent, "append") and callable(getattr(parent, "append")):
           parent.append(self)
        self(**attrs)
        return
        
    @property 
    def Contents(self):
        return self
        
    @property 
    def Root(self):
        if self._Parent is None:
            return self
        if hasattr(self._Parent, _w.Root):
            return self._Parent.Root
        return self
         
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
     
    def __setattr__(self, i, v):
        if i.isupper():
            i = i.replace('_', '-')
            i = sys.intern(i.title())
            self._Arguments[i] = v
            return
#    raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

        return super().__setattr__(i, v)
        
    def __getattr__(self, i):
        print("---", i)
        if i.isupper():
            i = i.replace('_', '-')
            i = sys.intern(i.title())
            return self._Arguments.get(i, None)
        raise AttributeError("TAG: attibute not found %s in %s" % (i, self.__class__.__name__))

        return super().__getattr__(item)
        
    def writeout_open(self, out):
        self.prefix(out)
        if self._Tag is None:
            return
            
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
                    out.write(_w.Null)              
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
        if self._Tag is not None:
            out.write("</")
            out.write(self._Tag)
            out.write(">")
        return
        
    def writeout_part(self, s, out, _indent=0):
        if _indent >0:
            out.write("\t"*_indent)
        out.write(s)
        out.write("\n")
        return
    
    def writeout(self, out, _indent=0):
        #DEBUG.WRITEOUT("i=",_indent
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
        #DEBUG.WRITEOUT("indent", self._Indent)   
        
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
                
        return self 
        
        
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
        
    def bytes(self, encode=_w.UTF_8):
        return bytes(str(self), encode)
        
    def Find(cls, tag=None, all=False, _id=None, _class=None):
        r=[]
        for e in self:
            ff=False            
            if tag is None:
                ff=True
            elif e._Tag==tag:
                ff=True
            if not ff and (_id is not None):
                i=self._Arguments.get(_w.Id, None)  
                if _id==i:
                    ff=True
            if not ff and (_class is not None):
                c=self._Arguments.get(_w.Class, None)
                if _class==c:
                    ff=True
            if ff:
                if all:
                   r.append(e)
                else:
                   return e
        if len(r)>0:
            return r
           
        return None
    
    _Requires = None
    
    @classmethod 
    def Requires(cls, k, f=True):
        if cls._Requires is None:
            cls._Requires={}
        cls._Requires[k]=f
        return 
        
    pass


class asComment(asTag):
    
    def __init__(self, parent):
        super().__init__(parent, None, sbreak=True)       
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
        super().__init__(parent, _w.Title, breakclose=True, **attrs)  
        self(*s)    
        return
        
        
    pass
    
class asStyle(asTag, _Event):
    
    def __init__(self, parent, *s, **attrs):
        super().__init__(parent, _w.Style, sbreak=True, **attrs)  
        for e in s:
            self.append(e)    
        
        return
    
    pass
    
class asLink(asTag):
    
    def __init__(self, parent, rel, href, type=None):
        super().__init__(parent, _w.Link, sbreak=True, empty=True, single=True)   
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
        
        super().__init__(parent, _w.Script, sbreak=True)   
        self(src=src,
        	     language=language,
        	     defer=defer
        	    )    
        return
    
    pass
    
class _HeadContent_():    
    pass
    
class asHeadBlock(asTag, _HeadContent_):
    
    def __init__(self, parent):
        super().__init__(parent, tag=None, sbreak=True, empty=True)
        return
        
    pass
    
class asCode(list):
    
    def __init__(self, parent, *args, **opts):
        super().__init__(*args, **opts)
        return
        
    def __call__(self, *s):
        self.extend(s)        
        return self
        
    def writeout(self, out, _indent=1):        
        return
    
    pass

class asJQuery(asScript):
    
    def __init__(self, parent):        
        if System.isDevelop:
            u="https://code.jquery.com/jquery-3.7.0.min.js" ## integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
        else:
            u="/Scripts/JQuery/jquery.js" 
        super().__init__(parent, src=u)
        return
    
    pass    
    
class asStylesheet(asLink):
    
    def __init__(self, parent, href, **attrs):
        super().__init__(parent, rel=_w.Stylesheet, href=href, **attrs)
        return
    
    pass
    
class asJavascriptCode(asCode):

    pass

class asJQueryUi(asJQuery):
    
    def __init__(self, parent):
        super().__init__(parent)
        if System.isDevelop:
            u="https://code.jquery.com/ui/1.13.2/jquery-ui.js"
            c="https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css"
        else:
            u="/Scripts/JQuery/jquery.js" 
            c="/Scripts/JQuery/Ui/jquery-ui.css"
        self._JQueryUi=asScript(None, src=u)
        self._Stylesheet=asStylesheet(None, href=c)
        self._Initialize=None
        return
        
    def InitializeFor(self, target, obj):
        if self._Initialize is None:
            self._Initialize ={}    
        self._Initialize[target]=obj      
        return self
        
    def writeout(self, out, _indent=0):
        #super().writeout(out, _indent)
        self._JQueryUi.writeout(out, _indent)
        self._Stylesheet.writeout(out, _indent)
        if self._Initialize is not None:      
            self.writeout_part("<Script>", out, _indent)     
            self.writeout_part('$( function() {', out, _indent)  
            for e, cd in self._Initialize.items():
                cd.doInitialize(out, _indent+2)
            self.writeout_part('}', out, _indent+2)
            self.writeout_part(');', out, _indent)
            self.writeout_part('</Script>', out, _indent)
        return
           
    pass
    
class asMeta(asTag):
    
    def __init__(self, parent, **attrs):
        super().__init__(parent, _w.Meta, sbreak=True, empty=True, **attrs)
        return
    
    pass
    
class _HeadContent_():
            
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
        return self.Script(language=_w.Javascript, src=src)
        
    def Module(self, src=None):
        return self.Script(language=_w.Module, src=src)
    
    pass

class asHead(asTag, _HeadContent_):
    
    def __init__(self, parent):
        super().__init__(parent, _w.Head, sbreak=True)    
        self._Title = None
        self._JQuery =None
        self._JQueryUi =None
        
        self.Meta_Item("viewport", "width=device-width, initial-scale=1")


        return
        
    def Title(self, *s):
        if self._Title is None:
            self._Title= asTitle(self, *s)
        return self._Title
        
    def Comment(self):
        return asComment(self)
        
    def Meta_Charset(self, charset=None):
        return asMeta(self, charset=charset)
    
    def Meta_Item(self, _name=None, _content=None):
        return asMeta(self, _name=_name, _content=_content)
    
    def Meta_HttpEquiv(self, http_equiv=None, content=None):
        return asMeta(self, http_equiv=http_equiv, content=content)
    
          
    def JQuery(self):
        if self._JQuery is None:
            self._JQuery = asJQuery(self)
        return self._JQuery
        
        
    def JQueryUi(self):
        if self._JQueryUi is None:
            self.JQuery()
            self._JQueryUi = asJQueryUi(self)
        return self._JQueryUi
    pass
    
    
class _Content_():
    
    pass
    
class asButton(asTag):
    
    def __init__(self, parent, **attrs):
        super().__init__(parent, _w.Button, sbreak=True, **attrs)       
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

class asImage(asTag):
    
    def __init__(self, parent, src,
    	                 width=None,
    	                 heigth=None,
    	                 **attrs
    	             ):
        super().__init__(parent, _w.Img, sbreak=True, **attrs)       
        return
        
    pass
    
class asHeading(asTag):
    
    def __init__(self, parent, level=1, **attrs):
        super().__init__(parent, "H"+str(level), sbreak=True, **attrs)
        return
    
    pass
    
class asBlock(asTag, _Content_):
    
    def __init__(self, parent, **attrs):
        super().__init__(parent, tag=None, sbreak=True, **attrs)
        return    
    
    pass
    
class asParagraph(asTag, _Content_):
  
    def __init__(self, parent, **attrs):
        super().__init__(parent, tag="P", sbreak=True, **attrs)
        return    
        
    pass
   


class asDiv(asTag):
    
    def __init__(self, parent,
    	                   **attrs    	                 
    	             ):
        super().__init__(parent, _w.Div, sbreak=True, **attrs)       
        return
        
    pass
    
class asPanel(asBlock):
    
    def __init__(self, parent, title=None, **attrs):
        super().__init__(parent, **attrs)
        self._Heading=None
        self._Contents=None
        if title is not None:
            self.Heading(title)
        return    
    
    def Heading(self, title=None):
        if self._Heading is None:
            self._Heading=asHeading(self, level=3)
        if title is not None:
            self._Heading(title)
        return self._Heading
    
    @property 
    def Contents(self):
        if self._Contents is None:
            p=asDiv(self)            
            self._Contents=p
        return self._Contents
    
    pass
    
  
class asPanelGroup(asTag):
    
    def __init__(self, parent, _id=next_id(), **attrs):
        super().__init__(parent, _w.Div, _id=_id, **attrs)
        h=parent.Root.Head()
        s=h.JQueryUi()       
        s.InitializeFor("PanelGroup", self)
        return
        
    def Panel(self, title):
        return asPanel(self, title)
        
        
    def doInitialize(self, out, _indent=0):
        o={
        	  "collapsible": True,
          "heightStyle": "content"
        	  }
        o=json.dumps(o)
        DEBUG.ID(self.ID)
        self.writeout_part('$( "#'+self.ID+'" ).accordion('+o+');',out, _indent)
        return
           
        
    pass

class asListItem(asTag):
    
    def __init__(self, parent):
        super().__init__(parent, _w.Li)
        return
    
    pass

class asMenu(asTag):
    
    def __init__(self, parent, _id=next_id(), **attrs):
        super().__init__(parent, tag=_w.Ul, _id=_id, **attrs)
        h=parent.Root.Head()
        s=h.JQueryUi()
        si=s.InitializeFor(_id)
        
        return
        
    def doInitialize(self, out, _indent=0):       
        self.writeout_part('$( "#'+self.ID+'" ).menu();',out, _indent)
        return
           
    def MenuItem(self):
        return asMenuItem()
        
    
    pass
    
class asTab():
    
    pass

class asTabGroup():
    
    def __init__(self, parent, _id=next_id(), **attrs):
        super().__init__(parent, _w.Div, _id=_id, **attrs)
        h=parent.Root.Head()
        s=h.JQueryUi()       
        s.InitializeFor("TabGroup", self)
        self._Tab=None
        self._Contents=None
        return
    
    def doInitialize(self, out, _indent=0):
        o={
        	  "collapsible": True,
          "heightStyle": "content"
        	  }
        o=json.dumps(o)        
        self.writeout_part('$( "#'+self.ID+'" ).tabs('+o+');',out, _indent)
        return
    
    pass
    
    
class asButtonGroup():
    
    
    
    pass
    
class asRadioButton():
    
    
    pass
    
class asFillbar():
    
    pass
    
class asCheckbox():
    
    pass
    
class asTable():
    
    pass
    
    
class asSelectbox():
    pass
    
class _Content_(_Content_):
    
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
        
    def PanelGroup(self, **attrs):       
        return asPanelGroup(self, **attrs)
        
        
    def Heading(self, level=1, **attrs):
        return asheading(self, level=level, **attrs)
        
    def Paragraph(self, **ttrs):
        return asParagraph(self, **attrs)
        
    pass
    
class asBody(asTag, _Content_):
    
    def __init__(self, parent):
        super().__init__(parent, _w.Body, sbreak=True)       
        return
        
         
    pass
    
    

class Html(asTag):
    
    
    def __init__(self, lang="en"):
        super().__init__(None, _w.Html, sbreak=True)   
        self(lang=lang)    
        self._Head = None
        self._Body = None
        return
    
    def prefix(self, out):
        out.write("<!DOCTYPE Html>\n")   
        return
            
    def Head(self):
        if self._Head is None:
            self._Head=asHead(self)
        return self._Head
        
    def Body(self):
        if self._Body is None:
            self._Body = asBody(self)
        return self._Body
    
    pass



if __name__ == "__main__":
    
      
    from Node.EmulateWsgi import EmulateWsgi 
    
    css = File.Input.Load((_w.Styles,"Node.css"), pwd=__file__)
    
    h=None
    with Html() as pg:
        h=pg
        pg.ID="23"
        with pg.Head() as hd:
            hd.Comment()
            hd.Meta_Charset(_w.UTF_8)
            hd.Meta_HttpEquiv(_w.Description, "teste de pagina")
            hd.Title("xxx")
            #hd.Style(css)
            hd.Stylesheet("/Styles/Node.css")
        with pg.Body() as bd:
            bd("xxxxxxxx")
            bd.Div(_class="s")
            p=bd.PanelGroup()
            p1=p.Panel("panel 1")
            p1.Contents("asdfvcdth jjuhbyg")
            p2=p.Panel("panel 2")
            p2.Contents("455454556")
            p3=p.Panel("panel 3")
            p3.Contents("hjhyujb")




    print(str(h))
    
    def handler(env, begin_response):
        global h
        r = str(h).encode()
        hh=(("content-type", "text/html"),) 
        begin_response("200 ok", hh)
        
        return [r]
    
    
    EmulateWsgi.Start(name="Html", handler=handler)



####