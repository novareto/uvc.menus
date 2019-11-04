import collections
import collections.abc
import grokcore.component
import grok

import martian
from martian.util import scan_for_classes
from martian.error import GrokError

import zope.security
from zope.component import queryMultiAdapter, getAdapters 
from grok.interfaces import IGrokView
from zope.interface import Interface, implementer


class menu(martian.Directive):
    scope = martian.CLASS_OR_MODULE
    store = martian.ONCE
    validate = martian.validateInterfaceOrClass

    @classmethod
    def get_default(cls, component, module=None, **data):
        components = list(scan_for_classes(module, IMenu))
        if len(components) == 0:
            raise GrokError(
                "No module-level menu for %r, please use the "
                "'menu' directive." % (component), component)
        elif len(components) == 1:
            component = components[0]
        else:
            raise GrokError(
                "Multiple possible menus for %r, please use the "
                "'menu' directive."
                % (component), component)
        return component
