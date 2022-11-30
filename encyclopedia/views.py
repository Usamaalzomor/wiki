from django.shortcuts import render

from . import util

from markdown2 import markdown

from django.http import HttpResponse




# # normalize entries "lower case the list"
# for entry in range(len(entries_list)):
#     entries_list[entry] = entries_list[entry].lower()


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, entry):
    entry_content = util.get_entry(entry)     

    if not entry_content:
        return render(request, 'encyclopedia/entries.html', {
        "entry_content":"Your Requested Page is not Found"
    })

    conv_entry = markdown(entry_content)

    return render(request, 'encyclopedia/entries.html', {
        "entry_content":conv_entry
    })


def search(request):
    if request.method == "POST":
        entries_list = util.list_entries()
        input = request.POST['q']

        if input in entries_list:
            return entries(request, input)
        else:
            return render(request, 'encyclopedia/search.html')

        
    if request.method == "GET":
        return render(request, 'encyclopedia/search.html')
