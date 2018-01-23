from django.shortcuts import render, HttpResponse, redirect
def index( request ):
    
    return render( request, "Survey_Form/index.html" )