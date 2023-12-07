from django.shortcuts import render

html_base = """
    <h1> Mi Web Personal </h1>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about-me">Acerca De</a></li>
            <li><a href="/portfolio">Portfolio</a></li>
            <li><a href="/contact">Contact</a></li>
    
        </ul>

"""

# Create your views here.

def home(request):
    return render(request, "core/home.html" )
def about(request):
    return render(request, "core/about.html" )
def contact(request):
    return render(request, "core/contact.html" )
