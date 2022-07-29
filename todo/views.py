from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import login
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from .forms import LoginForm, UserCreateForm, UserUpdateForm, MyPasswordChangeForm
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import render_to_string
from django.urls import reverse_lazy

User = get_user_model()

class Top(TemplateView):
    template_name = 'todo/top.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'todo/login.html'

class Logout(LogoutView):
    template_name = 'todo/top.html'

class UserCreate(CreateView):
    template_name = 'todo/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('todo/mail_template/create/subject.txt', context)
        message = render_to_string('todo/mail_template/create/message.txt', context)

        user.email_user(subject, message)

        return redirect('todo:user_create_done')

class UserCreateDone(TemplateView):
    template_name = 'todo/user_create_done.html'

class UserCreateComplete(TemplateView):
    template_name = 'todo/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATE_TIMEOUT_SECONDS', 60*60*24)

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        except SignatureExpired:
            return HttpResponseBadRequest()

        except BadSignature:
            return HttpResponseBadRequest()

        else:
            try:
                user = User.objects.get(pk=user_pk)

            except User.DoesNotExist:
                return HttpResponseBadRequest()

            else:
                if not user.is_active:
                    user.is_active = True
                    #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserDetail(OnlyYouMixin, DetailView):
    model = User
    template_name = 'todo/user_detail.html'

class UserUpdate(OnlyYouMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'todo/user_form.html'

    def get_success_url(self):
        return resolve_url('todo:user_detail', pk=self.kwargs['pk'])

class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('todo:password_change_done')
    template_name = 'todo/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'todo/password_change_done.html'

# Create your views here.
