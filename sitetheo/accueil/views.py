from django.shortcuts import render

def home(request):
    return render(request, 'base.html', {'section': 'home'})

def formation(request):
    return render(request, 'formation.html', {'section': 'formation'})

def experience(request):
    return render(request, 'experience.html', {'section': 'experience'})

def competences(request):
    return render(request, 'competences.html', {'section': 'competences'})
