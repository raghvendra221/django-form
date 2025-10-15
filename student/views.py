from django.shortcuts import render,redirect
from student.forms import profileform
from student.models import Profile

def home(req):
    candidates = Profile.objects.all()
    if req.method=='POST':
        form =profileform(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = profileform()
    return render(req,'student/homes.html',{'form':form,'candidates':candidates})

def candidates_details(req,pk):
    candidate= Profile.objects.get(pk=pk)
    return render(req,'student/candidate.html',{'candidate':candidate})
