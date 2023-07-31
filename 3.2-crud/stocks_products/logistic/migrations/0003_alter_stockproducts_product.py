from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_stockproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='logistic.product'),
        ),
    ]