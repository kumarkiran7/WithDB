from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def employee_details(request):
    try:
        if request.method == 'POST':
            
            a = request.body
            b=json.loads(a)
            b=b['id']
            Emp_Det = Employee_Details.objects.get(pk=b)
            
            emp_Id            = (Emp_Det.Emp_Id)
            name              = (Emp_Det.Name)
            email             = (Emp_Det.Email)
            first_Name        = (Emp_Det.First_Name)
            last_Name         = (Emp_Det.Last_Name)
            father_Name       = (Emp_Det.Father_Name)
            mother_Name       = (Emp_Det.Mother_Name)
            dob               = (Emp_Det.Dob)
            blood_Group       = (Emp_Det.Blood_Group)
            contact_Number    = (Emp_Det.Contact_Number)
            emergency_Number  = (Emp_Det.Emergency_Number)
            present_Address   = (Emp_Det.Present_Address)
            permanent_Address = (Emp_Det.Permanent_Address)
            qualification     = (Emp_Det.Qualification)
            
            Emp_Det.Emp_Id            = emp_Id
            Emp_Det.Name              = name
            Emp_Det.Email             = email
            Emp_Det.First_Name        = first_Name
            Emp_Det.Last_Name         = last_Name
            Emp_Det.Father_Name       = father_Name
            Emp_Det.Mother_Name       = mother_Name
            Emp_Det.Dob               = dob
            Emp_Det.Blood_Group       = blood_Group
            Emp_Det.Contact_Number    = contact_Number
            Emp_Det.Emergency_Number  = emergency_Number
            Emp_Det.Present_Address   = present_Address
            Emp_Det.Permanent_Address = permanent_Address
            Emp_Det.Qualification     = qualification
            
            name = Emp_Det.add_name()
            
            Emp_Det.save()
            
            response = {
                    'Emp_Id'            : emp_Id,
                    'Name'              : name,
                    'Email'             : email,
                    'First_Name'        : first_Name,
                    'Last_Name'         : last_Name,
                    'Father_Name'       : father_Name,
                    'Mother_Name'       : mother_Name,
                    'Dob'               : dob,
                    'Blood_Group'       : blood_Group,
                    'Contact_Number'    : contact_Number,
                    'Emergency_Number'  : emergency_Number,
                    'Present_Address'   : present_Address,
                    'Permanent_Address' : permanent_Address,
                    'Qualification'     : qualification,
                    }

            return JsonResponse(response)
            
            
        
    except Exception as ex:
        return(ex)
    
    

@csrf_exempt

def employee_hist(request):
    try:
        if request.method == 'POST':
            
            a = request.body
            b=json.loads(a)
            b=b['id']
            Emp_Hist = Employment_History.objects.get(pk=b)
            
            emp_Id               = (Emp_Hist.Emp_Id)
            previous_CompanyName = (Emp_Hist.Previous_CompanyName)
            designation          = (Emp_Hist.Designation)
            location             = (Emp_Hist.Location)
            date_of_Employment   = (Emp_Hist.Date_of_Employment)
            experience           = (Emp_Hist.Experience)
            achievements         = (Emp_Hist.Achievements)
            qualification        = (Emp_Hist.Qualification)
            
            Emp_Hist.Emp_Id               = emp_Id
            Emp_Hist.Previous_CompanyName = previous_CompanyName
            Emp_Hist.Designation          = designation
            Emp_Hist.Location             = location
            Emp_Hist.Date_of_Employment   = date_of_Employment
            Emp_Hist.Experience           = experience
            Emp_Hist.Achievements         = achievements
            Emp_Hist.Qualification        = qualification
            
            Emp_Hist.save()
            
            response = {
                    'Emp_Id'               : emp_Id,
                    'Previous_CompanyName' : previous_CompanyName,
                    'Designation'          : designation,
                    'Location'             : location,
                    'Date_of_Employment'   : date_of_Employment,
                    'Experience'           : experience,
                    'Achievements'         : achievements,
                    'Qualification'        : qualification,
                       }
            
            return JsonResponse(response)

    except Exception as ex:
        return(ex)

def salary_managemet(request):
    pass