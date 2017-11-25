from pygments import highlight
from pygments.lexers import XmlLexer
from pygments.formatters import HtmlFormatter
import lxml.etree as et
from uuid import uuid4

HTML_TEMPLATE = """<div class={}> <style>
{}
</style>
{}
</div>
"""

class XML:
    
    def __init__(self, in_obj, style='default'):
        if isinstance(in_obj, str):
            self.text = in_obj.encode('utf-8')
        elif isinstance(in_obj, et._Element):
            self.text = et.tostring(in_obj)
        elif isinstance(in_obj, et._ElementTree):
            self.text = et.tostring(in_obj.getroot())
        else: # assume isinstance(in_obj, bytes)
            self.text = in_obj
        self.style = style
        self.formatter = HtmlFormatter(style=self.style)
        self.uuid_class = "a"+str(self.uuid)
    
    @property
    def style_css(self):
        temp_css = self.formatter.get_style_defs()
        css_list = [f"div.{self.uuid_class} {x}" for x in temp_css.split("\n")]
        return "\n".join(css_list)

    @property
    def uuid(self):
        return uuid4()
    
    def _repr_html_(self):
        content = highlight(self.text, XmlLexer(), self.formatter)
        return HTML_TEMPLATE.format(self.uuid_class, self.style_css, content)