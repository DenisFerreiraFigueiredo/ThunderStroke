#!/bin/false
#
#

import sys
import os
import copy

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

import json
import xml
import yaml

# import StringIO
from io import StringIO

_w._write = _w._i('write')

_w.MARKUP = _w._i('Markup')

def isWritable(s):
    return hasattr(s, _w._write)


class Tools():

    @staticmethod
    def fromJson(s):
        return

    @staticmethod
    def fromXml(s):
        return

    @staticmethod
    def fromYaml(s):
        return

    @staticmethod
    def fromHtml(s):
        return

    @staticmethod
    def _Load(path, fn):
        if isinstance(path, str):
           path = pathlib.Path(path)
        if path.is_file():
            r = path.open('r').read()
            return fn(r)
        return None

    @staticmethod
    def LoadJson(path):
        return Markup.Load(path, Html.fromJson)

    @staticmethod
    def LoadXml(path):
        return Markup.Load(path, Html.fromXml)

    @staticmethod
    def LoadYaml(path):
        return Markup.Load(path, Html.fromYaml)

    @staticmethod
    def LoadHtml(path):
        return Html.Load(path, Html.fromHtml)

    @staticmethod
    def LoadFrom(src):
        if isinstance(pathlib.Path, src):
            s = src.suffix
        if s == Filetypes.JSON:
            return Html.loadJson(src)
        elif s == Filetypes.XML:
            return Html.loadXml(src)
        elif s == Filetypes.YAML:
            return Html.loadYaml(src)
        elif s == Filetypes.HTML:
            return Html.loadHtml(src)
        elif isinstance(src, Html):
            pass
        elif isinstance(src, dict):
            pass
        elif isinstance(src, str):
            pass
        else:
            pass

        return None

    pass


class EmptyTag(dict):

    def __init__(self, parent, name=None, breakable=False, indentable=False, **opts):
        self._Parent = parent
        self._Name = name
        self._Contents = None
        self._Breakable = breakable
        self._Indentable = indentable

        if isinstance(parent, EmptyTag): # asattr(parent, '_parent_'):
	            # print('self=', type(self), 'Parent=', type(parent))
            parent.append(self)

        if len(opts)>0:
            # print("opts=", opts)
            for e in opts:
                ee = '_'+e.capitalize()
                vv = opts[e]
                fn = getattr(self, ee, None)
                if callable(fn):
                    fn(vv)

        return

    @property
    def Parent(self):
        return self._Parent

    def __setattr__(self, item, v):
        if isinstance(item, str):
            if item == item.upper():
                if len(item)>1 and  '_' in item[1:]:
                    item = item.replace('_', '-')
                item = item.title()
                self[item] = v
                return
#		raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

        return super().__setattr__(item, v)

    def Set(self, item, *s):
        if len(s) == 0:
            return self.get(item, None)
        elif len(s) == 1:
            self[item] = s[0]
        else:
            self[item] = s

        return self

    def __getattr__(self, item):
        if isinstance(item, str):
            if item == item.upper():
                if len(item)>1 and '_' in item[1:]:
                    i = item.replace('_', '-')
                else:
                    i = item
                i = Symbols(i.title())
                return self[i]
        raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

        return super().__getattr__(item)

    @property
    def Name(self):
        return self._Name

    @property
    def Contents(self):
        return self._Contents

    @property
    def writePrefix(self):
        return None

    @property
    def writeSulfix(self):
        return None

    def writeCloseTag(self, out=None):
        if out is None:
            out = StringIO()
        if isWritable(out):
            out.write('>')
        return out

    def write(self, out=None):
        # print('name=', self.Name)
        if out is None:
            out = StringIO()

        if isWritable(out):
            s = self.writePrefix
            if s is not None:
                out.write(s)
            _n = self.Name
            if _n is not None:
                out.write('<')
                out.write(_n)
                if len(self) > 0:
					for e in self:
						v = self[e]
						out.write(' ')
						out.write(e)
						if not v is None:
							out.write('=')
							if isWritable(v):
								v.write(out)
							else:
								if isinstance(v, int):
									out.write(str(v))
								elif isinstance(v, float):
									out.write(str(v))
								elif isinstance(v, (str, bytes)):
									out.write('"')
									out.write(v)
									out.write('"')
								else:
									out.write('"')
									out.write(str(v))
									out.write('"')
				self.writeCloseTag(out)

			if self._Breakable:
				out.write('\n')

		return out

	def Attribute(self, name, val=None):
		name = name.title()
		r = self.get(name, None)
		if r is None:
			r = self[name] = Attribute(val)
		return self

	Attr = Attribute

	def append(self, s):
	#	print('append -->', s)
		if self._contents_ is None:
			self._contents_ = [s]
		else:
			self._contents_.append(s)
		return self

	def On(self, event, s):
		e = 'on' + event
		self[e] = s
		return self

	def __str__(self):
		s = StringIO()
		self.write(s)
		return s.getvalue()

	def __repr__(self):
		s = '('
		s += self.Name
		s += ' '
		f1 = False
		if len(self)>0:
			for e in self:
				if f1:
					s += ' '
				f1 = True
				v = self[e]
				s += e
				if v is not None:
					s += '="'+v+'"'

		if self.Contents is not None:
			s += '['
			f2 = False
			for e in self.Contents:
				if f2:
					s += ' '
				f2 = True
				s += repr(e)
			s += '] '
		s += ')'
		return s

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, tb=None):
		if tb is None:
			pass # no exception
		else:
			# Exception occurred, so rollback.
			pass
		return False

	pass


class SingleTag(EmptyTag):

	def __init__(self, parent, name, breakable=False, **opts):
		EmptyTag.__init__(self, parent, name, breakable=breakable, single=True, **opts)
		return

	def writeClosseTag(self, out):
		if isWritable(out):
			out.write('/>')
		return

	pass


class Tag(EmptyTag):

	def __init__(self, parent, name, breakable=False, **opts):
		EmptyTag.__init__(self, parent, name, breakable=breakable, **opts)
		return

	def write(self, out=None, breakable=None, ident=None):
		out = super().write(out)
		if isWritable(out):
			if self._contents_ and len(self._contents_) > 0:
				for e in self._contents_:
					if isWritable(e):
						e.write(out, breakable=breakable, ident=ident)
					else:
						out.write(e)
				if self._Breakable:
					out.write('\n')

			if self.Name is not None:
				out.write('</')
				out.write(self.Name)
				out.write('>')

		return self

	pass


###
