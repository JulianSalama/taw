import re
from Slide import Slide, EndSlide
from Pre import Pre, EndPre
from Next import Next, EndNext
from Text import Text, EndText
from Form import Form, EndForm, Name
from Link import Link, EndLink, Linked
from Triger import TrigerNext, EndTrigerNext
from JavaScript import JavaScript, EndJavaScript
from BeginNewSlide import BeginNewSlide, EndBeginNewSlide
from Separator import Separator, EndSeparator

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   
   open(outputfile, 'w').write(toHTML(open(inputfile, 'r').read()))
   


if __name__ == "__main__":
   main(sys.argv[1:])




class Tag:
  def __init__(self, name, start, end):
    self.name = name
    self.start = start
    self.end = end
  
  def render(self, option=''):
    return eval(self.name.strip('$$'))(self.start, self.end)
      
def toHTML(content):
  list_of_tags = [Tag(m.group(), m.start(0), m.end(0)).render() for m in re.finditer(re.compile(r"\$\$\w+\$\$"), content)]
  
  l = len(list_of_tags)
  contents = list()
  for i in range(len(list_of_tags)):
    if (i+1 != l):
      contents.append(content[list_of_tags[i].end:list_of_tags[i+1].start])
    else:
      contents.append(content[list_of_tags[i].end:])
      
  return "".join([str(list_of_tags[i].toHTML(contents[i])) for i in range(l)])
  
