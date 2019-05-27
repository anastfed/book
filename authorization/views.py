from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from authorization.forms import MyUserCreationForm, MyUserChangeForm
from django.http import JsonResponse

def user_login(request):
    if request.is_ajax():
        print('AJAX login', request.META['HTTP_REFERER'])
        context = {
            'login': reverse('auth:login'),
        }

        return JsonResponse(context)

    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['psw']
        print(login, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            print('пользователь найден: ', user)
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'authorization/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_register(request):
    register_form = MyUserCreationForm()


    if request.method == "POST":
        register_form = MyUserCreationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = MyUserCreationForm()

    context = {
        'register_form': register_form
    }

    return render(request, 'authorization/register.html', context)



def user_edit(request):
    if request.method == "POST":
        edit_form = MyUserChangeForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = MyUserChangeForm(instance=request.user)


    context = {
        'edit_form': edit_form
    }

    return render(request, 'authorization/edit.html', context)


