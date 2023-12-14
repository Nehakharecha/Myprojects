from django.db import models

class Marksheet(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    email=models.EmailField(max_length=255,null=True,default="demo@gmail.com")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

'''
add student             //
search txtbox -> btn    //
action -> upd, del      
validation  phone       //
dob yyyy/mm/dd          //
name string format      //neha kharecha -> Neha Kharecha
Stud. ID , Mob.         //
email id                //
msg-> add, del 
search on name , email  //

'''