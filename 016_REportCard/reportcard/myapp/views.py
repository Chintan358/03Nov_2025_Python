from django.shortcuts import render
from myapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum
# Create your views here.
def index(request):
    students = Student.objects.all()
    paginator = Paginator(students, 7)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request,"index.html",{"students":page_obj})

def reportcard(request):
    stid = request.GET['stid']
    marks = Marks.objects.filter(student_id = stid)

    total = 0
    for m in marks:
        total+=m.marks
    per = round((total*100)/300,2)


    students = Student.objects.annotate(
    total_marks = Sum('marks__marks')
    ).order_by('-total_marks')

    rank = 0
    for st in students:
        rank+=1
        
        if int(st.id)==int(stid):
            break


    return render(request,"reportcard.html",{"marks":marks,"total":total,"per":per,"rank":rank})