from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect  
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

def show_xml(request):
    data = ThriftEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ThriftEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ThriftEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ThriftEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
# Create your views here.
