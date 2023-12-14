import email
from .models import Marksheet
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.db.models import Q
import re
from django.contrib import messages

def marksheet(request):
    mydata = Marksheet.objects.all().values()
    return render(request, 'stud_data.html', {'mydata': mydata})

#views ....
def myfirst(request):
    # You can add any logic here if needed
    return render(request, 'myfirst.html')

def stud_data(request):

    mydata = Marksheet.objects.all().values()
    return render(request, 'stud_data.html',{'mydata': mydata})
    
def insert_data(request):
    if request.method == 'POST':
        # Get data from the form
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email=request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']

        first_name=firstname.capitalize()
        last_name=lastname.capitalize()

        phone_pattern='^\d{10}$'
        valid_phone=re.match(phone_pattern,phone)
        
        email_pattern='^[a-zA-Z0-9_.+-]+@+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        valid_email=re.match(email_pattern,email)

        if not valid_phone:
            error_msg ="Invalid phone number. Please enter a 10-digit number."
            return render(request, 'insert_data.html', {'error_message': error_msg})
        elif not valid_email:
            error_msg ="Invalid Email Address."
            return render(request, 'insert_data.html', {'error_message': error_msg})

        # Marksheet.objects.create(
        #    firstname=firstname,
        #    lastname=lastname,
        #    phone=phone,
        #    dob=dob
        # )

        new_marksheet = Marksheet(
            firstname=first_name,
            lastname=last_name,
            email=email,
            phone=phone,
            dob=dob
        )

        # Save the instance to the database
        new_marksheet.save()
        messages.success(request, 'Data Inserted successfully!')

        # Redirect
        return redirect('stud_data')

    return render(request, 'insert_data.html')


def update_data(request,item_id):
    record_to_update = Marksheet.objects.get(pk=item_id)  # request.data.get()

    if request.method == 'POST':

        #id_to_update = request.POST['id_']
       
        # Get data from the form
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']

        #VALIDATIONS: 
        phone_pattern='^\d{10}$'
        valid_phone=re.match(phone_pattern,phone)
        
        email_pattern='^[a-zA-Z0-9_.+-]+@+[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        valid_email=re.match(email_pattern,email)

        if not valid_phone:
            error_msg ="Invalid phone number. Please enter a 10-digit number."
            return render(request, 'insert_data.html', {'error_message': error_msg})
        elif not valid_email:
            error_msg ="Invalid Email Address."
            return render(request, 'insert_data.html', {'error_message': error_msg})

        #UPDATE
        
        record_to_update.firstname = firstname
        record_to_update.lastname = lastname
        record_to_update.email=email
        record_to_update.phone = phone
        record_to_update.dob = dob

        # Save the instance to the database
        record_to_update.save()

        return redirect('stud_data')

    return render(request, 'update_data.html',{'record_to_update': record_to_update})


def delete_data(request,item_id2):
        record_to_delete = Marksheet.objects.get(pk=item_id2)
      
    #if request.method == 'POST':
       
      #  id_to_delete = Marksheet.objects.get('id_1')             
      #  i=request.POST['id_1']
      #  x = Marksheet.objects.all()[i]
      #  x.delete()
        record_to_delete.delete()
        return redirect('stud_data')

        #return render(request, 'stud_data.html',{'record_to_delete': record_to_delete})

def search_data(request):
    if request.method == 'POST':
        #id_to_search = request.POST['id_to_search']

        search_term=request.POST['search_name']

        # Search for the Marksheet instance with the provided ID
        searched_data = Marksheet.objects.filter(
            Q(id__icontains=search_term) |
            Q(firstname__icontains=search_term) |
            Q(lastname__icontains=search_term) |
            Q(email__icontains=search_term)
        )
      #  searched_data = Marksheet.objects.filter(firstname__icontains=search_name,lastname__icontains=search_name)
        print(searched_data)

        if not searched_data:
            return render(request, 'stud_data.html', {'mydata': "NO DATA EXISTS"})
        
        return render(request, 'stud_data.html', {'mydata': searched_data})

    return render(request, 'search_data.html')
