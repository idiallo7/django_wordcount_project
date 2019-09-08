from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context={'res':'res'}
    return render(request, 'wordcountapp/home.html', context)


def countForm(request):
    if request.method == 'POST':
        cmt = request.POST.get('comment')
        nbr =cmt.split()
        freq={}
        for i in nbr:
            if i in freq:
                freq[i.lower()]+=1
            else:
                freq[i.lower()]=1

        context={'formWelcome':'WordCount Form','cmt':cmt, 'nbr':len(nbr), 'freq':freq}
    else:

        context={'formWelcome':'WordCount Form'}

    return render(request, 'wordcountapp/countForm.html',context)

def about(request):
    context={}
    return render(request, 'wordcountapp/about.html', context)
