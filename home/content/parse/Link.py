# creates an external link and open in new tab.

from Template import Template

class Link(Template):    
  def toHTML(self, option=''):
    return "<div class='link'><div class='window' id='"+option

class EndLink(Template):
  def toHTML(self, option=''):
    return "'>" + option

class Linked(Template):
  def toHTML(self, option=''):
    return "</div></div>" + option
