from django.db import models
from ckeditor.fields import RichTextField

class Efemerides(models.Model):

    colors = [
        ("warning", "Amarillo"),
        ("primary", "Azul"),
        ("info", "Cian"),
        ("fuchsia", "Fucsia"),
        ("orange", "Naranja"),
        ("dark", "Negro"),
        ("danger", "Rojo"),
        ("success", "Verde")
    ]

    titulo =  models.CharField("Título", max_length=50)
    texto = RichTextField("Texto")
    foto = models.ImageField("Foto de la Tematica", upload_to="efemerides_photo", default="")
    color = models.CharField("Color", max_length=50, choices=colors)
    fecha_festividad = models.DateField("Día de festividad", unique=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        try:
            this = Efemerides.objects.get(id=self.id)
            if this.foto != self.foto:
                this.foto.delete()
        except:
            pass
        super(Efemerides, self).save(*args, **kwargs)

    class Meta:

        verbose_name = "Efemérides"
        verbose_name_plural = "Efemérides"