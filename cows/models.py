from django.db import models


class Cow(models.Model):
    crotal_number = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=(('M', "Macho"), ("H", "Hembra")))
    raze = models.CharField(max_length=50)
    birth_date = models.DateField()
    explotation_code = models.CharField(max_length=50)
    date_register_as_mother_or_father = models.DateField(null=True, blank=True)
    date_of_send_to_feeding = models.DateField(null=True, blank=True)
    # Cria en el campo son aquellos que no se han enviado a cebadero ni son sementales ni madres

    @property
    def is_father(self):
        return self.sex == "M" and self.date_register_as_mother_or_father is not None

    @property
    def is_mother(self):
        return self.sex == "H" and self.date_register_as_mother_or_father is not None

    @property
    def is_feeding(self):
        return self.date_of_send_to_feeding is not None

    def __str__(self):
        return "{} ({})".format(self.crotal_number, self.name)


class CowDrop(models.Model):
    cow = models.OneToOneField(Cow, primary_key=True)
    date = models.DateField()


class Sell(CowDrop):
    explotation_code = models.CharField(max_length=50)
    sell_price = models.DecimalField(max_digits=20, decimal_places=2)


class InExplotationDeath(CowDrop):
    reason = models.TextField()


class SentToSlaughterhouse(CowDrop):
    weight = models.DecimalField(max_digits=20, decimal_places=3)
    sell_price = models.DecimalField(max_digits=20, decimal_places=2)


class Expenses(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.price * self.quantity


class Earnings(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()

    @property
    def total(self):
        return self.price * self.quantity
