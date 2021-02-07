from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from log.models import Log

# Create your views here.
class BorrowerList(LoginRequiredMixin, ListView):     
    model = Borrower
    ordering = ['realname']     # 依姓名排序
    paginate_by = 20

class BorrowerView(LoginRequiredMixin, DetailView):   
    model = Borrower

class BorrowerView(LoginRequiredMixin, DetailView):   # 檢視讀者
    model = Borrower

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['log_list'] = Log.objects.filter(
            borrower=self.object
        ).order_by('-id').select_related('book')
        return ctx
class BorrowerAdd(LoginRequiredMixin, CreateView):   
    model = Borrower
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerEdit(LoginRequiredMixin, UpdateView):   
    model = Borrower
    fields = '__all__'
    template_name = 'form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerDelete(LoginRequiredMixin, DeleteView): 
    model = Borrower
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('borrower_list')