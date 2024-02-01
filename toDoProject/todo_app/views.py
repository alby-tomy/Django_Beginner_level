from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from todo_app.updateData import UpdateData
from . models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'taskData'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'taskUp'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('dddName',kwargs={'pk':self.object.id})
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'detail.html'
    success_url = reverse_lazy('cbvhomeName')
    


# Create your views here.
def addView(request):
    taskData = Task.objects.all()

    if request.method == 'POST':
        add_name = request.POST.get('task')
        add_priority = request.POST.get('priority')
        add_date = request.POST.get('date')
        model = Task(name=add_name, priority=add_priority, date=add_date)
        model.save()
    return render(request,'home.html',{'taskData':taskData})


def deleteView(request, itemId):
    item_id = Task.objects.get(id=itemId)

    if request.method == 'POST':
        item_id.delete() 
        return redirect('/')  
    return render(request,'delete.html')

def updateView(request, itemId):
    itemId = Task.objects.get(id=itemId)
    updateData = UpdateData(request.POST or None, instance=itemId)
    if updateData.is_valid():
        updateData.save()
        return redirect('/')
    return render(request, 'edit.html',{'updateD':updateData, 'item-id':itemId})