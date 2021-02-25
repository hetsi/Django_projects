from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcome(req, name):
    message = "<h2> Mr./Ms. "
    message+= name+" ! "
    message+="Welcome to Shopping app <h2>"
    return HttpResponse(message)

def get_items():
    items = []
    with open('./shoppingApp/items.csv', 'r') as file:
        for line in file.readlines():
            item = {}
            info = (line.rstrip().split(","))
            item["name"] = info[0]
            item["quantity"] = info[1]
            items.append(item)
    return items

def get_all_items(req):
    items = get_items()
    return render(req,'shoppingApp/cart.html',{'cart':items})

def formatting_for_write(items):
    write_str = ""
    for item in items:
        write_str += item['name'] + ',' + item['quantity'] + '\n'
    return write_str.rstrip()

def delete_items(req, name):
    items = get_items()
    new_items = list(filter(lambda x:x['name']!=name, items))
    write_format = formatting_for_write(new_items)
    with open('./shoppingApp/items.csv','w+') as f:
        f.write(write_format)

    return HttpResponse('successfully deleted <a href="/shoppingApp/get_all_items"> Go back </a>')
