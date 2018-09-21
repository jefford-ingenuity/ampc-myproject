from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import Group

from django.views.generic import TemplateView

import datetime



def hello(request):
    print(request.user.groups.all())
    if request.user.is_authenticated:
        return HttpResponse("There is a logged user")
    else:
        return HttpResponse("No logged-in user")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(
        request,
        "hours_ahead.html",
        {"hour_offset": offset, "next_time": dt}
    )


class CurrentDateTimeView(TemplateView):
    template_name = "current_datetime.html"
