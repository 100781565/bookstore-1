# Generated by Django 2.0.2 on 2018-03-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0002_payment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': '支付方式', 'verbose_name_plural': '支付方式'},
        ),
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(choices=[('支付宝', '支付宝'), ('微信', '微信')], max_length=10, verbose_name='名称'),
        ),
    ]
