import csv
from django.core.management.base import BaseCommand
from jobscrape_api.models import JobLanguages, JobFrameworks, JobDatabases, JobSkills

class Command(BaseCommand):
    help = 'Loads job skills data from CSV file into database'

    def handle(self, *args, **kwargs):
        if JobLanguages.objects.count() == 0:
            with open('./media/csv/languages.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    language = JobLanguages(
                        language=row['languages']
                    )

                    # Save the object to the database
                    language.save()

            self.stdout.write(self.style.SUCCESS('JobLanguages loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('JobLanguages already exists, skipping data load'))


        if JobFrameworks.objects.count() == 0:
            with open('./media/csv/frameworks.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    framework = JobFrameworks(
                        framework=row['frameworks']
                    )

                    framework.save()

            self.stdout.write(self.style.SUCCESS('JobFrameworks loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('JobFrameworks already exists, skipping data load'))

        
        if JobDatabases.objects.count() == 0:
            with open('./media/csv/databases.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    database = JobDatabases(
                        database=row['databases']
                    )

                    database.save()

            self.stdout.write(self.style.SUCCESS('JobDatabases loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('JobDatabases already exists, skipping data load'))

        
        if JobSkills.objects.count() == 0:
            with open('./media/csv/skills.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    skill = JobSkills(
                        skill=row['skills']
                    )

                    skill.save()

            self.stdout.write(self.style.SUCCESS('JobSkills loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('JobSkills already exists, skipping data load'))

    