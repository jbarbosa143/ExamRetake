from django.db import models
import re

class UserManager(models.Manager):
    def registerValidator(self,postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # first name required
        Emaildata =  User.objects.filter(email_address = postData['email'])
        # email required
        if len(postData['email']) == 0:
            errors['email'] = 'A Email is Required!'
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(Emaildata) > 0:
            errors['duplicatedemail'] = "Email already in use!"
        # password required
        if len(postData['pw']) < 8:
            errors['pw'] = 'Password Requires a Min of 9 Characters!'
        # passwords must match
        if postData['pw'] != postData['cpw']:
            errors['cpw'] ='Passwords Must MATCH!!!!'
        return errors

    def loginValidator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        Emaildata =  User.objects.filter(email_address = postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = 'A Email is Required!'
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!,Please use a Valid Email!"
        elif len(Emaildata) == 0:
            errors['emaildoesntmatch'] = 'This email doesnt match, or isnt Registed.'
        else:
            print(Emaildata[0].password)
            if Emaildata[0].password != postData['pw']:
                errors['matchpw'] = "Invaild Password!!! Try Agin." 
        return errors
class QuoteManager(models.Manager):
    def quoteValidator(self,postData):
        errors={}
        print(postData)
        if len(postData['quotedby']) == 0:
            errors['quotedby'] = 'Quoted By is Required!'
        elif len(postData['quotedby'])<=2:
            errors['quoteleng'] = 'Quoted By must be atleast 2 characters!'
        if len(['message']) == 0:
            errors['message'] = 'Message is required!'
        elif len(postData['message']) <=10:
            errors['message'] = 'Message MUST BE ATLEAST 10 Charaters long!!'
        return errors

class User(models.Model):
    email_address = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    quote = models.TextField()
    quoter = models.CharField(max_length=55,default="name")
    added_by = models.ForeignKey(User, related_name="quoteuploaded", on_delete = models.CASCADE)
    favoredquote = models.ManyToManyField(User, related_name = "favoredaquote")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()