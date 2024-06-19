from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from sweets.models import Order

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Admin')
        customer_group, created = Group.objects.get_or_create(name='Customer')
        delivery_group, created = Group.objects.get_or_create(name='Delivery')

        # Get permissions
        order_content_type = ContentType.objects.get_for_model(Order)
        view_order_permission = Permission.objects.get(codename='view_order', content_type=order_content_type)
        add_order_permission = Permission.objects.get(codename='add_order', content_type=order_content_type)
        change_order_permission = Permission.objects.get(codename='change_order', content_type=order_content_type)
        delete_order_permission = Permission.objects.get(codename='delete_order', content_type=order_content_type)

        # Assign permissions to groups
        admin_group.permissions.set([view_order_permission, add_order_permission, change_order_permission, delete_order_permission])
        customer_group.permissions.set([view_order_permission, add_order_permission])
        delivery_group.permissions.set([view_order_permission, change_order_permission])

        self.stdout.write(self.style.SUCCESS('Groups and permissions have been set up'))
