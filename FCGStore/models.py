from django.db import models


# Create your models here.
class Game(models.Model):
    Title = models.CharField(max_length=30)
    Version = models.CharField(max_length=11)
    Heading = models.CharField(max_length=100)
    ShortDescription = models.TextField(max_length=300)
    MeanDescription = models.TextField(max_length=500)
    LongDescription = models.TextField(max_length=1000)
    UserName1 = models.CharField(max_length=100)
    UserName2 = models.CharField(max_length=100, null=True)
    UserName3 = models.CharField(max_length=100, null=True)
    UserExp1 = models.CharField(max_length=255)
    UserExp2 = models.CharField(max_length=255, null=True)
    UserExp3 = models.CharField(max_length=255, null=True)
    ExtraTextField1 = models.TextField(max_length=500, null=True)
    ExtraTextField2 = models.TextField(max_length=500, null=True)
    ExtraTextField3 = models.TextField(max_length=500, null=True)
    Link1 = models.CharField(max_length=255, null=True)
    Link2 = models.CharField(max_length=255, null=True)
    Link3 = models.CharField(max_length=255, null=True)
    PriceRating = models.FloatField()
    GraphicsRating = models.FloatField()
    LevelsRating = models.FloatField()
    DifficultyRating = models.FloatField()
    Rating = models.FloatField()
    ExtraIntField1 = models.IntegerField()
    ExtraIntField2 = models.IntegerField()
    ExtraIntField3 = models.IntegerField()
    IsGameAvailable = models.BooleanField()
    DownloadButtonState = models.BooleanField()
    ExtraBoolField1 = models.BooleanField()
    ExtraBoolField2 = models.BooleanField()
    ExtraBoolField3 = models.BooleanField()
    Image1 = models.FileField(upload_to='media/Images/', max_length=255)
    Image2 = models.FileField(upload_to='media/Images/', max_length=255)
    Image3 = models.FileField(upload_to='media/Images/', max_length=255)
    Image4 = models.FileField(upload_to='media/Images', max_length=255)
    Image5 = models.FileField(upload_to='media/Images',
                              max_length=255,
                              null=True,
                              default=None)
    Image6 = models.FileField(upload_to='media/Images',
                              max_length=255,
                              null=True,
                              default=None)
    Image7 = models.FileField(upload_to='media/Images',
                              max_length=255,
                              null=True,
                              default=None)
    Video1 = models.FileField(upload_to='media/Videos',
                              max_length=255,
                              null=True,
                              default=None)
    Video2 = models.FileField(upload_to='media/Videos',
                              max_length=255,
                              null=True,
                              default=None)
    GameFile = models.FileField(upload_to='media/Games',
                                max_length=255,
                                null=True,
                                default=None)
    Dependencies = models.FileField(upload_to='media/Games',
                                    max_length=255,
                                    null=True,
                                    default=None)
    GameName = models.SlugField(default="", null=False)