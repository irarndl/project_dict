from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from .models import Language, Word, Translation
from django import forms
from datetime import date, timedelta    
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_process_view(request):
    username = request.POST['username']
    password = request.POST['password']
    if username=="":
        return HttpResponseRedirect("/login")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/login")


@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def index(request):
    language_list = Language.objects.order_by('name_eng')
    template = loader.get_template('dict/language_select.html')
    context = {'language_list': language_list}
    return HttpResponse(template.render(context, request))


def search_form(request,lang_id):
    word_list = Translation.objects.filter(language_id=lang_id)
    template = loader.get_template('dict/word_select.html')
    context = {'word_list': word_list}
    return HttpResponse(template.render(context, request))


def search(request):
    last_added_terms_list = Translation.objects.order_by("pub_date")
    template = loader.get_template('dict/word_search.html')
    context = {'last_added_terms_list': last_added_terms_list}
    return HttpResponse(template.render(context, request))

def view_the_whole_translation(request, word_id):
    word_list = Translation.objects.filter(word_id=word_id)
    info_list = []
    for word in word_list:
        info_list.append((word, Language.objects.get(id=word.language_id)))
    template = loader.get_template('dict/word_details.html')
    context = {'info_list': info_list}
    return HttpResponse(template.render(context, request))


def searchlist(request):
    query = request.GET.get("query")
    word_list = Translation.objects.filter(translation__startswith=query)
    info_list = []
    for word in word_list:
        info_list.append((word, Language.objects.get(id=word.language_id)))
    context = {'info_list': info_list}
    template = loader.get_template('dict/word_found_list.html')
    return HttpResponse(template.render(context, request))

#def search_for_term_form(request, word_id):
#    search_term = input ("")
#    word_list = Translation.objects.filter(word_id=word_id)
#    if search_term in word_list:
#    template = loader.get_template('dict/word_search.html')
#    context = {'search_term': word_list}
#    return HttpResponse(template.render(context, request))


def view_word(request, word_id):
    word_list = Translation.objects.filter(word_id=word_id)
    info_list = []
    for word in word_list:
        info_list.append((word, Language.objects.get(id=word.language_id)))
    template = loader.get_template('dict/word_details.html')
    context = {'info_list': info_list}
    return HttpResponse(template.render(context, request))


def like_word(request, word_id, translation_id):
    if request.user.is_authenticated:
        translation_to_like=Translation.objects.get(id=translation_id)
        translation_to_like.likes.create(user=request.user)
        
    return redirect('/word/'+str(word_id))
