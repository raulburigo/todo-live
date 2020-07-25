from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import TaskSerializer
import datetime
from .models import Task
from django.utils import timezone

# Create your views here.

@login_required
def tasklist(request):

    # dados para o gráfico "Status das tarefas"
    labels = ["Concluídas", "Por fazer"]
    data = [Task.objects.filter(user=request.user, done=2).count(), Task.objects.filter(user=request.user, done=1).count()]

    #dados para gráfico "Últimas 24 horas" - que aparentemente era last week no início...
    donelastweek = Task.objects.filter(user=request.user, done=2, updated_at__gt=datetime.datetime.now()-datetime.timedelta(hours=24)).count()
    createdlastweek = Task.objects.filter(user=request.user, created_at__gt=datetime.datetime.now()-datetime.timedelta(hours=24)).count()

    lwlabels = ["Criadas", "Concluídas"]
    lwdata = [createdlastweek, donelastweek]

    # dados para gráfico "Última semana"
    week = {6: "Dom", 0: "Seg", 1: "Ter", 2: "Qua", 3: "Qui", 4: "Sex", 5: "Sáb"}

    tasks_per_day = []
    created_per_day = []
    days_of_week = []

    n = 0
    for n in reversed(range(7)):
        tasks_per_day.append(Task.objects.filter(user=request.user, done=2, updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=n+1), updated_at__lt=datetime.datetime.now()-datetime.timedelta(days=n)).count())
        created_per_day.append(Task.objects.filter(user=request.user, created_at__gt=datetime.datetime.now()-datetime.timedelta(days=n+1), created_at__lt=datetime.datetime.now()-datetime.timedelta(days=n)).count())
    for n in range(7):
        days_of_week.append(week[(datetime.datetime.now() - datetime.timedelta(days=6 - n)).weekday()])

    #segue geral -> busca e paginação
    if request.GET.get('search'):
        search = request.GET.get('search')
        tasks = Task.objects.filter(title__icontains=search, user=request.user).order_by('-created_at').order_by('done')

    else:
        tasks_list = Task.objects.filter(user=request.user).order_by('-created_at').order_by('done')  # já tava
        paginator = Paginator(tasks_list, 5)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {
        'tasks': tasks,
        'labels': labels,
        'data': data,
        'lwlabels': lwlabels,
        'lwdata': lwdata,
        'tasks_per_day': tasks_per_day,
        'days_of_week': days_of_week,
        'created_per_day': created_per_day,
    })

@login_required
def taskdetail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/detail.html', {'task': task})

@login_required
def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 1
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def taskedit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def taskdone(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if task.done == 1:
        task.done = 2
        messages.info(request, f"{task.title} atualizada!", )

    elif task.done == 2:
        task.done = 1
        messages.info(request, f"{task.title} atualizada!", )

    task.save()
    return redirect('/')

@login_required
def taskdelete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    messages.info(request, f"{task.title} deletada!", )

    task.delete()
    return redirect('/')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def bootsview(request):
    return render(request, 'tasks/boots.html')
