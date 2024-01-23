from django.apps import apps
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Загружает данные из приложенных CSV-файлов (static/data)'

    def check_installed_apps(self, app_name):
        if apps.is_installed(app_name):
            self.stdout.write(
                self.style.SUCCESS(f'Приложение "{app_name}" найдено:')
            )
            return True

        self.stdout.write(
            self.style.WARNING(f'Приложение "{app_name}" не найдено')
        )
        return False

    def check_table_exist(self, table_name):
        if table_name in connection.introspection.table_names():
            self.stdout.write(
                self.style.SUCCESS(f'Запись в таблицу "{table_name}":')
            )
            return True
        self.stdout.write(
            self.style.WARNING(f'Приложение "{app_name}" не найдено')
        )
        return False

    def handle(self, *args, **kwargs):
        self.check_installed_apps('titles')
        self.check_installed_apps('core')
        all_tables = 
        print(all_tables)
