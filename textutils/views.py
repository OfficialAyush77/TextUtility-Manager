# I have created this File -- By Ayush Anand

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name': 'Ayush', 'place': 'Jupiter'}
    return render(request, 'index.html')


def impLinks(request):
    return HttpResponse('''<h1> IMPORTANT WEBPAGE LINKS </h1> <a href="https://web.whatsapp.com/"> To Open Whatsappp 
    Click Here </a> ''')
    # return HttpResponse('''<a href="https://docs.google.com/document/u/0/?tgif=d"> To Open Google Doc ➡️ Click Here
    # </a> ''') return HttpResponse('''<a href="https://vtop.vitbhopal.ac.in/vtop/initialProcess"> To Open VTOP ➡️
    # Click Here </a> ''') return HttpResponse('''<a href="https://docs.google.com/presentation/u/0/?tgif=d"> To Open
    # Google Slides Click Here </a> ''') return HttpResponse('''<a href="https://fontawesome.com"> To Open Font
    # Awesome ➡️ Click Here </a> ''')


def analyze(request):
    # Get the Text

    global params, analyzed
    mytext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newline = request.POST.get('newline', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in mytext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        mytext = analyzed

    # CONVERT TO UPPERCASE

    if uppercase == "on":
        analyzed = ""
        for char in mytext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To UpperCase', 'converted_text': analyzed}
        mytext = analyzed

    # NEWLINE REMOVER

    if newline == "on":
        analyzed = " "
        for char in mytext:
            analyzed = analyzed + char.strip()
        params = {'purpose': 'Remove Newline from the Strings.', 'removed_text': analyzed}
        mytext = analyzed

        # CHARACTER COUNTER

    if charcount == "on":
        analyzed = ""
        for char in mytext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Character Counter in the entered Strings::-- ', 'counted_text': analyzed}

    if removepunc != "on" and newline != "on" and uppercase != "on" and charcount != "on":
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)


def navigator(request):
    navbar = '''<h1 style=" color: chartreuse;"> IMPORTANT WEBSITES THAT IS USED BY ME EVERYDAY</h1> <br>
                  <li><a href="https://vtop.vitbhopal.ac.in/vtop/initialProcess">For V-Top Click Here and Enjoy the VIT BHOPAL Services... <br></li>
                 <li> <a href="https://fontawesome.com">To Get Awesome font for Your Website Click Here !!<br></li>
                  <li><a href="https://docs.google.com/document/u/0/?tgif=d">To Open Google Docs Click Here<br></li>
                    
                    '''
    return HttpResponse(navbar)
