from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

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

    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']

        if username != user_data['username']:
            return HttpResponse('유저 아이디가 올바르지 않습니다.')
        if password != user_data['password']:
            return HttpResponse('비밀번호가 올바르지 않습니다.')

        return HttpResponse('로그인 성공')    
