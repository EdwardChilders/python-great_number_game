from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
  if request.session['correct'] == False:
    request.session['correct'] = False
  if 'num' not in request.session:
    request.session['num'] = random.randint(1, 100) 
  print(request.session['num'])

  return render(request, 'index.html')

def guess(request):
  print(request.POST['theGuess'])
  if int(request.POST['theGuess']) < request.session['num']:
    request.session['str'] = "Too Low!"
    request.session['correct'] = False
  if int(request.POST['theGuess']) > request.session['num']:
    request.session['str'] = "Too High!"
    request.session['correct'] = False
  if int(request.POST['theGuess']) == request.session['num']:
    request.session['str'] = f"The number was {request.session['num']}!"
    request.session['correct'] = True
  return redirect('/')

def again(request):
  request.session['num'] = random.randint(1, 100)
  request.session['str'] = ""
  request.session['correct'] = False
  return redirect('/')