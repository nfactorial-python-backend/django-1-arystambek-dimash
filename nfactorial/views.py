from django.shortcuts import render
from django.http import HttpResponse


def nfactorial(request):
    return HttpResponse("Hello, nfactorial school!")


def add(request, first, second):
    return HttpResponse(first + second)


def upper_str(request, text: str):
    return HttpResponse(text.upper())


def is_palindrome(request, word):
    return HttpResponse(word == word[::-1])


def calculator(request, first, operation, second):
    operations = {'add': '+', 'sub': '-', 'mult': '*', 'div': '/'}
    if operation in operations:
        try:
            operator = operations[operation]
            return HttpResponse(eval(f"{first}{operator}{second}"))
        except (SyntaxError,ValueError):
            return HttpResponse("Invalid operation or division by zero")
    else:
        return HttpResponse('Invalid operation')
