from django.shortcuts import render, get_object_or_404, redirect

from meetapp.forms import ParticipantForm
from meetapp.models import Meet


# Create your views here.


from django.shortcuts import render
from .models import Meet

def home(request):
    query = request.GET.get('q')
    status = request.GET.get('status')
    sort_by = request.GET.get('sort_by', 'start_datetime')

    meets = Meet.objects.all()

    if query:
        meets = meets.filter(name__icontains=query)

    if status:
        meets = meets.filter(status=status)

    meets = meets.order_by(sort_by)

    latest_meet = meets.last()

    context = {
        'meets': meets,
        'latest_meet': latest_meet,
        'query': query,
        'status': status,
        'sort_by': sort_by,
    }

    return render(request, 'home.html', context)



def meet_detail_view(request, pk):
    meet = get_object_or_404(Meet, pk=pk)
    context = {
        'meet': meet,
    }
    return render(request, 'meets/meetpage.html', context)





def add_participant_view(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParticipantForm()

    context = {
        'form': form,
    }

    return render(request, 'add_participant.html', context)



def all_meetings(request):
    query = request.GET.get('q')
    status = request.GET.get('status')
    sort_by = request.GET.get('sort_by', 'start_datetime')

    meets = Meet.objects.all()

    if query:
        meets = meets.filter(name__icontains=query)

    if status:
        meets = meets.filter(status=status)

    meets = meets.order_by(sort_by)

    context = {
        'meets': meets,
        'query': query,
        'status': status,
        'sort_by': sort_by,
    }

    return render(request, 'all_meetings.html', context)
