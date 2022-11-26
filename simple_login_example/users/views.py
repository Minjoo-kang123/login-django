from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
import json
from django.utils.datastructures import MultiValueDictKeyError
 
'''def login(request):
    data = json.dumps(request.GET) #문자열로 바꿔주는 처리 필요
    return HttpResponse(data)

def login_detail(request, id):
    return HttpResponse(f'user id는 {id} 입니다.')'''


def login(request):
    user_data ={
        'username' : 'python',
        'password' : 'django'
    }
    context = {
        'method' : request.method,
        'is_valid' : True
    }

    if request.method == 'GET':
        return render(request, 'users/login.html', context)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == '': 
            context['is_vaild'] = False           
        if password == '':
            context['is_valid'] = False
        if username != user_data['username']:
            context['is_vaild'] = False
        if password != user_data['password']:
            context['is_vaild'] = False

        if context['is_valid']:
            response = redirect('pages:index')
            response.set_cookie('is_login', True)
            response.set_cookie('username', user_data['username'])
            response.set_cookie('password', user_data['password'])

            return response
        return render(request, 'users/login.html', context)


def login_detail(request, id):
    return HttpResponse('user id 는' + str(id) + '입니다.')

def index(request,):
    return render(request, 'index.html')