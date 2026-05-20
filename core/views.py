from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta


from .models import User, Login, Donar, Patient, Contact, Feedback, BloodStock, BloodRequest, BloodDonation,ContactFooter,ContactTeam




def is_logged_in(request):
    return request.session.get('user_id') is not None

def index(request): return render(request, 'index.html')
def home(request): return render(request, 'home.html')
def donar(request): return render(request, 'donar.html')
def bloodbank(request): return render(request, 'bloodbank.html')
def gallery(request): return render(request, 'gallery.html')
def thanks(request): return render(request, 'thanks.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip().lower()
        phone = request.POST.get('phone', '').strip()
        gender = request.POST.get('gender', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        if not fullname or not email or not phone or not password:
            messages.error(request, 'All required fields are mandatory.')
        elif password != confirm_password:
            messages.error(request, 'Password and confirm password do not match.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            User.objects.create(fullname=fullname, email=email, phone=phone, gender=gender, password=make_password(password))
            messages.success(request, 'Registration successful. Please login.')
            return redirect('admin_login')
    return render(request, 'register.html')


# def donor_register(request):

#     if request.method == "POST":

#         User.objects.create(
#             fullname=request.POST.get('fullname'),
#             email=request.POST.get('email'),
#             phone=request.POST.get('phone'),
#             password=make_password(request.POST.get('password')),
#             confirm_password = request.POST.get('confirm_password', '')
#         )

#         return redirect('donor_login')

#     return render(request, 'donor_register.html')



 
def donor_register(request):

    if request.method == "POST":

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # ❌ password check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('donor_register')

        # ❌ EMAIL DUPLICATE CHECK (IMPORTANT)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please login.")
            return redirect('donor_register')

        # ✅ SAVE USER
        User.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            password=make_password(password)
        )

        messages.success(request, "Registration successful")
        return redirect('donor_login')

    return render(request, 'donor_register.html')

def donor_login(request):

    if request.method == "POST":

        email = request.POST.get('email')
   
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):

            request.session['user_id'] = user.id
            request.session['user_name'] = user.fullname
            request.session['user_email'] = user.email   # ✅ ADD THIS
            request.session['role'] = "donor"

            return redirect('donordashboard')

        messages.error(request, "Invalid credentials")

    return render(request, 'donor_login.html')









def patient_register(request):

    if request.method == "POST":

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # ❌ password check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('patient_register')

        # ❌ EMAIL DUPLICATE CHECK (IMPORTANT)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please login.")
            return redirect('patient_register')

        # ✅ SAVE USER
        User.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            password=make_password(password)
        )

        messages.success(request, "Registration successful")
        return redirect('patient_login')

    return render(request, 'patient_register.html')

def patient_login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password):

            request.session['user_id'] = user.id
            request.session['user_name'] = user.fullname
            request.session['user_email'] = user.email
            request.session['role'] = "patient"

            return redirect('patientdashboard')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'patient_login.html')

    return render(request, 'patient_login.html')




# def patient_login(request):

#     if request.method == "POST":

#         email = request.POST.get('email')
#         password = request.POST.get('password')

    #     user = User.objects.filter(email=email).first()

    #     if user and check_password(password, user.password):

    #         request.session['user_id'] = user.id
    #         request.session['user_name'] = user.fullname
    #         request.session['user_email'] = user.email

    #         # ✅ FIXED ROLE
    #         request.session['role'] = "patient"

    #         # ✅ FIXED REDIRECT
    #         return redirect('patientdashboard')

    #     messages.error(request, "Invalid credentials")

    # return render(request, 'patient_login.html')
        
      

# def donor_login(request):

#     if request.method == "POST":

#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = User.objects.filter(email=email).first()

#         if user and check_password(password, user.password):

#             request.session['user_id'] = user.id
#             request.session['user_name'] = user.fullname
#             request.session['role'] = "donor"

#             return redirect('donordashboard')

#         messages.error(request, "Invalid credentials")

#     return render(request, 'donor_login.html')





# def admin_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email', '').strip().lower()
#         password = request.POST.get('password', '')
#         user = User.objects.filter(email=email).first()
#         if user and check_password(password, user.password):
#             request.session['user_id'] = user.id
#             request.session['user_name'] = user.fullname
#             Login.objects.create(email=email, password='hidden')
#             messages.success(request, 'Login successful.')
#             return redirect('admindashboard')
#         messages.error(request, 'Invalid email or password.')
#     return render(request, 'login.html')
def admin_login(request):

    if request.method == 'POST':

        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        # ✅ HARD-CODED ADMIN LOGIN
        if email == "admin@gmail.com" and password == "admin":

            request.session['user_id'] = 1
            request.session['user_name'] = "Admin"
            request.session['role'] = "admin"

            messages.success(request, "Admin login successful")

            return redirect('admindashboard')

        # ❌ INVALID ADMIN LOGIN
        else:
            messages.error(request, "Only admin can login with valid credentials")

    return render(request, 'login.html')
   

def logout_view(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully.')
    return redirect('home')

# def donordashboard(request):

#     # 🔥 ADMIN BYPASS CHECK
#     if request.session.get('role') == "admin":
#         return render(request, 'donordashboard.html')

#     # 🔥 NORMAL USER CHECK
#     if request.session.get('role') != "donor":
#         return redirect('donor_login')

#     return render(request, 'donordashboard.html')

def donordashboard(request):

    # 🔥 ADMIN VIEW
    if request.session.get('role') == "admin":
        donations = Donar.objects.all().order_by('-date')
        return render(request, 'donordashboard.html', {
            'donations': donations
        })

    # 🔥 DONOR CHECK
    if request.session.get('role') != "donor":
        return redirect('donor_login')

    # 🔥 SAFE EMAIL GET
    email = request.session.get('user_email')

    # 🔥 DEBUG (optional)
    print("LOGGED EMAIL:", email)

    # 🔥 IF EMAIL IS MISSING
    if not email:
        return redirect('donor_login')

    donations = Donar.objects.filter(
        email=email
    ).order_by('-date')

    return render(request, 'donordashboard.html', {
        'donations': donations
    })


# ==============================================================
def bloodrequest(request):

    if not request.session.get('user_id'):
        return redirect('admin_login')

    role = request.session.get('role')

    # 🔥 ADMIN: sees ALL requests
    if role == "admin":
        requests = BloodRequest.objects.all().order_by('-id')

    # 🔥 PATIENT: sees ONLY own requests
    elif role == "patient":
        requests = BloodRequest.objects.filter(
            email=request.session.get('user_email')
        ).order_by('-id')

    # 🔥 DONOR or others: block or redirect
    else:
        return redirect('home')

    return render(request, 'bloodrequest.html', {
        'requests': requests
    })



def patientdashboard(request):

    if request.session.get('role') == "admin":
        requests = BloodRequest.objects.all().order_by('-id')
        return render(request, 'patientdashboard.html', {
            'requests': requests
        })

    if request.session.get('role') != "patient":
        return redirect('patient_login')

    email = request.session.get('user_email')

    print("LOGGED EMAIL:", email)

    if not email:
        return redirect('patient_login')


    requests = BloodRequest.objects.filter(
    email=request.session.get('user_email')
).order_by('-id')

    return render(request, 'patientdashboard.html', {
        'requests': requests
    })



# def patientdashboard(request):

#     role = request.session.get('role')

#     if not role:
#         return redirect('login')

#     if role not in ['patient', 'admin']:
#         return redirect('home')

#     requests = BloodRequest.objects.filter(
#         fullname=request.session.get('user_name')
#     ).order_by('-id')

#     return render(request, 'patientdashboard.html', {
#         'requests': requests
#     })
    
# def admindashboard(request):
#     if not is_logged_in(request): return redirect('admin_login')
#     context = {
#         'stocks': BloodStock.objects.all().order_by('bloodgroup'),
#         'total_donors': Donar.objects.count(),
#         'total_patients': Patient.objects.count(),
#         'total_requests': BloodRequest.objects.count(),
#         'total_units': BloodStock.objects.aggregate(total=Sum('units'))['total'] or 0,
#     }
#     return render(request, 'admindashboard.html', context)

def admindashboard(request):

    if not is_logged_in(request):
        return redirect('admin_login')

    if request.session.get('role') != 'admin':
        return redirect('home')

    context = {
        'stocks': BloodStock.objects.all().order_by('bloodgroup'),
        'total_donors': Donar.objects.count(),
        'total_patients': Patient.objects.count(),
        'total_requests': BloodRequest.objects.count(),
        'total_units': BloodStock.objects.aggregate(total=Sum('units'))['total'] or 0,
    }

    return render(request, 'admindashboard.html', context)



def bloodstock(request):
    return render(request, 'bloodstock.html', {'stocks': BloodStock.objects.all().order_by('bloodgroup')})

# def bloodrequest(request):
#     if not is_logged_in(request): return redirect('admin_login')
#     return render(request, 'bloodrequest.html', {'requests': BloodRequest.objects.all().order_by('-id')})



def approve_request(request, id):
    if not is_logged_in(request): return redirect('admin_login')
    req = get_object_or_404(BloodRequest, id=id)
    stock = BloodStock.objects.filter(bloodgroup=req.bloodgroup).first()
    if stock and stock.units >= req.units:
        stock.units -= req.units
        stock.save()
        req.status = 'Completed'
        BloodDonation.objects.create(fullname=req.fullname, age=req.age, bloodgroup=req.bloodgroup, units=req.units, status='Approved')
        messages.success(request, 'Request approved and stock updated.')
    else:
        req.status = 'Not Available'
        messages.warning(request, 'Insufficient stock for this blood group.')
    req.save()
    return redirect('bloodrequest')

def reject_request(request, id):
    if not is_logged_in(request): return redirect('admin_login')
    req = get_object_or_404(BloodRequest, id=id)
    req.status = 'Rejected'
    req.save()
    messages.info(request, 'Request rejected.')
    return redirect('bloodrequest')

def donation(request):
    if not is_logged_in(request): return redirect('admin_login')
    return render(request, 'donation.html', {'donations': BloodDonation.objects.all().order_by('-id')})

def donor_history(request):

    if not request.session.get('user_id'):
        return redirect('donor_login')

    email = request.session.get('user_email')

    history = Donar.objects.filter(email=email).order_by('-date')

    return render(request, 'donor_history.html', {'history': history})



# def donor_history(request):

#     if request.session.get('role') != "donor":
#         return redirect('donor_login')

#     email = request.session.get('email')

#     donations = Donar.objects.filter(email=email).order_by('-date')

#     return render(request, 'donor_history.html', {
#         'donations': donations
#     })

def patient_history(request):

    if not request.session.get('user_id'):
        return redirect('patient_login')

    email = request.session.get('user_email')

    history = BloodRequest.objects.filter(email=email).order_by('-id')

    return render(request, 'patient_history.html', {
        'history': history
    })






def donarform(request):

    if request.method == 'POST':

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')

        # 🔍 LAST DONATION (ONLY BY EMAIL - RELIABLE)
        last_donation = Donar.objects.filter(
            email=email
        ).order_by('-date').first()

        # ⛔ 90 DAYS VALIDATION
        if last_donation:

            last_date = last_donation.date
            today = timezone.now().date()

            next_allowed_date = last_date + timedelta(days=90)

            if today < next_allowed_date:
                remaining = (next_allowed_date - today).days

                messages.error(
                    request,
                    f"You can donate again after {remaining} days."
                )
                return redirect('donor_history')

        # 💾 CREATE DONOR (AUTO DATE — NO USER INPUT DATE)
        donor = Donar.objects.create(
            fullname=fullname,
            age=request.POST.get('age'),
            bloodgroup=request.POST.get('bloodgroup'),
            units=int(request.POST.get('units') or 0),
            contact=request.POST.get('contact'),
            address=request.POST.get('address'),
            email=email,
            date=timezone.now().date()   # 🔥 IMPORTANT FIX
        )

        # 📦 BLOOD STOCK UPDATE
        stock, _ = BloodStock.objects.get_or_create(
            bloodgroup=donor.bloodgroup,
            defaults={
                'bankname': 'Main Blood Bank',
                'units': 0
            }
        )

        stock.units += donor.units
        stock.save()

        # 📦 OPTIONAL: DONATION HISTORY LOG
        BloodDonation.objects.create(
            fullname=donor.fullname,
            age=donor.age,
            bloodgroup=donor.bloodgroup,
            units=donor.units,
            status='Pending'
        )

        messages.success(request, "Donation successful!")
        return redirect('thanks')

    return render(request, 'donarform.html')

# def donarform(request):
#     if request.method == 'POST':
#         donor = Donar.objects.create(
#             fullname=request.POST.get('fullname'), age=request.POST.get('age'), bloodgroup=request.POST.get('bloodgroup'),
#             units=int(request.POST.get('units') or 0), date=request.POST.get('date'), contact=request.POST.get('contact'),
#             address=request.POST.get('address'), email=request.POST.get('email')
#         )
#         stock, _ = BloodStock.objects.get_or_create(bloodgroup=donor.bloodgroup, defaults={'bankname': 'Main Blood Bank', 'address': donor.address or '', 'units': 0})
#         stock.units += donor.units
#         stock.save()
#         BloodDonation.objects.create(fullname=donor.fullname, age=donor.age, bloodgroup=donor.bloodgroup, units=donor.units, status='Approved')
#         messages.success(request, 'Donor added and blood stock updated.')
#         return redirect('thanks')
#     return render(request, 'donarform.html')



def patient(request):

    if request.method == 'POST':

        if not request.session.get('user_id'):
            return redirect('patient_login')

        user_email = request.session.get('user_email')

        patient_obj = Patient.objects.create(
            fullname=request.POST.get('fullname'),
            age=request.POST.get('age'),
            bloodgroup=request.POST.get('bloodgroup'),
            units=int(request.POST.get('units') or 0),
            date=request.POST.get('date'),
            contact=request.POST.get('contact'),
            address=request.POST.get('address'),
        )

        BloodRequest.objects.create(
            fullname=patient_obj.fullname,
            age=patient_obj.age,
            bloodgroup=patient_obj.bloodgroup,
            units=patient_obj.units,
            date=patient_obj.date,
            contact=patient_obj.contact,
            address=patient_obj.address,
            email=user_email,   # ⭐ THIS IS KEY
            status='Pending'
        )

        messages.success(request, 'Blood request submitted successfully.')
        return redirect('patientdashboard')

    return render(request, 'patient.html')
# def patient(request):
#     if request.method == 'POST':
#         patient_obj = Patient.objects.create(
#             fullname=request.POST.get('fullname'), age=request.POST.get('age'), bloodgroup=request.POST.get('bloodgroup'),
#             units=int(request.POST.get('units') or 0), date=request.POST.get('date'), contact=request.POST.get('contact'),
#             address=request.POST.get('address'), email=request.POST.get('email')
#         )
#         BloodRequest.objects.create(fullname=patient_obj.fullname, age=patient_obj.age, bloodgroup=patient_obj.bloodgroup, units=patient_obj.units, date=patient_obj.date, contact=patient_obj.contact, address=patient_obj.address, status='Pending')
#         messages.success(request, 'Blood request submitted successfully.')
#         return redirect('thanks')
#     return render(request, 'patient.html')

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(name=request.POST.get('name'), email=request.POST.get('email'), phone=request.POST.get('phone'), message=request.POST.get('message'))
        messages.success(request, 'Thank you! Our team will contact you soon.')
        return redirect('thanks')
    return render(request, 'contact.html')

def feedback(request):
    if request.method == 'POST':
        Feedback.objects.create(name=request.POST.get('name'), phone=request.POST.get('phone'), email=request.POST.get('email'), comments=request.POST.get('comments'), rating=request.POST.get('rating'))
        messages.success(request, 'Thanks for your feedback.')
        return redirect('thanks')
    return render(request, 'feedback.html')

def bloodcamp(request):
    return render(request,'bloodcamp.html')

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')


def terms(request):
    return render(request,'TermsCondition.html')


def contactfooter(request):
    if request.method == 'POST':
        ContactFooter.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(request, 'Thank you! Our team will contact you soon.')
        return redirect('thanks')

    return render(request, 'contactfooter.html')


def contact_team(request):
    if request.method == 'POST':

        print("POST DATA:", request.POST)

        name = request.POST.get('name')
        message = request.POST.get('message')

        print("NAME:", name)
        print("MESSAGE:", message)

        ContactTeam.objects.create(
            name=name,
            message=message
        )

        return redirect('thanks')

    return render(request, 'base.html')

def lab_testing(request, id):

    record = BloodDonation.objects.get(id=id)

    if request.method == "POST":
        record.hb_level = request.POST.get('hb_level')
        record.bp = request.POST.get('bp')
        record.result = request.POST.get('result')
        record.remarks = request.POST.get('remarks')

        record.status = "Lab Tested"
        record.save()

        return redirect('donation')

    return render(request, 'lab_testing.html', {'record': record})




def update_status(request, id, status):

    donation = get_object_or_404(BloodDonation, id=id)

    donation.status = status
    donation.save()

    return redirect('donation')
