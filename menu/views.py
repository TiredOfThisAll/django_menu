from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader


def main_page(request):
    return HttpResponseRedirect("food/")

def food(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def fruit(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def vegetables(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def berries(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def orange(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def clothes(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def hats(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def tops(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def pants(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def boots(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))

def ushanka(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render(request=request, context={"menu_name": "nav_menu"}))
