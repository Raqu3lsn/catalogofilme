from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalogo.forms import CatalogoForm, FilmeForm
from models import Catalogo, Filme

class CatalogoListView(ListView):
    model = Catalogo
    template_name = 'catalogo/catalogo_list.html'
    context_object_name = 'catalogos'
    paginate_by = 8
    queryset = Catalogo.objects.order_by('-id')

class CatalogoDetailView(DetailView):
    model = Catalogo
    context_object_name = 'catalogos'
    template_name = 'catalogo/catalogo_detail.html'

class CatalogoCreateView(CreateView):
    model = Catalogo
    form_class = CatalogoForm
    template_name = 'catalogo/catalogo_form.html'
    success_url = reverse_lazy('catalogo_list')

class CatalogoUpdateView(UpdateView):
    model = Catalogo
    fields = ['nome', 'elenco']  
    template_name = 'catalogo/catalogo_form.html'
    success_url = reverse_lazy('catalogo_list')  

class CatalogoDeleteView(DeleteView):
    model = Catalogo
    context_object_name = 'catalogo'
    success_url = reverse_lazy('catalogo_list')  

# musicas crud

class FilmeListView(ListView):
    model = Filme
    template_name = 'filme/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme/filme_detail.html'

class FilmeCreateView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/filme_form.html'
    success_url = reverse_lazy('filme_list')

class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'filme/filme_form.html'
    success_url = reverse_lazy('filme_list')  

class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme/filme_confirm_delete.html'
    success_url = reverse_lazy('filme_list')