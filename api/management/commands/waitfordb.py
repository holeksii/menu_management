import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Wait to connect to db until db is initialised"""

    def handle(self, *args, **options):
        start = time.time()
        self.stdout.write("Waiting for database...")
        can_connect = False
        while not can_connect:
            try:
                connection.ensure_connection()
                can_connect = True
            except OperationalError:
                time.sleep(0.5)

        end = time.time()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database available! Time taken: {end-start:.4f} second(s)"
            )
        )
