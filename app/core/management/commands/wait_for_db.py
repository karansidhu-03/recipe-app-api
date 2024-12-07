"""
Django command to wait for database
"""

import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):

        self.stdout.write("Waiting for Database...")
        while True:
            try:
                self.check(databases=["default"])
                break
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable ,waiting for 1 second")
                time.sleep(1)
        self.stdout.write("Database Available!")
