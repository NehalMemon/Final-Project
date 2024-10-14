from django.shortcuts import render , redirect ,  get_object_or_404
from poll.models import poll
from poll.models import Formdata
from django.views.decorators.csrf import csrf_exempt


def home(request):
    poll_data=poll.objects.all()
    data={
        'data':poll_data
    }
    return render(request, "home.html",data) 


def details(request,slug):
    details=poll.objects.get(slugs=slug)
    data={
        'data':details
    }
    return render(request, "details.html",data)


@csrf_exempt
def vote(request):
    poll_data = poll.objects.all()  
    data = {
        'data': poll_data
    }
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            ID = request.POST.get('id')
            
            # Check if the email already exists
            if Formdata.objects.filter(email=email).exists():
                data['error'] = "This email has already been used to vote."
                return render(request, "vote.html", data)
            
            # Save the form data if the email is unique
            form_data = Formdata(name=name, email=email, selected_id=ID)
            form_data.save()
            
            if ID:
                polls = get_object_or_404(poll, id=ID)
                polls.count += 1
                polls.save()
                return redirect('result')
            else:
                return render(request, "vote.html", data)
    except Exception as e:
        print(f"Error: {e}")
    return render(request, "vote.html", data)


@csrf_exempt
def result(request):
    polls = poll.objects.all() 
    data = {
        'polls': polls
        }
    return render(request, 'result.html', data)

