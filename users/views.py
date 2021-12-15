from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

User = get_user_model()

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = RegisterForm()
    else:
        # Process completed form.
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('main:index')

    # Diplay a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def profile(request, user_id):
    """Shows a specific user"""
    user = User.objects.get(id = user_id)
    games = user.game_set.order_by('-date_added')
    context = {'user': user, 'games': games}
    return render(request, 'registration/profile.html', context)