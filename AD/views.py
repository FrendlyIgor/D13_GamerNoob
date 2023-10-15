from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.models import User
from .models import AD
from .filters import ADFilter
from .forms import ADForm

# Create your views here.

class ADListView(ListView):
    model = AD
    template_name = 'AD/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ADFilter(self.request.GET, queryset=self.get_queryset())
        context['choices'] = AD.how_choise
        context['form'] = ADForm()
        return context

class ADDetailView(DetailView):
    model = AD
    template_name = 'AD/one_post.html'
    context_object_name = 'one_post'
    queryset = AD.objects.all()



    