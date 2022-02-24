from django.shortcuts import render,render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.isvalid():
            new_user = form.save()
            login(request,new_user)
            return redirect('learning_logs:index')

    context = {'form':form}
    return render(request, 'registration/register.html', context)
                            

