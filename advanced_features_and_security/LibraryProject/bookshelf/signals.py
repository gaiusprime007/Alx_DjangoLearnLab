# from django.contrib.auth.models import Group, Permission
# from django.apps import apps
# from .models import CustomUser

# def setup_groups_and_permissions():
#     Group = apps.get_model('auth', 'Group')
#     Permission = apps.get_model('auth', 'Permission')
#     CustomUser = apps.get_model('bookshelf', 'CustomUser')

#     # Define groups and their permissions
#     groups_permissions = {
#         'Admin': ['add_customuser', 'change_customuser', 'delete_customuser', 'view_customuser'],
#         'Editor': ['change_customuser', 'view_customuser'],
#         'Viewer': ['view_customuser'],
#     }

#     for group_name, perm_codenames in groups_permissions.items():
#         group, created = Group.objects.get_or_create(name=group_name)
#         permissions = Permission.objects.filter(codename__in=perm_codenames)
#         group.permissions.set(permissions)
#         group.save()


from django.contrib.auth.models import Group, Permission
from django.apps import apps


def setup_groups_and_permissions():
    CustomUser = apps.get_model("accounts", "CustomUser")

    # Get permissions
    can_view = Permission.objects.get(codename="can_view")
    can_create = Permission.objects.get(codename="can_create")
    can_edit = Permission.objects.get(codename="can_edit")
    can_delete = Permission.objects.get(codename="can_delete")

    # Create groups
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    viewers.permissions.set([can_view])
    editors.permissions.set([can_view, can_create, can_edit])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])
