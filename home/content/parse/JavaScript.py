# import a template, it is used for animation.
from django.template.loader import render_to_string
from Template import Template

class JavaScript(Template):
  def toHTML(self, option=''):
    return render_to_string('home/extra/'+option)

class EndJavaScript(Template):
  def toHTML(self, option=''):
    return ""
