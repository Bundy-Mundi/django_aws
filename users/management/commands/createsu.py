from django.core.management.base import BaseCommand, CommandError
from users.models import User
import os

class Command(BaseCommand):

    help = "This Command Creates a Superuser!!!"

    def handle(self, *args, **options):
        eb_id = os.environ.get("EB_SUPERUSER_ID")
        eb_email = os.environ.get("EB_SUPERUSER_EMAIL")
        eb_password = os.environ.get("EB_SUPERUSER_PASSWORD")
        try:
            user_exist = User.objects.get(username=eb_id)
            raise CommandError("Superuser Already Exists.")
        except User.DoesNotExist:
            User.objects.create_superuser(eb_id, eb_email, eb_password)
            self.stdout.write("Superuser Created")