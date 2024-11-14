from django.shortcuts import render, redirect

from app1.models import Movie

from app1.forms import MovieForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})

class Home(ListView):
    model=Movie
    template_name = "home.html"
    context_object_name = "movie"

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     # query=qs.filter(year="2023")
    #     # query = qs.filter(title__icontains="m")
    #     # query = qs.filter(year__gt=2023)
    #     query = qs.filter(title__startswith="k")
    #     return query

    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context["name"]="adhi"
    #     context["age"]=21
    #     return context


    extra_context ={'name':'adhi','age':21}



# def addmovies1(request):
#     if(request.method=="POST"):
#         form=MovieForm(request.POST,request.FILES) #create a form object using values that are passed through request
#         if form.is_valid():  # is valid() bult in fuction to chechk the values of forms fileds
#             form.save()    # saVE THE Form objects in table
#             return redirect("/")
#
#     form=MovieForm()  #empty form objects is created
#     context={'form':form}
#     return render(request,'add1.html',context)
class Addmovie(CreateView):
    model=Movie
    fields = ['title','description','year','image']
    template_name = 'add1.html'
    success_url = reverse_lazy('app1:home')

# def addmovie(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         l=request.POST['l']
#         i=request.FILES['i']
#
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')

# def detail(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request,'detail.html',{'movie':k})
class Detail(DetailView):
    model = Movie
    template_name = "detail.html"
    context_object_name = "movie"

# def edit(request,p):
#     k=Movie.objects.get(id=p)
#     if(request.method=='POST'):
#         k.title=request.POST['t']
#         k.description = request.POST['d']
#         k.year= request.POST['y']
#         k.language= request.POST['l']
#
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#         k.save()
#         return Home(request)
#
#
#     return render(request,'edit.html',{'movie':k})
class Edit(UpdateView):
    model=Movie
    fields = ['title','description','year','image']
    template_name = 'edit.html'
    success_url = reverse_lazy('app1:home')




# def delete(request,i):
#     k = Movie.objects.get(id=i)
#     k.delete()
#     return Home(request)

class Delete(DeleteView):
    template_name ="delete.html"
    model = Movie
    success_url = reverse_lazy('app1:home')

