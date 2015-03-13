# create a link to trigger the next slide

from Template import Template

class Next(Template):
  def toHTML(self, option=''):
    return "<div class='link next'>" + option

class EndNext(Template):
  def toHTML(self, option=''):
    return "</div>" + option
