from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Language(models.Model):
    """ Save language details """
    name = models.CharField(max_length=100)
    link = models.URLField()
    logo = models.URLField()

    def __str__(self):
        return self.name


class Project(models.Model):
    """ Save project details """
    title = models.CharField(max_length=100)
    live_link = models.URLField()
    code_link = models.URLField()
    preview_img = models.URLField()
    languages = models.ManyToManyField(Language, through='ProjectLanguage', related_name="projects")

    def __str__(self):
        return self.title


class ProjectLanguage(models.Model):
    """ Connect Project model to Language model """
    class Meta:
        """
        Ensure each email can only be added to each list once.
        """
        constraints = [models.UniqueConstraint(fields=["project", "language"], name='unique_pairing')]

    project = models.ForeignKey(Project, related_name="project_languages", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name="project_languages", on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + " - " + self.language.name
