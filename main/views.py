from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ThriftEntryForm
from main.models import ThriftEntry
def show_main(request):
    thrift_entries = ThriftEntry.objects.all()
    context = {
        'app' : 'Moory Thrift',
        'name': 'Felita Zahra D',
        'class': 'PBP C',
        'thrift_entries': thrift_entries
    }

    return render(request, "main.html", context)

def create_thrift_entry(request):
    form = ThriftEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_thrift_entry.html", context)
# Create your views here.
