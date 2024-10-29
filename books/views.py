from django.shortcuts import get_object_or_404

from .models import About, Privacy_policy, Terms_condition, Contact, Comment, PostImage, Posts
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .forms import EmailForm

class AboutList(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'


class PostListView(ListView):
    model = Posts
    template_name = 'list.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.model
        return context

    def get_success_url(self):
        return reverse_lazy('post_detail')


class PostDetailView(DetailView, FormView):
    model = Posts
    template_name = 'post-detail.html'
    context_object_name = 'detail'
    form_class = EmailForm

    def get_object(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        slug = self.kwargs['slug']
        return get_object_or_404(
            Posts,
            slug=slug,
            date__year=year,
            date__month=month,
            date__day=day,
        )


class PrivacyListView(ListView):
    model = Privacy_policy
    template_name = 'privacy-policy.html'
    context_object_name = 'form'


class Terms_conditionsListView(ListView):
    model = Terms_condition
    template_name = 'terms-conditions.html'
    context_object_name = 'form'

class EmailSendView(FormView):
    template_name = 'contact.html'
    form_class = EmailForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        comments = form.cleaned_data['comments']

        # Email yuborish
        send_mail(
            subject=f'Post from {name}',
            message=comments,
            from_email='erkayevazuhra6@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
        return super().form_valid(form)




class IndexListView(ListView):
    model = Posts
    template_name = 'index.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Posts.objects.all()