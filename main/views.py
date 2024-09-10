from django.shortcuts import render
def show_main(request):
    context = {
        'app' : 'Moory Thrift',
        'name': 'Felita Zahra D',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
