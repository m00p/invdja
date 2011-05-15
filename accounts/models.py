from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class UserSettings(models.Model):
    name            = models.CharField(max_length=80, verbose_name=_("Name"))
    surname         = models.CharField(max_length=50, blank=True,  verbose_name=_("Surname"))
    address         = models.CharField(max_length=80, verbose_name=_("Address"))
    zipcode         = models.CharField(max_length=10, verbose_name=_("Zip Code"))
    town            = models.CharField(max_length=50, verbose_name=_("Town"))
    province        = models.CharField(max_length=2, verbose_name=_("Province"))
    phone           = models.CharField(max_length=30, blank=True, verbose_name=_("Phone"))
    mobilephone     = models.CharField(max_length=30, blank=True, verbose_name=_("Mobile phone"))
    email           = models.CharField(max_length=30, blank=True, verbose_name=_("Email"))
    vatnumber       = models.CharField(max_length=11, blank=True, verbose_name=_("VAT number"))
    language        = models.CharField(max_length = 2)
    user            = models.ForeignKey(User,unique=True)
    
    
    def __unicode__(self):
        return u"%s" %(self.user)
