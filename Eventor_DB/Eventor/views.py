from django.shortcuts import render
from .forms import Participant , EventHolder ,  Comment , Location


def participant(request):
    if request.method == 'POST':
        form = Participant(request.POST)
        print(form.data['name'])
        if form.is_valid():
            print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    else:
        form = Participant()
    return render(request, 'participant.html', {'form': form})

def eventholder(request):
    if request.method == 'POST':
        form = EventHolder(request.POST)
        print(form.data['first_name'])
        if form.is_valid():
            print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    else:
        form = EventHolder()
    return render(request, 'eventholder.html', {'form': form})
    
def comment(request):
    if request.method == 'POST':
        form = Comment(request.POST)
        print(form.data['name'])
        if form.is_valid():
            print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    else:
        form = Comment()
    return render(request, 'comment.html', {'form': form})

def location(request):
    if request.method == 'POST':
        form = Location(request.POST)
        print(form.data['name'])
        if form.is_valid():
            print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    else:
        form = Location()
    return render(request, 'location.html', {'form': form})

# def ticket(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def discountcode(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def event(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def transaction(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def participate(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def follow(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def commenting(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})

# def event_description(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         print(form.data['name'])
#         if form.is_valid():
#             print("aaaaaaaaaaaaaaaaaaaaaaaaaa")
#     else:
#         form = ContactForm()
#     return render(request, 'home.html', {'form': form})