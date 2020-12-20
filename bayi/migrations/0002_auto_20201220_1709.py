# Generated by Django 3.1.3 on 2020-12-20 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bayi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bakim',
            options={'verbose_name': 'Bakım', 'verbose_name_plural': 'Bakımlar'},
        ),
        migrations.AlterModelOptions(
            name='bayiler',
            options={'verbose_name': 'Bayi', 'verbose_name_plural': 'Bayiler'},
        ),
        migrations.AlterModelOptions(
            name='bayiler_odeme',
            options={'verbose_name': 'Bayi Ödeme', 'verbose_name_plural': 'Bayi Ödemeleri'},
        ),
        migrations.AlterModelOptions(
            name='bayiler_siparis',
            options={'verbose_name': 'Bayi Sipariş', 'verbose_name_plural': 'Bayi Siparişleri'},
        ),
        migrations.AlterModelOptions(
            name='ebat',
            options={'verbose_name': 'Ebat', 'verbose_name_plural': 'Ebatlar'},
        ),
        migrations.AlterModelOptions(
            name='hammadde',
            options={'verbose_name': 'Hammadde', 'verbose_name_plural': 'Hammaddeler'},
        ),
        migrations.AlterModelOptions(
            name='recete',
            options={'verbose_name': 'Reçete', 'verbose_name_plural': 'Reçeteler'},
        ),
        migrations.AlterModelOptions(
            name='urunler',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AddField(
            model_name='bayiler_siparis',
            name='urunler',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bayi.urunler'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recete',
            name='kullanim',
            field=models.TextField(),
        ),
    ]