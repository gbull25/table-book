# Generated by Django 4.2.2 on 2023-06-21 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0003_alter_branchadress_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchadress',
            name='branch_id',
            field=models.OneToOneField(db_column='branch_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user_service.restaurantbranch'),
        ),
        migrations.AlterField(
            model_name='restaurantbranch',
            name='branch_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='branchadress',
            table='branch_adress',
        ),
    ]