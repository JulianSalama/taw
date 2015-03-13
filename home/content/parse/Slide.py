# create a slide

from Template import Template

class Slide(Template):
  def toHTML(self, option=''):
    return "<div class='slide'>" + option

class EndSlide(Template):
  def toHTML(self, option=''):
    return "</div>" + option
