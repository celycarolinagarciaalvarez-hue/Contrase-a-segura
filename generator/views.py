import random
import string
from django.shortcuts import render

def home(request):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for _ in range(12))
    return render(request, "generator/home.html")