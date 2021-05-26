# Generated by Django 3.2.2 on 2021-05-26 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_auto_20210520_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='insurance_1_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_1_id', to='viewer.insurance'),
        ),
        migrations.AddField(
            model_name='contract',
            name='insurance_2_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_2_id', to='viewer.insurance'),
        ),
        migrations.AddField(
            model_name='contract',
            name='insurance_3_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_3_id', to='viewer.insurance'),
        ),
        migrations.AddField(
            model_name='contract',
            name='insurance_4_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_4_id', to='viewer.insurance'),
        ),
        migrations.AddField(
            model_name='contract',
            name='insurance_5_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_5_id', to='viewer.insurance'),
        ),
    ]
