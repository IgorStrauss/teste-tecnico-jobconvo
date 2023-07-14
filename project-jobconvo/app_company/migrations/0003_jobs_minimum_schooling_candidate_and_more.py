# Generated by Django 4.2.3 on 2023-07-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_company', '0002_jobs_candidate_alter_jobs_salary_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='minimum_schooling_candidate',
            field=models.CharField(choices=[(1, 'Ensino Fundamental'), (2, 'Ensino Médio'), (3, 'Tecnólogo'), (4, 'Ensino Superior'), (5, 'Pós / MBA / Mestrado'), (6, 'Doutorado')], max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='salary_range_candidate',
            field=models.CharField(choices=[(1, 'Até R$ 1.000,00'), (2, 'De R$ 1.000,01 a R$ 2.000,00'), (3, 'De R$ 2.000,01 a R$ 3.000,00'), (4, 'Acima de R$ 3.000,00')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='minimum_schooling',
            field=models.CharField(choices=[(1, 'Ensino Fundamental'), (2, 'Ensino Médio'), (3, 'Tecnólogo'), (4, 'Ensino Superior'), (5, 'Pós / MBA / Mestrado'), (6, 'Doutorado')], max_length=45, null=True, verbose_name='Escolaridade'),
        ),
    ]
