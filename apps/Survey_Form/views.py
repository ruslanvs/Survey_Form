from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index( request ):
    # messages.add_message( request, messages.INFO, 'FLASH long' )
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    messages.success( request, 'Thanks for submitting this form! You have submitted this form ' + str( request.session['counter'] ) + ' times now' )
    return render( request, "Survey_Form/index.html" )

def form_process( request ):
    print "SUBMIT"
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    print request.POST
    return redirect( '/survey_form/result' )

def result( request ):
    print "result route"
    return render( request, "Survey_Form/result.html" )
