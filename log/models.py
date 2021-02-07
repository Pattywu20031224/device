from django.db.models import *
from equip.models import *
from borrower.models import *

# Create your models here.
# 借閱紀錄
class Log(Model):
    borrower = ForeignKey(Borrower, CASCADE)
    equip = ForeignKey(Equip, CASCADE)
    checkout = DateTimeField('借用時間', auto_now_add=True)
    returned = DateTimeField('歸還時間', null=True)    # 以 null 代表尚未歸還

    def __str__(self):
        return "{} | {} | {}".format(
            self.checkout, 
            self.borrower.realname, 
            self.equip.SerialNumber
        )
