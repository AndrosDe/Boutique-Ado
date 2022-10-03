'''imports'''
from django.shortcuts import render


def view_bag(request):
    ''' A view the user bag '''

    return render(request, "bag/bag.html")
