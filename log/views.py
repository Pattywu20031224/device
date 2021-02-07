from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from borrower.models import Borrower
from equip.models import Equip
from .models import Log

# 借閱記錄列表
class LogList(LoginRequiredMixin, ListView):
    model = Log
    ordering = ['-checkout']
    paginate_by = 20


class CheckoutBorrower(LoginRequiredMixin, ListView):
    model = Borrower
    paginate_by = 20
    template_name = 'log/checkout_borrower_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            borrowers = Borrower.objects.filter(realname__icontains=query)
        else:
            borrowers = Borrower.objects
        return borrowers.order_by('realname')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx

class CheckoutEquip(LoginRequiredMixin, ListView):
    model = Equip
    paginate_by = 5
    template_name = 'log/checkout_equip_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            equips = Equip.objects.filter(title__icontains=query)
        else:
            equips = Equip.objects
        return equips.exclude(
            log__checkout__isnull=False, 
            log__returned__isnull=True
        ).order_by('SerialNumber')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        curr_borrower = Borrower.objects.get(id=self.kwargs['rid'])
        ctx['query'] = self.request.GET.get('query') or ""
        ctx['borrower'] = curr_borrower
        ctx['borrowing'] = curr_borrower.log_set.filter(
            returned__isnull=True
        ).select_related('equip')
        return ctx

class CheckoutLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        borrower = Borrower.objects.get(id=self.kwargs['rid'])
        equip = Equip.objects.get(id=self.kwargs['bid'])
        log = Log(borrower=borrower, equip=equip)
        log.save()
        return reverse('checkout_equip', kwargs={'rid': borrower.id})

class ReturnEquip(LoginRequiredMixin, ListView):
    model = Log
    paginate_by = 20
    template_name = 'log/return_equip_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            logs = Log.objects.filter(equip__SerialNumber=query)
        else:
            logs = Log.objects
        return logs.exclude(
            returned__isnull=False
        ).select_related('equip', 'borrower')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('query') or ""
        return ctx
class ReturnLog(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        log = Log.objects.get(id=self.kwargs['lid'])
        log.returned = datetime.now()
        log.save()
        return reverse('return_equip')