import csv

from django.apps import apps
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Загружает данные из приложенных CSV-файлов (static/data)'

    def print_divider(self):
        """Печатает разделитель в вывод."""
        self.stdout.write(
            self.style.SUCCESS(
                '---------------------------------------------------------'
            )
        )

    def get_data_file_path(self, data_file_name):
        """Проверяет существует ли файл с данными.

        Parameters
        ----------
        data_file_name : str
            Пусть до файла с данными, относительно \"static/\".

        Returns
        -------
        str
            Путь до файла или None, если файл не найден.
        """
        result = finders.find(data_file_name)
        if result:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Файл с данными "static/{data_file_name}" найден'
                )
            )
            return result
        self.stdout.write(
            self.style.ERROR(
                f'Файл с данными "static/{data_file_name}" не найден'
            )
        )
        return None

    def check_installed_apps(self, app_name):
        """Проверяет зарегестрированно ли приложение.

        Parameters
        ----------
        app_name : str
            Название приложения.

        Returns
        -------
        bool
            True, если приложение зарегистрированно в settings.py.
        """
        if apps.is_installed(app_name):
            self.stdout.write(
                self.style.SUCCESS(f'Приложение "{app_name}" найдено')
            )
            return True

        self.stdout.write(
            self.style.ERROR(f'Приложение "{app_name}" не найдено')
        )
        return False

    def check_table_exist(self, table_name):
        """Проверяет существует ли таблица приложения в БД.

        Parameters
        ----------
        table_name : str
            Имя таблицы в БД.

        Returns
        -------
        bool
            True, если таблица существует в БД.
        """
        if table_name in connection.introspection.table_names():
            self.stdout.write(
                self.style.SUCCESS(f'Запись в таблицу "{table_name}":')
            )
            return True
        self.stdout.write(
            self.style.ERROR(
                (
                    f'Таблица "{table_name}" не найдена '
                    f'(необходимо выполнить миграции)'
                )
            )
        )
        return False

    def load_data(self, app_name, model_name, data_file_name, foreign_keys=[]):
        """Загружает данные из  CSV-файла.

        Parameters
        ----------
        app_name : str
            Название приложение.
        model_name : str
            Название модели в приложении.
        data_file_name : str
            Путь до файла, относительно \"static/\".
        foreign_keys : list, optional
            список полей ForeignKey, для добавления постфикса _id.
        """
        model = apps.get_model(app_name, model_name)
        table_name = model.objects.model._meta.db_table

        if self.check_table_exist(table_name):
            data_file_path = self.get_data_file_path(data_file_name)
            if data_file_path:
                with open(data_file_path, newline='') as csvfile:
                    csv_reader = csv.DictReader(f=csvfile)

                    csv_reader.fieldnames = [
                        name if name not in foreign_keys else f'{name}_id'
                        for name in csv_reader.fieldnames
                    ]
                    index = 0
                    index_all = 0
                    for row in csv_reader:
                        try:
                            index = index + 1
                            index_all = index_all + 1
                            model_object = model.objects.create(**row)
                            model_object.save()

                        except Exception as ex:
                            index = index - 1
                            self.stdout.write(
                                self.style.ERROR(
                                    f'Запись "{row}" не добавлена: {ex}'
                                )
                            )
                    self.stdout.write(
                        self.style.SUCCESS(
                            (
                                f'\nДобавлено {index} из записей '
                                f'из {index_all}\n\n'
                            )
                        )
                    )
                    return

        self.stdout.write('\n')
        self.stdout.write(
            self.style.ERROR(
                (
                    f'Ошибка при загрузке данных в таблицу "{table_name}" '
                    f'из файла "static/{data_file_name}"'
                )
            )
        )
        self.stdout.write('\n\n')

    def handle(self, *args, **kwargs):
        self.print_divider()
        if self.check_installed_apps('titles'):
            self.load_data('titles', 'CategoriesModel', 'data/category.csv')
            self.load_data('titles', 'GenresModel', 'data/genre.csv')
            self.load_data(
                'titles', 'TitlesModel', 'data/titles.csv', ['category']
            )
            # self.load_data('titles', 'CategoriesModel', 'data/genre_title.csv')
        if self.check_installed_apps('users'):
            self.load_data('users', 'User', 'data/users.csv')
        if self.check_installed_apps('comments'):
            self.load_data(
                'comments',
                'ReviewModel',
                'data/review.csv',
                ['title_id', 'author'],
            )
            self.load_data(
                'comments',
                'CommentModel',
                'data/comments.csv',
                ['review_id', 'author'],
            )
        self.print_divider()
