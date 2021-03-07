from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, ListView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.

class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']

    
class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack-create.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'
    model = Snack
    fields = ['title', 'purchaser', 'description']
    
class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')





    


