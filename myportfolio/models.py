from djongo import models
from django.contrib.auth.models import User


class PersonalDetail(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=15)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    fb = models.URLField(null=True)
    insta = models.URLField(null=True)
    twitter = models.URLField(null=True)
    dob = models.DateField()
    profile_image = models.ImageField()
    cover_image = models.ImageField()
    address = models.TextField(max_length=200)
    resume = models.FileField()
    maps = models.TextField(help_text="Enter Iframe of Google Maps")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.email = self.user.email
        self.slug = self.user.username
        super(PersonalDetail, self).save(*args, **kwargs)


class Skill(models.Model):
    user = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    level = models.PositiveSmallIntegerField()
    proficiency = models.CharField(max_length=100)

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


class WorkExperience(models.Model):
    user = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.designation} at {self.company}'


class Education(models.Model):
    user = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    alma_mater = models.CharField(max_length=100)
    start_year = models.SmallIntegerField()
    end_year = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} from {self.alma_mater}'


class Project(models.Model):
    user = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    url = models.CharField(max_length=250)
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=100)
    description = models.TextField()
    left = models.BooleanField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.title}'


class Reference(models.Model):
    user = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.name}'



