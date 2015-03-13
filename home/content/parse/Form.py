# create a form, and upon enter sends an ajax request to save the right answer.

from Template import Template

class Form(Template):
  def toHTML(self, option=''):
    #checkmark to do <img src='images/checkmarks.png'/>
    return "<form action='.' class='inactive'><input type='text'/><div class='answer'>" + option

class Name(Template):
  def toHTML(self, option=''):
    return option

class EndForm(Template):
  def toHTML(self, option=''):
    return "</div></form>" + option
