from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from .models import AD, Author
from .filters import ADFilter
from .forms import ADForm, CommentForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


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

class ADDetailView(FormMixin, DetailView):
    model = AD
    template_name = 'AD/one_post.html'
    context_object_name = 'one'
    queryset = AD.objects.all()
    form_class = CommentForm
#Комментарии
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.commentAD = self.get_object()
        self.object.commentUser = self.request.user
        self.object.save()
        return super().form_valid(form)
    def get_success_url(self, **kwargs):
        return reverse_lazy('AD:one', kwargs={'pk':self.get_object().id})
    
class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = AD.objects.get(pk=pk)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if is_dislike:
            post.dislikes.remove(request.user)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('AD:one', args=[str(pk)]))

class AddDislike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = AD.objects.get(pk=pk)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        return HttpResponseRedirect(reverse('AD:one', args=[str(pk)]))


class ADCreateView(CreateView, PermissionRequiredMixin):

    template_name = 'AD/AD_add.html'
    model = AD
    form_class = ADForm
  

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Author.objects.get_or_create(user=user)[0]
            post.save()
            return self.form_valid(form)
        return redirect('AD:posts')
    
    
class ADUpdateView( UpdateView, PermissionRequiredMixin):
    template_name = 'AD/AD_edit.html'
    form_class = ADForm
    success_url = '/posts/one_post/{id}'
       
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return AD.objects.get(pk=id)
    






    