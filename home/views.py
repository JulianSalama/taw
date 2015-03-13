# Create your views here.
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import RequestContext, Template
from home.models import Dictionary, Menue, Post, TextPost, User_Post_Link, User_Slide_Link
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib import auth
from django.contrib.auth.models import User

from parse import main

import sys

def setArgs(request, categorie, chapter):
  args = RequestContext(request, setPost(chapter) if chapter else {})
  args.update(csrf(request))
  args['chapter'] = chapter
  args['menues'] = Menue.objects.all().order_by('id') #order by something
  args['show_menues'] = categorie
  
  args['base_url'] = "http://" + request.META['HTTP_HOST']
  args['complete_url'] = args['base_url'] + request.path_info
  args['logged_in'] = request.user.is_authenticated()
  if args['logged_in']:
    args['user'] = request.user
    return setUserPreferences(args, request)
  else:
    args['user_slide'] = 0
    args['user_post'] = {}
  return args

def setUserPreferences(args, request):
  try:
    upls = User_Post_Link.objects.filter(user=request.user)
    args['user_post'] = list()
    for upl in upls:
      args['user_post'].append(str(upl.post.name))  
  except User_Post_Link.DoesNotExist:
    args['user_post'] = list('')
  try:
    args['user_slide'] = User_Slide_Link.objects.get(user=request.user, page=args['chapter']).slides
  except User_Slide_Link.DoesNotExist:
    args['user_slide'] = 0
  return args

def setPost(chapter):
  args = {}
  try :
    args['post'] = Post.objects.get(name = " ".join(chapter.split('_')))
  except Post.DoesNotExist:
    args['post'] = Post.objects.get(name = "servers")
  try:
    args['content'] = main(args['post'].content)
  except:
    args['content'] = "Unexpected error:", str(sys.exc_info()[0])
  args['content_as_string'] = args['post'].content
  return args

def home(request, categorie="", chapter=""):
  args = setArgs(request, categorie, chapter)
  #if chapter == "":
  #  return render_to_response("home/about.html", args)
  
  return render_to_response('home/content/talkAboutWeb2.html', args)

def fsignup(request):
  args = setArgs(request, "", "")
  email = request.POST.get('email', False)
  first = request.POST.get('fname', False)
  last = request.POST.get('lname',False)
  password = request.POST.get('password', False)
  if email and first and last and password:
    user = User.objects.create(username=email, first_name=first, last_name=last, email=email)
    user.set_password(password)
    user.save()
    
  return render_to_response("home/content/talkAboutWeb2.html", args)
  

def login(request):
  args = setArgs(request, "", "")
  email = request.POST.get('email', False)
  password = request.POST.get('password', False)
  if email and password:
    user = auth.authenticate(username=email, password=password) 
    if user:
      auth.login(request, user)
  return home(request)

def about(request):
  args = setArgs(request, "", "about")

  return render_to_response("home/content/talkAboutWeb2.html", args)

def logout(request):
  auth.logout(request)
  return home(request)

def user_post(request, categorie, chapter):
  if request.is_ajax():
    try:
      post = TextPost.objects.get(name=request.POST.get('name'))
    except Post.DoesNotExist:
      return HttpResponse(simplejson.dumps(""), mimetype='application/javascript')
    try:
      User_Post_Link.objects.get(post=post, user=request.user)
    except User_Post_Link.DoesNotExist:
      upl = User_Post_Link()
      upl.post = post
      upl.user = request.user
      upl.save()

  return HttpResponse(simplejson.dumps(""), mimetype='application/javascript')

def user_slide(request, categorie, chapter):
  if request.is_ajax():
    try:
      usl = User_Slide_Link.objects.get(user=request.user, page=chapter)
      usl.slides += 1
      usl.save()
    except User_Slide_Link.DoesNotExist:
      usl = User_Slide_Link()
      usl.page = chapter
      usl.user = request.user
      usl.slides = 1
      usl.save()
  return HttpResponse(simplejson.dumps(""), mimetype='application/javascript')

def dev(request, chapter=""):
  args = RequestContext(request, setPost(chapter) if chapter else {})
  args.update(csrf(request))
  args['chapter'] = chapter
  args['base_url'] = "http://" + request.META['HTTP_HOST']
  args['complete_url'] = args['base_url'] + request.path_info
  args['logged_in'] = request.user.is_authenticated()
  if args['logged_in']:
    args['user'] = request.user
    setUserPreferences(args, request)
  else:
    args['user_slide'] = 0
    args['user_post'] = {}

  if(request.POST.get("test", False)):
    if(request.POST.get('test_content', False)):
      args['content_as_string'] = request.POST.get('test_content', False)
      try:
        args['content'] = main(args['content_as_string'])
      except:
        args['content'] = "an error occured parsing."
      args['testing'] = True
    else:
      args['testing'] = False
  
  if(request.POST.get('save', False)):
    if(request.POST.get('test_content', False)):
      try :
        post = Post.objects.get(name = " ".join(chapter.split('_')))
      except Post.DoesNotExist:
        print "post does not exist"
        post = Post()
      post.name = " ".join(chapter.split('_'))
      post.content = args['content_as_string'] = request.POST.get('test_content', False)
      post.save()
      try:
        args['content'] = main(args['content_as_string'])
      except:
        args['content'] = "an error occured."
        args['testing'] = False
      post.content = args['content_as_string']
      post.save()
    else:
      args['testing'] = False
  
  return render_to_response("home/content/dev.html", args)

def database(request):
  return render_to_response("home/database.html", {})
  

#weird old stuff
def dictionary(request):
  args = RequestContext(request)
  if request.method == 'POST':
    if request.user.is_authenticated():
      args['word'] = word = str(request.POST.get('s', False))        
      if word:
        try:
          p = Dictionary.objects.get(name=word)
        except:
          p = None
          if p:
            args['name'] = p.name
            args['description'] = p.description
            args['no_definition'] = False
            return args['description']
          else:
            args['no_definition'] = True
            args['description'] = "Sorry, no word found."
            return args['description']
        else:
          return "Sorry, you need to be logged in."
    return render_to_string('dictionary/home.html', args)


def chapter(request, chapter_id, lesson_id):
  args = {}
  args['chapter'] = chapter_id
  args['lesson'] = lesson_id
  return render_to_string('home/'+chapter_id+'/'+lesson_id+'.html', args)



def home2(request, chapter_id=0, lesson_id=0):
    #pass blocks as arguments from apps.
  args = {}
  args['user'] = request.user.is_authenticated()    
  if request.is_ajax():
    if 's' in request.POST:
      c = dictionary(request)
      return HttpResponse(simplejson.dumps(c), mimetype='application/javascript')
        
    if request.method == 'GET':
      t = get_template('default.html')
      args['dictionary'] = dictionary(request)
      if chapter_id and lesson_id:
        args['chapter'] = chapter(request, chapter_id, lesson_id)
        args['var1'] = "Chapter" #stupid
        args['var2'] = 'd'
    

    return render_to_response('home/content/talk_test.html', args)

def analytics(request):
  if request.is_ajax():
    if 'like' in request.POST:
      #persist one like in db;
      return HttpResponse("hello");      

