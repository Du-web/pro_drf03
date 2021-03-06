from django.db import models

# Create your models here.


class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Student(BaseModel):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'other')
    )

    username = models.CharField(max_length=40)
    age = models.SmallIntegerField()
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    team_id = models.ForeignKey(to='Team', on_delete=models.CASCADE, db_constraint=False, related_name='students')

    class Meta:
        db_table = 'db_student'
        verbose_name = '学生表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Team(BaseModel):
    classname = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)

    class Meta:
        db_table = 'db_team'
        verbose_name = '班级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.classname
