from django.contrib.auth.models import AbstractUser
from django.db import models
# from actstream import registry


class User(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")
    about = models.TextField(null=True)
    image = models.ImageField(upload_to='profile_images', default="http://www.mygolfkaki.com/DesktopModules/Custom%20Module/Member%20Management/Image/default.gif",
                              blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u"{}".format(self.name)


class Company(models.Model):
    name = models.CharField(max_length=120)
    founded = models.DateField(null=True)
    address1 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    funding = models.IntegerField(null=True)
    url = models.CharField(max_length=150, null=True)
    followers = models.ManyToManyField(User, blank=True, null=True, related_name='company')
    category = models.ManyToManyField(Category, related_name='company', null=True, blank=True)
    image = models.ImageField(upload_to='company_images',
                               blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class Comment(models.Model):
    subject = models.CharField(max_length=120, null=True)
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments')
    post = models.ForeignKey(Company, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.comment)


class FundingRound(models.Model):
    ROUND = (
        ("Seed", "Seed"),
        ("SeriesA", "Series A"),
        ("SeriesB", "Series B"),
        ("SeriesC", "Series C"),
        ("SeriesD", "Series D"),
    )
    series = models.CharField(max_length=20, choices = ROUND)
    raised = models.IntegerField()
    date = models.DateField()
    company = models.ForeignKey(Company, related_name='funding_round')
