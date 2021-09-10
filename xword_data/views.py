from django.shortcuts import render
from .models import Clue
from django.http import Http404
from django.shortcuts import redirect
# Create your views here.


def drillView(request):
    if request.method == 'GET':
        clue = Clue.objects.order_by('?').first()
        results = ""
    else:
        clue = Clue.objects.get(id=request.POST['clue_id'])
        print(clue)
        if clue.entry.entry_text.lower() == request.POST['answer'].lower():
            return redirect('xword-answer', clue.id)
        else:
            results = 'not correct'
    # for requested count
    if request.session.get('requested_count'):
        requested_count = request.session.get('requested_count') + 1
    else:
        requested_count = 1

    return render(request, 'drill.html', {'clue': clue, 'requested_count': requested_count, 'result': results})
