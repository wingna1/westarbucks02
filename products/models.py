from django.db import models

# Create your models here.
class Menu(models.Model):
    # id를 categories가 참조 - 역참조
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    # id를 drinks가 참조 - 역참조
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE) # menu의 id를 참조해옴 - 정참조
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE) # 카테고리에서 참조해옴 - 정참조
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=2000)

    class Meta:
        db_table = 'drinks'

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'sizes'

class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE, null=True) # drinks에서 참조해옴 - 정참조
    size = models.ForeignKey("Size", on_delete=models.CASCADE, null=True) # sizes에서 참조해옴 - 정참조

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE) # drinks에서 참조해옴 - 정참조

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    drink = models.ManyToManyField(Drink, through="Allergy_drink") # , related_name="allergies"

    class Meta:
        db_table = 'allergies'


class Allergy_drink(models.Model):
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE) # allergy에서 참조해옴 - 정참조 - 다대다
    drink = models.ForeignKey("Drink", on_delete=models.CASCADE) # drinks에서 참조해옴 - 정참조 - 다대다

    class Meta:
        db_table = 'allergy_drink'


