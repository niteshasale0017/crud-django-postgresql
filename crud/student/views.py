from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import StudentForm
from .models import Student


# Create your views here.
def add_show(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            
        form = StudentForm()                
    else:
        form = StudentForm()
    stu = Student.objects.all()
    paginator = Paginator(stu,4)
    page=request.GET.get('page')
    page_no = Paginator.get_page(paginator,page)
    

    return render(request,'student/add_show.html',{'key':form,'stu':stu,'page_no':page_no})

def delete(request,id):
    data = Student.objects.get(pk=id)
    data.delete()
    return redirect('/')

def update(request,id):
    if request.method=='POST':
        pi = Student.objects.get(pk=id)
        form = StudentForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
        return redirect('/')        
    else:
        pi = Student.objects.get(pk=id)
        form = StudentForm(instance=pi)
    return render(request,'student/update.html',{'key':form})            
    
    





    
