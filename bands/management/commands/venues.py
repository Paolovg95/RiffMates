# RiffMates/bands/management/commands/musicians.py
from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from bands.models import Venue, Room

class Command(BaseCommand):
    help = "List all venues"

    def add_arguments(self, parser, action="store_true"):
        parser.add_argument("--rooms", "-r", help=("List all rooms associated with a venue"))

    def handle(self, *args, **options):
        venues = Venue.objects.all()
        if options['rooms']:
            venue = Venue.objects.get(name=options["rooms"])
            rooms = venue.room_set.all()
            for room in rooms:
                self.stdout.write(f"{room.room_name}")
        else:
            for venue in venues:
                self.stdout.write(f"{venue.name}")
