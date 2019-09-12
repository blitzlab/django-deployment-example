from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title':'Home Page', 'text':'Hello World', 'number': 100}
    return render(request, 'basic_app/index.html', context)

def other(request):
    context = {'title':'Other Page'}
    return render(request, 'basic_app/other.html', context)

def relative(request):
    context = {'title':'Relative Page'}
    return render(request, 'basic_app/relative_url_templates.html', context)
