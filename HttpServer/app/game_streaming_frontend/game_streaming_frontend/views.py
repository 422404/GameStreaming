from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

def index(request):
    return render(request, 'game_streaming_frontend/index.html')
