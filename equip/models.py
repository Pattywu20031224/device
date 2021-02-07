from django.db.models import *


class Equip(Model):
    SerialNumber = CharField('設備編號', max_length=255)
    pattern = CharField('型號', max_length=255)
    PropertyNumber = CharField('財產編號', max_length=255)
    comment = CharField('備註',max_length=255)

    def __str__(self):
        return "{}: {}".format(self.pattern, self.SerialNumber)




#設備編號，例：NB109001
#型號，例：Dell Latitude 3400，連結至「設備型號」
#財產編號，例：314010103-0002018
#備註，例：Wifi 無法連線