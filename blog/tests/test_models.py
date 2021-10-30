from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Publicaion


class PublicacionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        autor = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        Publicaion.objects.create(autor=autor, titulo='Titulo publicacion', texto='Texto de prueba de la publicación')
        pass

    def test_titulo_label(self):
        publicacion = Publicaion.objects.get(id=1)
        field_label = Publicaion._meta.get_field('texto').verbose_name
        self.assertEquals(field_label, 'texto')

    def test_titulo_max_length(self):
        publicacion = Publicaion.objects.get(id=1)
        max_length = Publicaion._meta.get_field('titulo').max_length
        self.assertEquals(max_length, 100)

    def test_fecha_creacion_label(self):
        publicacion = Publicaion.objects.get(id=1)
        field_label = Publicaion._meta.get_field(
            'fecha_creacion').verbose_name
        self.assertEquals(field_label, 'Creado')
