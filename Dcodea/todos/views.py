from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Todo, UserProfile
from .forms import TodoForm ,IntroductionForm

# Create your views here.

@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo')
    else:
        form = TodoForm()

    todos = Todo.objects.filter(user=request.user).order_by('date')
    return render(request, 'main.html', 
                  {'form': form, 'todos': todos, 
                   'userName': request.user.username})
@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = IntroductionForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = IntroductionForm(instance=user_profile)
    
    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})