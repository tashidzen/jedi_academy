from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class JediManager(models.Manager):
    # добавляет поле количество падаванов к джедаю
    def get_queryset(self):
        return super(JediManager, self).get_queryset().annotate(padawans_cnt=models.Count('candidate'))

    # возвращает джедаев, у которых меньше трех падаванов
    def can_teach(self):
        return self.get_queryset().filter(padawans_cnt__lte=3)

    # возвращает джедаев, у которых больше одного падавана
    def more_than_one(self):
        return self.get_queryset().filter(padawans_cnt__gt=1)

# #этот класс заведён для того, чтобы выходил список Джедаев
class Djeday(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class Jedi(models.Model):
    with_padawans = JediManager()
    name = models.ForeignKey(Djeday, null=True, on_delete=models.DO_NOTHING)
    planet = models.ForeignKey(Planet, on_delete=models.DO_NOTHING)
    #objects = models.Manager()


class Question(models.Model):
    qu = models.CharField(null=True, max_length=1000)
    ans = models.BooleanField(null=True)

class Candidate(models.Model):
    name = models.CharField(null=True, max_length=100)
    planet = models.ForeignKey(Planet, null=True, on_delete=models.DO_NOTHING)
    age = models.IntegerField(null=True)
    email = models.CharField(null=True, max_length=100)
    jedi = models.ForeignKey(Jedi, null=True, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, null=True, on_delete=models.DO_NOTHING)
    objects = models.Manager()
    # def __str__(self):
    #     return "{} from {}".format(self.name, self.planet)



class Test_task(models.Model):
    order = models.OneToOneField(Planet, on_delete=models.DO_NOTHING)
    question = models.ManyToManyField(Question)
    def __str__(self):
        return "{} order challenge".format(self.order)

# class Answer(models.Model):
#     candidate = models.ForeignKey(Candidate, on_delete=models.DO_NOTHING)
#     question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
#     answer = models.BooleanField()
#
#     class Meta:
#         unique_together = (('candidate', 'question'),)





