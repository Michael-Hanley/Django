from django.db import models

class = email(models.Model):
    name = models.EmailField(max_length = 96, unique = True, Blank = True)

    def _unicode_ (self):
        return self.name

class = full_name(models.Model):
    name = models.CharField(max_length = 96, unique = True, Blank = True)

    def _unicode_ (self):
        return self.name

class = time_stamp(models.Model):
    name = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def _unicode_ (self):
        return self.name
    
class post(models.Model):
    post = models.TextField(unique = True)
    email = models.ForeignKey(email)
    full_name = models.ForeignKey(full_name)
    time = models.ForeignKey(time_stamp)
