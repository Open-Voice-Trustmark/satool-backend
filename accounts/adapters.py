from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):
	def save_user(self, request, user, form, commit=True):
		from allauth.account.utils import user_field

		user = super(CustomAccountAdapter, self) \
			.save_user(request, user, form, False)

		data = form.cleaned_data
		terms_accepted = data.get("terms_accepted")
		
		setattr(user, "terms_accepted", terms_accepted)
		
		if commit:
			user.save()
		return user

	def get_email_confirmation_url(self, request, emailconfirmation):
		url = settings.FRONTEND_SERVER_URL + '/accounts/verification/' + emailconfirmation.key
		return url