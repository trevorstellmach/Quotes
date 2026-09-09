import time
import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    '''Func to respond to the 'home' request'''

    response_text = '''
    <html>
    <h1>Hello, world</h1>jj
    The current time is {time.ctime()}.
    </html>
    '''

    return HttpResponse(response_text)

def home_page(request):
    '''Respond to URL'''

    template_name = 'hw/home.html'
    # a dict of context variables
    context = {
        "time": time.ctime(),
        "letter1": chr(random.randint(65,90)),
        "letter2": chr(random.randint(65,90)),
        "number": random.randint(1,10),
    }
    return render(request, template_name, context)

def about(request):
    '''Respond to URL 'about'''

    template_name = 'hw/about.html'
    # a dict of context variables
    context = {
        "time": time.ctime(),
        "letter1": chr(random.randint(65,90)),
        "letter2": chr(random.randint(65,90)),
        "number": random.randint(1,10),
    }
    return render(request, template_name, context)