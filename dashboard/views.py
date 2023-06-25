from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpRequest,Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import ContactForm,HomePage,Office,AboutSection,TeamMemberKBG,TeamMemberKBGRA
# Create your views here.


def about_page(request):
    about_section = AboutSection.objects.first()
    return render(request, 'about.html', {'about_section': about_section})

def blog_page(request):
    return render(request,'blog.html')

def services_page(request):
    office = Office.objects.filter(active=True)
    context = {'offices': office}
    return render(request,'services.html',context)


def management_page(request):
    team = TeamMemberKBG.objects.all()
    teamofra = TeamMemberKBGRA.objects.all()
    context={'team':team,'teamofra':teamofra}
    return render(request,'management.html',context)


def contact_page(request):
    return render(request,'contact.html')


def home_page(request):
    homepage = HomePage.objects.latest('id')
    office = Office.objects.filter(active=True)
    context = {'homepage': homepage, 'offices': office}
    return render(request, 'index.html', context)





# Contact Form
@csrf_exempt
def contactform(request):
    if request.method == 'POST':
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        contact_form = ContactForm(name=name, email=email, subject=subject, message=message)
        
        contact_form.save()
        

        return render(request, 'index.html', {'message': 'Your form has been submitted successfully! We will contact with you soon.'}) 
    else:
        return render(request, 'contact.html',{'message': 'There is a problem'})


