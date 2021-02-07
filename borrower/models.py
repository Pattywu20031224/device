from django.db.models import *


#借用人資料
class Borrower(Model):
    realname = CharField('姓名', max_length=32)
    identify = CharField('身分', max_length=255)
    email = EmailField('電子信箱')
    work = CharField('職稱', max_length=255)
    subject = CharField('任教科目', max_length=255)
    tel=CharField('連絡電話',max_length=10)
    state= CharField('狀態', max_length=3)
    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.email, 
            self.tel
        )

# 借用人
#姓名
#身分
#職稱/任教科目 
#聯絡電話，例：0912-345-678 
#電子郵件信箱，例：test@dcsh.tp.edu.tw
#狀態