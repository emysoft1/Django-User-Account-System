from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ContactForm
from .models import Contact, Department

class ContactFormView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    template_name = 'contact_app/contact.html' 
    form_class = ContactForm 
    success_url = '/contact/' 
    success_message = "Your message has been sent successfully."

    def form_valid(self, form):
        # Handle the form submission
        user = self.request.user
        department_id = form.cleaned_data['department'].id
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Create a new contact entry
        contact = Contact.objects.create(
            user=user,
            department_id=department_id,
            subject=subject,
            message=message
        )

        # Get the selected department's email address
        department = Department.objects.get(id=department_id)
        department_email = department.email

        # Send the email
        send_mail(
            subject,
            message,
            user.email,  # Use the logged-in user's email as the sender email
            [department_email],
            fail_silently=False,
        )

        return super().form_valid(form)
