# RiffMates/bands/management/commands/musicians.py
from django.core.management.base import BaseCommand, CommandError
from bands.models import Musician
from datetime import datetime
class Command(BaseCommand):
    help = "Lists registered musicians" # Provide a help string for the --help command-line flag

    def add_arguments(self, parser):
        parser.add_argument("--first_name", "-f", help=("Query musicians "
            "whose first name is greater than or equal to this value. "
            "Note this is case sensitive."))
        parser.add_argument("--last_name", "-l", help=("Query musicians whose last name is greater than or equal"
                " to this value. Note this is case sensitive."
            ))
        parser.add_argument("--birth_date", "-b", help=("Query musicians "
            "whose birth date is greater than or equal to this value. "
            "Date must be given in YYYY-MM-DD format."))

    def handle(self, *args, **options):
        musicians = Musician.objects.all()
        if options["last_name"]:
            musicians = Musician.objects.filter(first_name__gte=options["last_name"])
        if options["first_name"]:
            musicians = Musician.objects.filter(first_name__gte=options["first_name"])
        if options["birth_date"]:
            try:
                birth_date = datetime.strptime(
                    options["birth_date"], "%Y-%m-%d"
                )
            except ValueError:
                raise CommandError(
                    "Birth date must be provided in YYYY-MM-DD format")

            musicians = Musician.objects.filter(birth_date__gte=birth_date)


        for musician in musicians:
            self.stdout.write(
                f"{musician.last_name}, {musician.first_name} - {musician.birth_date}"
            )
