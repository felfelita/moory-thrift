from django.shortcuts import render
def show_main(request):
    context = {
        'app' : 'Moory Thrift',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
