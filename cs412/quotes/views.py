# File: quotes/views.py
# Author: Trevor Stellmach, tstell@bu.edu (09/10/26)
# Description: Quotes site views file

import time
import random

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

quotes = [      # quote selections
    "In 1984 I was hospitalized for approaching perfection.",
    "Half hours on Earth, what are they worth? I don't know.",
    "Sin and gravity drag me down to sleep to dream of trains across the sea.",
    "No I didn't really want to die, I only wanted to die in your eyes."
]

images = [      # image selections
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXIJlDqmJpz9DPMr30o5EwEqxptxtwFJrZBZmoDzRHMQ&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnSQNk0owa70MVeKjjou-ulgp_lgZTyO6alC99BzDGSw&s=10",
    "https://upload.wikimedia.org/wikipedia/commons/1/1d/The_Silver_Jews_%282006%29_%28David_Berman_crop%29.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=original",
    "https://media.vanityfair.com/photos/5d4c886a4ac64700072d4743/master/w_2560%2Cc_limit/David-Berman-Musician.jpg"
]

# Create your views here.
def quote(request):
    """ responds to 'quote' url """

    # context variables
    context = {
        "quote": quotes[random.randint(0, len(quotes) - 1)],
        "image": images[random.randint(0, len(images) - 1)]
    }

    template_name = "quotes/quote.html"     # references quote html file

    return render(request, template_name, context)

def show_all(request):
    """ responds to 'show all' url """

    #context variables
    context = {
        "quotes": quotes,
        "images": images
    }

    template_name = "quotes/show_all.html"  # references show all html file

    return render(request, template_name, context)

def about(request):
    """ responds to 'about' url"""

    template_name = "quotes/about.html" # references about html file

    return render(request, template_name)
