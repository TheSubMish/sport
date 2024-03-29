from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import path,include,reverse_lazy
from django.conf.urls.static import static
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

class CustomAdminLoginView(LoginView):
    def form_valid(self, form: AuthenticationForm) -> HttpResponseRedirect:
        username = form.data.get('username')
        password = form.data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)

        if self.request.user.is_superuser:
            return HttpResponseRedirect('/admin')
        
        return HttpResponseRedirect(reverse_lazy('home-page'))
        

admin.site.login = CustomAdminLoginView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('src.apps.olympic.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)