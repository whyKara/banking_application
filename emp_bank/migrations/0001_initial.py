# Generated by Django 4.1.1 on 2022-10-06 19:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("acc_no", models.CharField(max_length=100)),
                ("cc_type", models.TextField()),
                ("acc_balance", models.FloatField()),
                (
                    "acc_opendate",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cards",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("c_id", models.CharField(max_length=20)),
                ("c_type", models.BinaryField()),
                ("c_pin", models.IntegerField()),
                ("c_limit", models.IntegerField()),
                ("c_doc", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("u_id", models.AutoField(primary_key=True, serialize=False)),
                ("u_fname", models.CharField(max_length=20)),
                ("u_lname", models.CharField(max_length=20)),
                ("u_add_l1", models.TextField()),
                ("u_add_l2", models.TextField()),
                ("u_email", models.EmailField(max_length=254)),
                ("u_password", models.CharField(max_length=20)),
                ("u_contact", models.IntegerField()),
                ("u_pancd", models.CharField(max_length=20)),
                ("u_doc", models.DateField()),
                ("u_isemp", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="user_acc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField()),
                (
                    "a_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="emp_bank.account",
                    ),
                ),
                (
                    "u_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp_bank.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tranaction",
            fields=[
                ("t_id", models.AutoField(primary_key=True, serialize=False)),
                ("t_ammount", models.FloatField()),
                ("t_doc", models.DateTimeField(auto_now_add=True)),
                ("t_status", models.CharField(max_length=20)),
                ("t_revert_req", models.BooleanField()),
                (
                    "t_facc",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_account",
                        to="emp_bank.account",
                    ),
                ),
                (
                    "t_tacc",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_account",
                        to="emp_bank.account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="acc_cards",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField()),
                (
                    "a_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="emp_bank.account",
                    ),
                ),
                (
                    "c_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp_bank.cards"
                    ),
                ),
            ],
        ),
    ]
