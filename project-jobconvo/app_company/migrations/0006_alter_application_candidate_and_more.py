# Generated by Django 4.2.3 on 2023-07-13 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_candidate', '0002_experience_user_remove_experience_name_and_more'),
        ('app_company', '0005_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_candidate.candidate', verbose_name='Candidato'),
        ),
        migrations.AlterField(
            model_name='application',
            name='minimum_schooling_candidate',
            field=models.CharField(choices=[('Ensino Fundamental', 'Ensino Fundamental'), ('Ensino Médio', 'Ensino Médio'), ('Tecnólogo', 'Tecnólogo'), ('Ensino Superior', 'Ensino Superior'), ('Pós / MBA / Mestrado', 'Pós / MBA / Mestrado'), ('Doutorado', 'Doutorado')], max_length=45, null=True, verbose_name='Escolaridade'),
        ),
        migrations.AlterField(
            model_name='application',
            name='salary_range_candidate',
            field=models.CharField(choices=[('Até R$ 1.000,00', 'Até R$ 1.000,00'), ('De R$ 1.000,01 a R$ 2.000,00', 'De R$ 1.000,01 a R$ 2.000,00'), ('De R$ 2.000,01 a R$ 3.000,00', 'De R$ 2.000,01 a R$ 3.000,00'), ('Acima de R$ 3.000,00', 'Acima de R$ 3.000,00')], max_length=45, verbose_name='Faixa salarial'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='minimum_schooling',
            field=models.CharField(choices=[('Ensino Fundamental', 'Ensino Fundamental'), ('Ensino Médio', 'Ensino Médio'), ('Tecnólogo', 'Tecnólogo'), ('Ensino Superior', 'Ensino Superior'), ('Pós / MBA / Mestrado', 'Pós / MBA / Mestrado'), ('Doutorado', 'Doutorado')], max_length=45, null=True, verbose_name='Escolaridade'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary_range',
            field=models.CharField(choices=[('Até R$ 1.000,00', 'Até R$ 1.000,00'), ('De R$ 1.000,01 a R$ 2.000,00', 'De R$ 1.000,01 a R$ 2.000,00'), ('De R$ 2.000,01 a R$ 3.000,00', 'De R$ 2.000,01 a R$ 3.000,00'), ('Acima de R$ 3.000,00', 'Acima de R$ 3.000,00')], max_length=45, verbose_name='Faixa salarial'),
        ),
    ]
