from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    address = models.TextField()
    status = models.CharField(max_length=20,choices=(("single","single"),("married","married"),("engaged","engaged")),default= "single" )
    gender = models.CharField(max_length=20,choices=(("male","male"),("female","female"),("other","other")),default= "male")
    phone_no = models.CharField(max_length=15,validators=[RegexValidator("^0?[5-9]{1}\d{9}$")])
    description = models.TextField()
    pic = models.ImageField(upload_to="images\\",null=True)
    
    def __str__(self):
        return "%s" %self.user
    
    
class MyPost(models.Model):
    pic = models.ImageField(upload_to="images\\",null=True)
    subject = models.CharField(max_length=200)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    
    def __str__(self):
        return "%s" %self.subject
    
    
class PostComment(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=20,null=True, blank=True, choices=(("helpful" ,"helpful"),("not-constructive","off-topic"),("abusive","abusive")))
    
    def __str__(self):
        return "%s" %self.msg
    
    
class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    liked_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return "%s" %self.liked_by    


class FollowUser(models.Model):
    prfle = models.ForeignKey(to=MyProfile, on_delete=CASCADE,related_name="proflie")
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE,related_name="followed_by")
             
    def __str__(self):
        return "%s" %self.followed_by



    



    
    
    
    