from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView
from .models import CustomUser

class EditProfileView(PermissionRequiredMixin, UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "date_of_birth", "profile_photo"]
    template_name = "bookshelf/edit_profile.html"
    permission_required = "bookshelf.can_edit"  # check for this permission
    raise_exception = True  # optional, raises 403 instead of redirecting
