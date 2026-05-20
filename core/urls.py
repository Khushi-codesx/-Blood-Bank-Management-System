from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('donar/', views.donar, name='donar'),
    path('donarform/', views.donarform, name='donarform'),
    path('patient/', views.patient, name='patient'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),

    path('donor/login/', views.donor_login, name='donor_login'),
path('donor/register/', views.donor_register, name='donor_register'),
 path('donor/history/', views.donor_history, name='donor_history'),
path('donor/dashboard/', views.donordashboard, name='donordashboard'),


    path('patient/login/', views.patient_login, name='patient_login'),
path('patient/register/', views.patient_register, name='patient_register'),
 path('patient/history/', views.patient_history, name='patient_history'),
path('patient/dashboard/', views.patientdashboard, name='patientdashboard'),

    path('logout/', views.logout_view, name='logout'),
    path('bloodstock/', views.bloodstock, name='bloodstock'),
    path('bloodrequest/', views.bloodrequest, name='bloodrequest'),
    path('approve/<int:id>/', views.approve_request, name='approve'),
    path('reject/<int:id>/', views.reject_request, name='reject'),
    path('donation/', views.donation, name='donation'),
    path('bloodbank/', views.bloodbank, name='bloodbank'),
    path('faq/', views.faq, name='faq'),
    path('bloodcamp/', views.bloodcamp, name='bloodcamp'),
    path('contact/', views.contact, name='contact'),
    # path('contactteam/', views.contact_team, name='contactteam'),
    path('contact-team/', views.contact_team, name='contact_team'),
    path('contactfooter/', views.contactfooter, name='contactfooter'),
    path('feedback/', views.feedback, name='feedback'),
    path('gallery/', views.gallery, name='gallery'),
    path('registration/', views.register, name='registration'),
    path('register/', views.register, name='register'),
    path('thanks/', views.thanks, name='thanks'),
    path('terms/', views.terms, name='terms'),
    path('help/', views.help, name='help'),
    path('lab-testing/<int:id>/', views.lab_testing, name='lab_testing'),
  
   path(
    'update-status/<int:id>/<str:status>/',
    views.update_status,
    name='update_status'
),
]
