from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts.models import Profile


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "second_name",
            "document_number",
            "age",
            "address",
            "email_address",
            "phone_number",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "second_name",
            "document_number",
            "age",
            "address",
            "email_address",
            "phone_number",
            "is_active",
            "is_admin",
        )


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "first_name",
        "second_name",
        "document_number",
        "age",
        "address",
        "email_address",
        "phone_number",
        "is_admin",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email_address", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "second_name",
                    "document_number",
                    "age",
                    "address",
                    "phone_number",
                )
            },
        ),
        ("Permissions", {"fields": ("is_admin", "is_staff", "is_active")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "second_name",
                    "document_number",
                    "age",
                    "address",
                    "email_address",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email_address",)
    ordering = ("email_address",)
    filter_horizontal = ()


admin.site.register(Profile, UserAdmin)

User = get_user_model()


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("users", False),
    )

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["users"].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data["users"])

    def save(self, *args, **kwargs):
        instance = super(GroupAdminForm, self).save()
        self.save_m2m()
        return instance


admin.site.unregister(Group)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ["permissions"]

    def save_model(self, request, obj, form, change):
        super(GroupAdmin, self).save_model(request, obj, form, change)
        if "users" in form.cleaned_data:
            form.instance.user_set.set(form.cleaned_data["users"])


admin.site.register(Group, GroupAdmin)
