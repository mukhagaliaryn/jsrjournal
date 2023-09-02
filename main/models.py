from django.db import models


class Article(models.Model):
    CATEGORY_CHOICE = (
        ('Педагогические науки', 'Педагогические науки'),
        ('Искусство и гуманитарные науки', 'Искусство и гуманитарные науки'),
        ('Социальные науки, журналистика и информация', 'Социальные науки, журналистика и информация'),
        ('Бизнес, управление и право', 'Бизнес, управление и право'),
        ('Естественные науки, математика и статистика', 'Естественные науки, математика и статистика'),
        ('Информационно-коммуникационные технологии', 'Информационно-коммуникационные технологии'),
        ('Инженерные, обрабатывающие и строительные отрасли', 'Инженерные, обрабатывающие и строительные отрасли'),
        ('Сельское хозяйство и биоресурсы', 'Сельское хозяйство и биоресурсы'),
        ('Ветеринария', 'Ветеринария'),
        ('Здравоохранение', 'Здравоохранение'),
        ('Услуги', 'Услуги'),
        ('Национальная безопасность и военное дело', 'Национальная безопасность и военное дело'),
    )

    ITEM_CHOICE = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )

    full_name = models.CharField(verbose_name='ФИО контактного лица', max_length=255)
    email = models.EmailField(verbose_name='Email контактного лица')
    phone = models.CharField(verbose_name='Телефон контактного лица', max_length=255)
    category = models.CharField(verbose_name='Научное направление', max_length=255,
                                choices=CATEGORY_CHOICE, default=CATEGORY_CHOICE[0][1])
    item = models.CharField(verbose_name='Количество авторов', max_length=20,
                            choices=ITEM_CHOICE, default=ITEM_CHOICE[0][1])
    file = models.FileField(verbose_name='Прикрепить статьи', upload_to='main/articles/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# Publisher
class Publisher(models.Model):
    CATEGORY_CHOICE = (
        ('1', 'Педагогические науки'),
        ('2', 'Искусство и гуманитарные науки'),
        ('3', 'Социальные науки, журналистика и информация'),
        ('4', 'Бизнес, управление и право'),
        ('5', 'Естественные науки, математика и статистика'),
        ('6', 'Информационно-коммуникационные технологии'),
        ('7', 'Инженерные, обрабатывающие и строительные отрасли'),
        ('8', 'Сельское хозяйство и биоресурсы'),
        ('9', 'Ветеринария'),
        ('10', 'Здравоохранение'),
        ('11', 'Услуги'),
        ('12', 'Национальная безопасность и военное дело'),
    )

    title = models.CharField(verbose_name='Название статьи', max_length=255)
    poster = models.ImageField(verbose_name='Обложка', upload_to='main/poster/', blank=True, null=True)
    category = models.CharField(verbose_name='Научное направление', max_length=255,
                                choices=CATEGORY_CHOICE, default=CATEGORY_CHOICE[0][1])
    file = models.FileField(verbose_name='Прикрепить статьи', upload_to='main/publishers/')
    date_created = models.DateField(verbose_name='Публикация выпуска')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Review(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=255)
    staff = models.CharField(verbose_name='Должность', max_length=255)
    body = models.TextField(verbose_name='Отзыв', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-date_created', )
