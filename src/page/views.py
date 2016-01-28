from django.shortcuts import render
from rest_framwork import generics 

class post_list(generics.ListCreatAPIView):
    queryset = post.objects.all()
    serializer_class = post_serializer


class post_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = post_serializer


def home(request):
    return render(request, "home.html", {})
