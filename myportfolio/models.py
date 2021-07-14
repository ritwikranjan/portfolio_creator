from django.db import models

# Create your models here.
skill_proficiency_levels = [('Beginner', 'Beginner'),
                            ('Familiar', 'Familiar'),
                            ('Intermediate', 'Intermediate'),
                            ('Proficient', 'Proficient'),
                            ('Expert', 'Expert')]


class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField()
    proficiency = models.CharField(max_length=100, choices=skill_proficiency_levels)

    def save(self, *args, **kwargs):
        if self.level > 0:
            self.proficiency = 'Beginner'
        if self.level > 20:
            self.proficiency = 'Familiar'
        if self.level > 40:
            self.proficiency = 'Intermediate'
        if self.level > 60:
            self.proficiency = 'Proficient'
        if self.level > 80:
            self.proficiency = 'Expert'
        super(Skill, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PersonalDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    fb = models.CharField(max_length=100, null=True)
    insta = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    dob = models.DateField()
    profile_image = models.ImageField(null=True)
    cover_image = models.ImageField(null=True)
    address = models.TextField(max_length=200)
    resume = models.FileField(null=True)
    maps = models.TextField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            return super(PersonalDetail, self).save(*args, **kwargs)
        if self.objects.count() == 0:
            return super(PersonalDetail, self).save(*args, **kwargs)
        else:
            pass


class WorkExperience(models.Model):
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    description = models.TextField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.designation} at {self.company}'


class Education(models.Model):
    title = models.CharField(max_length=100)
    alma_mater = models.CharField(max_length=100)
    start_year = models.SmallIntegerField()
    end_year = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} from {self.alma_mater}'


class Project(models.Model):
    url = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=100)
    description = models.TextField()
    left = models.BooleanField(default=False)
    image = models.ImageField()

    def __str__(self):
        return f'{self.title}'


class Reference(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.name}'



