from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Proyect, Tasks
from .forms import create_new_task, create_project

# Create your views here.
def index(request):
    return render(request, "index.html")

def Projects(request):
    proyects = Proyect.objects.all()
    return render(request, "projects/projects.html", {"proyects" : proyects})
#{"proyects" : proyects} esta es al forma de crear una variable para usarse en el frontend para llamar a objetos del backend, en este caso, estamos asignandole un valor proyects, que se va a ser una lista de objetos de una tabla sql, proyects se usa directyamente en el frontend, pero recibe su valor de elementos del backend
def about(request):
    tasks = Tasks.objects.all()
    return render(request, "tasks/about.html", {
            "tasks" : tasks,
            })
        

def Forms(request):
    if request.method == 'GET':
        return render(request, "tasks/create-forms.html", {
            "form": create_new_task()
        })
    else:
        id_project = request.POST.get('id_Proyect')
        # Obtener el objeto Proyect usando su ID
        project = get_object_or_404(Proyect, pk=id_project)
        Tasks.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project=project # Usar el objeto `project`
        )
        return redirect('create_task')

def projects_form(request):
    if request.method == 'GET':
        return render(request, "projects/create-projects.html", {
            "form": create_project()
        })
    else:
        Proyect.objects.create(
            name=request.POST['name'],
        )
        return redirect('create_project')
    
def delete_task(request, id_task):
    task = get_object_or_404(Tasks, id=id_task)
    task.delete()
    return redirect('show_tasks')

def delete_projects(request, id_project):
    project = get_object_or_404(Proyect, id=id_project)
    project.delete()
    return redirect('projects')

def done_tasks(request, id_task):
    task = get_object_or_404(Tasks, id=id_task)
    task.done = True
    task.save()
    return redirect('show_tasks')

def done_projects(request, id_projects):
    project = get_object_or_404(Proyect, id=id_projects)
    project.done = True
    project.save()
    return redirect('projects')