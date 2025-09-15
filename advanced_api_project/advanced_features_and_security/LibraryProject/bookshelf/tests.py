from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User, Group, Permission

# Get groups
viewers = Group.objects.get(name="Viewers")
editors = Group.objects.get(name="Editors")
admins = Group.objects.get(name="Admins")

# Create test users
viewer_user = User.objects.create_user(username="viewer1", email="v1@test.com", password="pass123")
editor_user = User.objects.create_user(username="editor1", email="e1@test.com", password="pass123")
admin_user = User.objects.create_user(username="admin1", email="a1@test.com", password="pass123")

# Assign to groups
viewer_user.groups.add(viewers)   # only has can_view
editor_user.groups.add(editors)   # has can_view, can_create, can_edit
admin_user.groups.add(admins)     # has can_view, can_create, can_edit, can_delete
