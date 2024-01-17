# Import necessary modules
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



# Create your views here.

# Function based view
# def index(request):    
#     items = Item.objects.all()   
#     context = {
#         'items': items
#     }
#     return render(request=request, template_name='food/index.html', context=context)

# def detail(request, item_id):
#     item = Item.objects.get(id=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request=request, template_name='food/detail.html', context=context)


# Class based view
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'


# Class based detail view
class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'


@login_required
def add_item(request):
    forms = ItemForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('food:index')
    return render(request=request, template_name='food/add_item.html', context = {'form': forms})


@login_required
def edit_item(request, item_id):
    item = Item.objects.get(id = item_id)
    form = ItemForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request=request, template_name='food/edit_item.html', context={'form': form})


@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id = item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request=request, template_name='food/delete_item.html', context={'item': item})

