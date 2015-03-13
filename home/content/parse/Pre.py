# creates a pre tag

from Template import Template

class Pre(Template):
  def toHTML(self, option=''):
    return "<pre class='padded_left'>" + option

class EndPre(Template):
  def toHTML(self, option=''):
    return "</pre>" + option
