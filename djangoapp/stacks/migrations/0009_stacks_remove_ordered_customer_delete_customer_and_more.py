# Generated by Django 4.2.6 on 2023-10-24 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0008_customer_ordered_remove_stack_stack_delete_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stack', models.CharField(max_length=200)),
                ('choice_stacks', models.CharField(choices=[('STACK', 'STACK'), ('PYTHON', 'PYTHON'), ('JAVA', 'JAVA')], default='STACK', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='ordered',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Ordered',
        ),
    ]