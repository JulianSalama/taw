# adds text, used in specific situation.

from Template import Template

class Text(Template):
  def toHTML(self, option=''):
    return option

class EndText(Template):
  def toHTML(self, option=''):
    return ""
