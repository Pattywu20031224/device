from django.urls import reverse, reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from log.models import Log


# Create your views here.
class EquipList(LoginRequiredMixin, ListView):   
    model = Equip    
    paginate_by = 10

class EquipView(LoginRequiredMixin, DetailView):
    model = Equip
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['log_list'] = Log.objects.filter(
            equip=self.object, 
        ).order_by('-id').select_related('borrower')
        return ctx
class EquipAdd(LoginRequiredMixin, CreateView):  
    model = Equip
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('equip_list')

class EquipEdit(LoginRequiredMixin, UpdateView): 
    model = Equip
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('equip_list')

class EquipDelete(LoginRequiredMixin, DeleteView):   
    model = Equip
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('equip_list')