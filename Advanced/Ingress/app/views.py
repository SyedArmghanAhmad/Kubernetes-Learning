# views.py
from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Hello, Ingress!"})

def demo(request):
    return JsonResponse({"message": "Demo endpoint works!"})