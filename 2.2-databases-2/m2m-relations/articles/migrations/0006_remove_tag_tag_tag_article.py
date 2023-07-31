
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options_tag_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tag', through='articles.Scope', to='articles.article'),
        ),
    ]