from django import forms as djform
from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = ('requested_role', )


class UserRegistrationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_username": _(
                "This username has already been taken."
            )
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password didn\'t match!')
        return cd['password2']


class ProfileCompleteForm(djform.ModelForm):
    class Meta:
        model = User
        fields = [
            'employee_or_student_id',
            'requested_role',
            'email',
            'approval_extra_note']


class ApprovalProfileUpdateForm(djform.ModelForm):
    class Meta:
        model = User
        fields = ['requested_role']