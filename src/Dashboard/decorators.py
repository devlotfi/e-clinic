from django.shortcuts import redirect

def login_not_required(view_func):
  def wrapper(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('dashboard')
    else:
      return view_func(request, *args, **kwargs)

  return wrapper
