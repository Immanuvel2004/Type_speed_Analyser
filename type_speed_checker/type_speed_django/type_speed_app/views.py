from django.shortcuts import render
from .utils import fetch_text, calculate_wpm, calculate_accuracy

def home(request):
    return render(request, 'home.html', {'text': None})

def test_page(request):
    text = fetch_text()
    request.session['text'] = text
    return render(request, 'home.html', {'text': text})

def result(request):
    if request.method == "POST":
        original = request.session.get('text')
        typed = request.POST.get('typed_text')
        time_taken = float(request.POST.get('time_taken'))

        wpm = calculate_wpm(original, time_taken)
        accuracy = calculate_accuracy(original, typed)

        return render(request, 'result.html', {
            'wpm': wpm,
            'accuracy': accuracy
        })
