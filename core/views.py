import vk
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'core/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/private/")
        return super().get(request, *args, **kwargs)


class PrivateView(TemplateView):
    template_name = 'core/private.html'

    def get_context_data(self, **kwargs):
        if not self.request.user.is_authenticated:
            raise PermissionDenied('Please sign in first')
        social = self.request.user.social_auth.get(provider='vk-oauth2')
        access_token = social.extra_data.get('access_token')
        session = vk.Session(access_token=access_token)
        api = vk.API(session)
        friends = api.friends.get(
            v='5.0',
            count=5,
            fields=['nickname', 'photo_50']
        )

        return {'friends': friends}
