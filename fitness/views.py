from django.shortcuts import render, redirect
from .models import FitnessActivity, DietaryLog, WeightEntry, UserProfile
from .forms import UserRegisterForm, ActivityForm, DietaryLogForm, WeightEntryForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

# write the activity list view
@login_required
def activity_list(request):
    activities = FitnessActivity.objects.filter(user=request.user)
    return render(request, 'fitness/activity_list.html', {'activities': activities})

# write the login view
def custom_logout(request):
    logout(request)
    return redirect('login')

# write the 404 view
def custom_404(request, exception):
    return render(request, 'fitness/404.html', status=404)

# write the activity log view
@login_required
def diet_log(request):
    diet_logs = DietaryLog.objects.filter(user=request.user)
    return render(request, 'fitness/diet_log.html', {'diet_logs': diet_logs})

# write the register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'fitness/register.html', {'form': form})

# write the home view
def home(request):
    if request.user.is_authenticated:
        return render(request, 'fitness/home.html')
    return render(request, 'fitness/landing.html')  


# write the about view
@login_required
def malcare_doc(request):
    context = {
        "api_key": settings.API_KEY,
        "azure_openai_endpoint": settings.AZURE_OPENAI_ENDPOINT,
        "azure_openai_api_key": settings.AZURE_OPENAI_API_KEY,
        "azure_openai_deployment": settings.AZURE_OPENAI_DEPLOYMENT
    }
    return render(request, 'fitness/malcare.html', context)

# add activity view
@login_required
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()  # Make sure this line is correct

    return render(request, 'fitness/add_activity.html', {'form': form})

# add diet log view
@login_required
def add_diet_log(request):
    if request.method == 'POST':
        form = DietaryLogForm(request.POST)
        if form.is_valid():
            dietary_log = form.save(commit=False)
            dietary_log.user = request.user  # Set the user to the current user
            dietary_log.save()
            return redirect('diet_log')
    else:
        form = DietaryLogForm()
    return render(request, 'fitness/add_diet_log.html', {'form': form})

# weight tracker view
@login_required
def weight_tracker(request):
    if request.method == 'POST':
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.user = request.user
            weight_entry.save()
            return redirect('weight_tracker')
    else:
        form = WeightEntryForm()

    # Fetch weight entries for the graph
    weight_entries = WeightEntry.objects.filter(user=request.user).order_by('date')
    dates = [entry.date.strftime("%Y-%m-%d") for entry in weight_entries]
    weights = [entry.weight for entry in weight_entries]

    return render(request, 'fitness/weight_tracker.html', {
        'form': form, 
        'dates': dates, 
        'weights': weights
    })

# login view
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user': request.user,
        'user_profile': user_profile
    }
    return render(request, 'fitness/profile.html', context)


# a function to view 