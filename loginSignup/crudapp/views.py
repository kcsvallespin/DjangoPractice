from django.shortcuts import render, redirect, get_object_or_404
from .models import TestTable

# List all items
def item_list(request):
    items = TestTable.objects.all()
    return render(request, 'crudapp/item_list.html', {'items': items})

# Create new item
def item_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        TestTable.objects.create(name=name)
        return redirect('crudapp:item_list')
    return render(request, 'crudapp/item_form.html', {'action': 'Create'})

# Update existing item
def item_update(request, id):
    item = get_object_or_404(TestTable, id=id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.save()
        return redirect('crudapp:item_list')
    return render(request, 'crudapp/item_form.html', {'item': item, 'action': 'Update'})

# Delete item
def item_delete(request, id):
    item = get_object_or_404(TestTable, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('crudapp:item_list')
    return render(request, 'crudapp/item_confirm_delete.html', {'item': item})