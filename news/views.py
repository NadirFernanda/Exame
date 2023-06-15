from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Noticia

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        noticias = Noticia.objects.all()  # Busca todas as notícias do modelo Noticia
        data['noticias'] = noticias  # Adiciona as notícias ao dicionário de contexto
        return data

    #def Noticia(request):
        #noticias= Noticia.objects.all()
        #return render(request, 'Noticia/index.html', {'noticia':noticias})