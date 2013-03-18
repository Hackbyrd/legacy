from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse

import _sqr
import add
import fib
import numpy as np

def home(request):
    return render_to_response('home.html', {});

def square(request, num):
    return HttpResponse(simplejson.dumps(_sqr.sqr(int(num))), mimetype="application/json")

def addNum(request, num, num2):
    return HttpResponse(simplejson.dumps(add.Add().add(int(num),int(num2))), mimetype="application/json")

def calcFib(request, num):
    c = int(num)
    j = '['


    if c == 0:
        j = "[]"
    
    elif c > 60:
        j = "The first " + c + " numbers are to large to fit on the screen."

    else:
        a = np.zeros(c) 
        fib.fib(a)
        s = []
        count = 0

        for t in a:
            s.append(t)

        for x in s:
            if count == c - 1:
                j = j + str(x).replace('.0', ']')

            else:
                j = j + str(x).replace('.0', ', ')
                    
            count = count +  1

    return HttpResponse(simplejson.dumps(j), mimetype="application/json")
