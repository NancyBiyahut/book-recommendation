# Generated by Django 4.1.4 on 2023-10-25 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_bookmain_alter_book_isbn_alter_book_bookrating_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Book",
        ),
    ]