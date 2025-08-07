from django.db import models

class Admin(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.fullname


class Mijoz(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.fullname


class Driver(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname


class Shartnoma(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='shartnomalar')
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE, related_name='shartnomalar')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='shartnomalar')
    start_date = models.DateField()
    end_date = models.DateField()
    narx = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Shartnoma {self.id} - {self.mijoz.fullname} ↔ {self.driver.fullname}"


class Static(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='statistikalar')
    total_orders = models.IntegerField(default=0)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Statistika - {self.driver.fullname}"


class Cament(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='izohlar')
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE, related_name='izohlar')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Izoh - {self.mijoz.fullname} ➝ {self.driver.fullname}"


class Tolov(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='tolovlar')
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE, related_name='tolovlar')
    shartnoma = models.ForeignKey(Shartnoma, on_delete=models.CASCADE, related_name='tolovlar')
    summa = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, default='naqt')  # Faqat 'naqt'

    def __str__(self):
        return f"{self.driver.fullname} ← {self.summa} so'm"
