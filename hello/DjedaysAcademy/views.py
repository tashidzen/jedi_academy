from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, DjedayForm, CandidateForm
from .q_forms import Q_UserForm
from .models import Candidate, Jedi, Question, Djeday, Planet

def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>Для Джедаев</h2>")


def contact(request):
     #userform = UserForm()
     if request.method == "POST":
         userform = UserForm(request.POST)
         nameForm = request.POST.get("name")  # получаем данные
         planetForm = request.POST.get("planet")
         ageForm = request.POST.get("age")
         emailForm = request.POST.get("email")
         a = Djeday(name="Нет Джедая")
         b = Planet(name="нет планеты")
         a.save()
         b.save()
         jediForm = Jedi(name=a, planet=b)
         questionForm = Question(qu="?", ans="True")
         candidate = Candidate(name=nameForm, planet=planetForm, age=ageForm, email=emailForm, jedi=jediForm, question=questionForm)
         jediForm.save()
         questionForm.save()
         candidate.save()  # сохраняем форму
         return render(request, "cand.html", {"form": userform})
     else:
         userform = UserForm()
         return render(request, "cand.html", {"form": userform})


def question(request):
    # if request.method == "POST":
    #     q_userform = Q_UserForm(request.POST)
    #     question = request.POST.all() # получаем данные
    #     answer = request.POST.all()
    #     Que = Question(qu=question, ans=answer)
    #     Que.save()  # сохраняем форму
    #     return render(request, "question.html", {"form": q_userform})
    # else:
    q_userform = Q_UserForm()
    return render(request, "question.html", {"form": q_userform})


def JediListView(request):
    form1 = DjedayForm(request.POST)
    form2 = CandidateForm()
    queryset = Jedi.with_padawans.all()
    if request.POST.get("planet") == Candidate.planet:
        list_cand = Candidate.objects.filter(planet=Jedi.planet)
        return render(list_cand, 'djeday.html', {"form2": form2})
    return render(request, 'djeday.html', {"form1": form1})



