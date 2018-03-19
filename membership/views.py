from django.shortcuts import render
from membership.forms import ContactForm
from . import forms
from django.core.mail import EmailMessage
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic.edit import FormView


class ContactFormView(FormView):
    template_name = 'membership/membership.html'
    form_class = ContactForm
    success_url = '/membership'

    def form_valid(self, form):
        print("good form\n")
        form.send_email()
        return super().form_valid(form)


def membership_view(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            print("good form")

            mail_subject = 'MESSAGE FROM UMAAU WEBSITE: {}'.format(form.cleaned_data['subject'])

            message = render_to_string('membership/email.html', {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'msg': form.cleaned_data['suggestion'],
                'mail': form.cleaned_data['email'],
            })

            email = EmailMessage(mail_subject, message, from_email='leadshop@motorhubmagazine.com',
                                 to=['abahoalvin@gmail.com'])
            email.send()

            # subject_to_contact = '{}'.format(form.cleaned_data['subject'])
            # message_to_contact = render_to_string('membership/email_to_contact.html', {
            #     'first_name': form.cleaned_data['first_name'],
            #     'last_name': form.cleaned_data['last_name'],
            #     'msg': form.cleaned_data['suggestion'],
            #     'mail': form.cleaned_data['email'],
            # })
            # contact_email = '{}'.format(form.cleaned_data['email'])
            # email = EmailMessage(subject_to_contact, message_to_contact,
            #                      from_email='leadshop@motorhubmagazine.com',
            #                      to=[contact_email]),
            # email.send()

            return HttpResponseRedirect(reverse('membership:membership'))

    return render(request, 'membership/membership.html', {'form': form})

