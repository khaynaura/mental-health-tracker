from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275310',
        'name': 'Khayla Naura Ulya Luqyana',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)