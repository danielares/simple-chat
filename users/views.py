from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from .forms import SignupForm


class SignupView(CreateView):
    template_name = 'registration/sign-up.html'
    form_class = SignupForm
    success_url = reverse_lazy('index')
    

@method_decorator(login_required, name='dispatch')
class UpdateUserView(UpdateView):
    template_name = 'registration/update-user.html'
    model =  User
    fields = ['first_name', 'last_name', 'username']
    success_url = reverse_lazy('index')
    
    def get(self, request, *args, **kwargs):
        user_id = int(self.request.user.id)
        user_id_path_url = int(self.request.get_full_path().split('/')[3])
        if user_id != user_id_path_url:
            return redirect('/accounts/update-user/' + str(user_id))
        else:
            return super().get(request, *args, **kwargs)
        
    def post(self, request, **kwargs):
        user_id = int(self.request.user.id)
        user_id_path_url = int(self.request.get_full_path().split('/')[3])
        
        if user_id == user_id_path_url:
            user = request.user
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.username = request.POST['username']
            user.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
        else:
            messages.warning(request, 'Você não tem autorização para isso.')
        return render(request, 'index.html')