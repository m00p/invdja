from django.shortcuts import redirect, get_object_or_404,render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.contrib.auth.models import User


from accounts.forms import SignupForm


def signup(request, signup_form=SignupForm, template_name='accounts/signup.html', success_url=None, extra_context=None):

    form = signup_form()
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user = form.save()

            if success_url: redirect_to = success_url
            else: redirect_to = reverse('accounts_signup_complete',
                                        kwargs={'username': user.username})
            return redirect(redirect_to)

    data = { 'form': form, }
    return render_to_response(template_name, data, context_instance=RequestContext(request))


def direct_to_user_template(request, username, template_name, extra_context=None):

    user = get_object_or_404(User, username__iexact=username)

    if not extra_context: extra_context = dict()
    extra_context['viewed_user'] = user
    return direct_to_template(request,
                              template_name,
                              extra_context=extra_context)
