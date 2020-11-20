from django.shortcuts import render, HttpResponse

def paginaInicial(request):
    return HttpResponse("Bem vindo a pagina do app de contas")
def login(request):
    return HttpResponse("Bem vindo a pagina de login")