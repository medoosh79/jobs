from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PersonCreationForm, SignupForm, UserForm, ProfileForm,SigninForm
from .models import Person, City
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'accounts/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'accounts/home.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'accounts/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)




def signup(request):
    if request.method == 'POST':
        formsignup = SignupForm(request.POST)
        if formsignup.is_valid():
            formsignup.save()
            username = formsignup.cleaned_data.get('username')
            password = formsignup.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')

    else:
        context={
            'formsigup':SignupForm(),
            'profileForm': ProfileForm(),
            'formsignin':AuthenticationForm(),
            'password_reset':PasswordResetForm(),
            'formsigup':SignupForm(),
            'resetform':PasswordResetForm(),
        }
            
    
            
    return render (request,'accounts/signup.html', context )


def signin(request):
	if request.method == "POST":
		formsignin = AuthenticationForm(request, data=request.POST)
		if formsignin.is_valid():
			username = formsignin.cleaned_data.get('username')
			password = formsignin.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	formsignin = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"formsignin":formsignin})



def profile(request):
    context={
        'profile':Person.objects.get(user=request.user),
       
    }
   
    return render(request, 'accounts/profile.html', context)
    

def profile_edite(request):
    profile= Person.objects.get(user=request.user)
    if request.method=='POST':
        userform= UserForm(request.POST,  instance=request.user)
        profileform= PersonCreationForm(request.POST,request.FILES, instance=profile)
       
        if userform.is_valid() and profileform.is_valid():          
            userform.save()
            #myprofile= profileform.save(commit=False)          
            #myprofile.user= request.user
            profileform.save() 
            messages.success(request, 'Your account has been updated!')          
            return redirect('profile')
    else:
        userform= UserForm(instance=request.user)
        profileform= PersonCreationForm(instance=profile)
        
    return render(request, 'accounts/profile_edite.html', {'userform':userform, 'profileform':profileform})

def profile_complete(request):
    profile= Person.objects.get(user=request.user)
    if request.method=='POST':
        userform= UserForm(request.POST,  instance=request.user)
        profileform= ProfileForm(request.POST,request.FILES, instance=profile)
       
        if userform.is_valid() and profileform.is_valid():          
            userform.save()
            #myprofile= profileform.save(commit=False)          
            #myprofile.user= request.user
            profileform.save() 
            messages.success(request, 'Your account has been updated!')          
            return redirect('profile')
    else:
        context={
            'userform': UserForm(instance=request.user),
            'profileform': ProfileForm(instance=profile),
        }

    return render(request, 'accounts/profile_complete.html', context)


def logout(request):
    logout(request)
    return render(request, 'index.html')


