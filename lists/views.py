from django.shortcuts import render
from lists.models import Item


def home_page(request):
    if (request.method == 'POST'):
        new_item = Item()
        new_item.text = request.POST.get('item_text')
        new_item.save()
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''), })
