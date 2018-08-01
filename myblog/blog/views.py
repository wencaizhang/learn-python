from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 每个响应对应一个函数，函数必须返回一个响应
# 函数必须存在一个参数，一般约定为 request
# 每个响应函数（响应）对应一个 url
def index(request):
    return render(request, 'index.html', { 'hello': 'hello python' })
