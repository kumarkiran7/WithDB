from django.db import models

class Employee_Details(models.Model):
    
    Emp_Id            = models.CharField(max_length=10, unique=True)
    Name              = models.CharField(max_length=100, unique=True)
    Email             = models.EmailField(null=True, unique=True)
    First_Name        = models.CharField(max_length=100, null=True)
    Last_Name         = models.CharField(max_length=100, null=True)
    Father_Name       = models.CharField(max_length=100)
    Mother_Name       = models.CharField(max_length=100)
    Dob               = models.DateField(null=True)
    Blood_Group       = models.CharField(max_length=25, null=True)
    Contact_Number    = models.CharField(max_length=10, unique=True)
    Emergency_Number  = models.CharField(max_length=10)
    Present_Address   = models.CharField(max_length=100)
    Permanent_Address = models.CharField(max_length=100)
    Qualification     = models.CharField(max_length=100)
    
    def add_name(self):
        self.Name = self.First_Name + ' ' + self.Last_Name
        return self.Name
    

class Employment_History(models.Model):
    
    Emp                  = models.ForeignKey(Employee_Details, related_name='parent' ,on_delete=models.CASCADE)
    Emp_Id               = models.CharField(max_length=10, unique=True)
    Previous_CompanyName = models.CharField(max_length=100)
    Designation          = models.CharField(max_length=100)
    Location             = models.CharField(max_length=100)
    Date_of_Employment   = models.CharField(max_length=100)
    Experience           = models.CharField(max_length=100)
    Achievements         = models.CharField(max_length=100)
    Qualification        = models.CharField(max_length=100)
    


class Salary_Management(models.Model):
    
    Emp = models.ForeignKey(Employment_History, on_delete=models.CASCADE)
