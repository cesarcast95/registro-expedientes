from django.shortcuts import render
#Aqui importaos la TemplateView para poder comenzar
from django.views.generic.base import TemplateView

#asi de define una CBV
class HomePageView(TemplateView):
    template_name = "core/home.html"
    #Se redefine el metodo get para devolver el contexto que queramos
    #los *args, **kwars son por buena practica
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'App de Noticias'})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"