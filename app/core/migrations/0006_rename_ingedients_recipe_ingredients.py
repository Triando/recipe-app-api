# Generated by Django 3.2.18 on 2023-03-19 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_ingredient_recipe_ingedients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingedients',
            new_name='ingredients',
        ),
    ]