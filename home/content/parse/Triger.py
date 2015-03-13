# trigers next slide when a form is entered correctly. 
# TBD: a little more functionality.

from Template import Template

class TrigerNext(Template):    
  def toHTML(self, option=''):
    return "<div class='triger'>" + option

class EndTrigerNext(Template):
  def toHTML(self, option=''):
    return "</div>" + option
