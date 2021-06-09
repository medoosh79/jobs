from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


JOB_TYBE=(
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Remote', 'Remote'),    
    ('Freelance', 'Freelance'),
)
EDU=(
    ('Student','Student'),
    ('Medium_Level','Medium_Level'),
    ('Bachelor','Bachelor'),
    ('Master','Master'),
    ('Doctorate','Doctorate'),
)

GEN=(
    ('Male','Male'),
    ('Female','Female'),
    ('NO Preference','NO Preference'),
)


class Person(models.Model):
    user=models.OneToOneField(User, verbose_name=_("User Name"), on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    degree= models.CharField(_("Degree"), max_length=15, choices=EDU,null=True,blank=True)
    certification= models.CharField(_("Certification "), max_length=50 ,null=True,blank=True)
    graduation_year= models.DateField(_("Graduation Year "), null=True,blank=True)
    job_type = models.CharField(_("Job Type"), max_length=15, choices=JOB_TYBE)
    gender = models.CharField(_("Gender"), max_length=15, choices=GEN )
    career = models.CharField(_("Career"), max_length=70,null=True,blank=True)   
    bio= models.TextField(_("Describe yourself"), max_length=1000,null=True, blank=True)
    biopro= models.TextField(_("Your Vision"), max_length=1000,null=True,blank=True)
    aboutskills= models.TextField(_("About Skills"), max_length=500,null=True,blank=True)
    nameskill1=models.CharField(_("First Skill"), max_length=50, null=True,blank=True)
    valueskill1= models.IntegerField(_("Value Skill1"),null=True,blank=True)

    fb = models.URLField(_("Face Book"), null=True,blank=True)
    tw = models.URLField(_("Twitter "),null=True,blank=True)
    instagram = models.URLField(_("Instagram "),null=True,blank=True)
    linkedin = models.URLField(_("Linkedin "),null=True,blank=True)
    address = models.CharField(_('Address'), max_length= 100,null=True,blank=True)    
    state = models.CharField(_('State'), max_length= 25,null=True,blank=True)
    zip = models.CharField(_('ZIP'), max_length= 25,null=True,blank=True)
    mobile= models.IntegerField(_('Mobile'), null=True,blank=True)
    birthday= models.DateField(_("Birthday"), auto_now=False, auto_now_add=False, blank=True , null=True)
    profile_pic = models.ImageField(upload_to='user/', default="defualt.jpg")
    bg_pic = models.ImageField(upload_to='background/', default="defualt.jpg")
    date_created = models.DateTimeField(  auto_now_add=True, null=True)
    date_update = models.DateTimeField(  auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username