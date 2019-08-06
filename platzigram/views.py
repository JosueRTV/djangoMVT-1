from django.http import HttpResponse, JsonResponse
# Utilities
from datetime import datetime
import json

def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is: {now}'.format(
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):

    # print(request.content_params)
    numbers =[int(i) for i in request.GET['numbers'].split(",")]
    sorted_ints = sorted(numbers)
    # numbers2 = []
    # for i in numbers:
    #     numbers2.append(int(i))

    data = {
        "stattus": 'ok',
        'numbers': sorted_ints,
        'message': 'Integers are sorted succesfully'
    }

    # response = HttpResponse(json.dumps(data), content_type="aplication/json")
    response = JsonResponse(data, safe=True)
    # response = JsonResponse([1, 2, 3], safe=False)
    # import pdb; pdb.set_trace()
    return response
    # HttpResponse('Hi!{numbers}'.format(numbers=numbers))

def say_hi(request, name, age):
    if age < 18:
        message = "Sorry {} you're not allowed here".format(name)
    else:
        message = "Hello {}! Wellcome to Platzigram".format(name)
    return HttpResponse(message)