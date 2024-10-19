from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def Home(request):
    if request.method == 'POST':
        obj = Todo()
        obj.task = request.POST.get('task')
        if obj.task is "":
            return redirect('/')
        else:
            obj.save()
        return redirect('/')
    data = Todo.objects.all()
    return render(request,'home.html',{'data':data})



def Delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    return redirect('/')