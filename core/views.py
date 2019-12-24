from django.shortcuts import render
from django.views import View
import requests

class HomeView(View):

    def get(self, request):

        name = "Home"
        requests.post("https://bennie.netlify.com/#/", data={"message":"Hello"}, json={"message":"Hello"})
        return render(request, "home.html", {"name":name})

