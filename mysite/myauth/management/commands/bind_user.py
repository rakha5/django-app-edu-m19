from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=4)
        group, created = Group.objects.get_or_create(
            name='profile_manager',
        )
        permission_profile = Permission.objects.get(
            codename='view_profile',
        )
        permission_logentry = Permission.objects.get(
            codename='view_logentry',
        )

        # add permissiom to group
        group.permissions.add(permission_profile)

        # add user to group
        user.groups.add(group)

        # add permission directly to user
        user.user_permissions.add(permission_logentry)

        group.save()
        user.save()

