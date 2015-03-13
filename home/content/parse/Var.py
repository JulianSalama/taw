#used to mark a variables in text. But I would not use this.

from Template import Template

class Var(Template):
  def toHTML(self, option=''):
    return "<div id='"+option+"'>"

class VarName(Template):
  def toHTML(self, option=''):
    return option

class EndVar(Template):
  def toHTML(self, option=''):
    return "</div>" + option
