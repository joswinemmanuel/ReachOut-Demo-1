from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from.chatbot import get_chatbot_response
from django.views.decorators.csrf import csrf_protect


@login_required
def home(request):
  return render(request, 'home.html', {})


@csrf_protect
def ask_question(request):
    if request.method == 'POST':
        question = request.POST['question']
        response = get_chatbot_response(question)
        print(response)
        return JsonResponse({'response': response})
    else:
        return render(request, 'ask_question.html')


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})
    