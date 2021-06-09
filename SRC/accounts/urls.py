from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

    path('profile',views.profile, name= 'profile'),
    path('signup',views.signup, name= 'signup'),   
    path('profile_edite',views.profile_edite, name= 'profile_edite'),
    path('profile_complete',views.profile_complete, name= 'profile_complete'),        
    path('logout', include('django.contrib.auth.urls')),
    path("signin/", views.signin, name="signin"),
    path('accounts', include('django.contrib.auth.urls')),
    
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html", 
     subject_template_name="accounts/password_reset_email.txt"),
      name= "reset_password"),

    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),

    path('password_change', auth_views.PasswordChangeView.as_view(template_name="accounts/change_password.html"), name="password_change"),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/change_password_done.html"), name="password_change_done"),

]