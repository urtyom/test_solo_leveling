from django.db import models
from django.utils import timezone


class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    points = models.PositiveIntegerField(default=0)  # Баллы за вход
    first_login = models.DateTimeField(null=True, blank=True)  # Отслеживание первого входа
    last_login = models.DateTimeField(null=True, blank=True)  # Последний вход

    def add_points(self, points):
        """Начисление баллов за вход"""
        self.points += points
        if self.first_login is None:
            self.first_login = timezone.now()
        self.last_login = timezone.now()
        self.save()

    def __str__(self):
        return self.username


class Boost(models.Model):
    BOOST_TYPES = (
        ('speed', 'Speed Boost'),
        ('strength', 'Strength Boost'),
        ('health', 'Health Boost'),
    )

    name = models.CharField(max_length=100)
    boost_type = models.CharField(max_length=10, choices=BOOST_TYPES)
    duration = models.PositiveIntegerField(help_text="Длительность буста в секундах")

    def __str__(self):
        return f"{self.name} ({self.get_boost_type_display()})"


class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    manually_assigned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.username} - {self.boost.name}"


class Player(models.Model):
    player_id = models.CharField(max_length=100)


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField()


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
