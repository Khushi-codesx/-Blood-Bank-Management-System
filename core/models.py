from django.db import models


BLOOD_GROUPS = [
    ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
]
STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Completed', 'Completed'), ('Not Available', 'Not Available')]

# class User(models.Model):
#     fullname = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=10, null=True, blank=True)

#     gender = models.CharField(max_length=20, blank=True)
#     password = models.CharField(max_length=128)
#     # ROLE_CHOICES = (
#     #     ('admin', 'Admin'),
#     #     ('user', 'User'),
#     # )

#     # role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self): return self.fullname


class User(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('donor', 'Donor'),
        ('patient', 'Patient'),
    )

    fullname = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10, null=True, blank=True)

    gender = models.CharField(max_length=20, blank=True)

    password = models.CharField(max_length=128)

    # ⭐ IMPORTANT
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='donor'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.role}"





class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
    logged_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.email

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    # phone = models.CharField(max_length=15, blank=True, null=True)
  
    phone = models.CharField(max_length=10, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class ContactFooter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name



class ContactTeam(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self): return self.name




class Donar(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    fullname = models.CharField(max_length=200)
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    age = models.PositiveIntegerField()
    units = models.PositiveIntegerField()

    date = models.DateField(auto_now_add=True)

    contact = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return self.fullname


# class Donar(models.Model):
#     fullname = models.CharField(max_length=200)
#     bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
#     age = models.PositiveIntegerField()
#     units = models.PositiveIntegerField()
#     date = models.DateField(auto_now_add=True)

#     contact = models.CharField(max_length=10, null=True, blank=True)
#     # contact = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     def __str__(self): return self.fullname



class Patient(models.Model):
    fullname = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    units = models.PositiveIntegerField()
    date = models.DateField()
    contact = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class BloodRequest(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    units = models.PositiveIntegerField(default=1)
    date = models.DateField()
    contact = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    # email = models.EmailField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.fullname} - {self.bloodgroup}'




class BloodDonation(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=18)
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    units = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Approved')
    status = models.CharField(
        max_length=20,
        default='Pending'
    )
 
        # THESE MUST EXIST
    hb_level = models.CharField(max_length=20, null=True, blank=True)
    bp = models.CharField(max_length=20, null=True, blank=True)
    result = models.CharField(max_length=20, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    def __str__(self): return f'{self.fullname} - {self.units} units'

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    # phone = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

 
    email = models.EmailField(blank=True, null=True)
    comments = models.TextField()
    rating = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class BloodStock(models.Model):
    bankname = models.CharField(max_length=150, default='Main Blood Bank')
    address = models.TextField(blank=True, null=True)
    bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS, unique=True)
    units = models.PositiveIntegerField(default=0)
    def __str__(self): return f'{self.bloodgroup} - {self.units} units'
