from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import CustomUserCreationForm, CustomAuthenticatedForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.conf import settings
import time
from django.http import HttpRequest
from django.shortcuts import redirect

# ======================= КОДИ ==========================

def generate_time_based_code():
    now = time.localtime()
    hour = now.tm_hour    
    minute = now.tm_min

    hour = (hour + 5) * 34  # 170 - 986
    minute_tens = minute // 10  
    minute_tens = (minute_tens + 7 )** 2 * 5  #245 - 845

    return f"{hour}{minute_tens}"

def is_code_valid(input_code):
    return input_code == generate_time_based_code()

def send_code_email(user_email, code):
    subject = 'Код підтвердження пошти'
    message = f'Ваш код підтвердження: {code}\nВін дійсний до 10 хвилин.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print(f"Email sent to {user_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
        
# ======================= РЕЄСТРАЦІЯ ==========================

class ViewSignup(CreateView):
    template_name = 'signup/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('verify_email')

    def form_valid(self, form):
        user = form.save()
        code = generate_time_based_code()
        print(user.username, code)
        send_code_email(user.username, code)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'register'
        return context
    
# ======================= ЛОГІН ==========================

class ViewLogin(LoginView):
    template_name = 'login/login.html'
    authentication_form = CustomAuthenticatedForm
    next_page = reverse_lazy('home_app')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'auth'
        return context

# ======================= ВИХІД ==========================

class CustomLogoutView(LogoutView):
    next_page = 'login'

# ======================= ПІДТВЕРДЖЕННЯ КОДУ ==========================

class EmailCodeVerificationView(TemplateView):
    template_name = 'email_code/email_code.html'

    def post(self, request: HttpRequest, *args, **kwargs):
        
        print('post')
        
        input_code1 = str(request.POST.get('code1'))
        print(input_code1)
        input_code2 = str(request.POST.get('code2'))
        print(input_code2)
        input_code3 = str(request.POST.get('code3'))
        print(input_code3)
        input_code4 = str(request.POST.get('code4'))
        print(input_code4)
        input_code5 = str(request.POST.get('code5'))
        print(input_code5)
        input_code6 = str(request.POST.get('code6'))
        print(input_code6)
        
        input_code = input_code1 + input_code2 + input_code3 + input_code4 + input_code5 + input_code6
        print(input_code)
        # input_code = int(input_code)
        print(input_code)
        
        is_valid_code = is_code_valid(input_code=input_code)
        print(is_valid_code)
        if is_valid_code:
            return redirect('login') 
        
        return self.render_to_response({'error': 'Невірний код'})
    