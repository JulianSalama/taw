# creates a separator between slides.

from Template import Template

class Separator(Template):
  def toHTML(self, option=''):
    return "<div class='shadtop'>"

class EndSeparator(Template):
  def toHTML(self, option=''):
    return "</div>"
