# create a default next, endslide, and new slide.

from Template import Template

class BeginNewSlide(Template):    
  def toHTML(self, option=''):
    return "<div class='link next'>" + option + "</div></div><div class='slide'>"

class EndBeginNewSlide(Template):
  def toHTML(self, option=''):
    return option + "</div>"
