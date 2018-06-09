from django import forms
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not Empty')


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='please verify your email address')
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               # validators=[validators.MaxLengthValidator(0)],
                               validators=[must_be_empty]
                               )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )

    def send_email(self):
        # mail_subject = 'MESSAGE FROM UMAAU WEBSITE: {}'.format(self.cleaned_data['subject'])
        mail_subject = 'MESSAGE FROM UNIVERSITY OF MANCHESTER UGANDA ALUMNI WEBSITE'
        message = render_to_string('membership/email.html', {
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'msg': self.cleaned_data['suggestion'],
            'mail': self.cleaned_data['email'],
        })

        email = EmailMessage(mail_subject, message, from_email='arms143mro@gmail.com',
                             to=['abahoalvin@gmail.com'])

        print("EMAIL MESSAGE: \n", email)

        email.send()
