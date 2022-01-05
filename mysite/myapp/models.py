from datetime import datetime
from io import DEFAULT_BUFFER_SIZE
from django import db
from django.db import models
from django.db.models.base import Model
from numpy import mod
from pandas.core.algorithms import mode

# add your models here

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Team(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    tempo = models.FloatField(default=0)
    pointsPerPossession = models.FloatField(default=0)
    oppPointsPerPossession = models.FloatField(default=0)
    efficiencyMargin = models.FloatField(default=0)
    eFGpct = models.FloatField(default=0)
    oppEFGpct = models.FloatField(default=0)
    turnoverRate = models.FloatField(default=0)
    oppTurnoverRate = models.FloatField(default=0)
    oRebpct = models.FloatField(default=0)
    oppORebpct = models.FloatField(default=0)
    ftaPerFga = models.FloatField(default=0)
    oppFtaPerFga = models.FloatField(default=0)
    stealpct = models.FloatField(default=0)
    oppStealpct = models.FloatField(default=0)
    assistRate = models.FloatField(default=0)
    oppAssistRate = models.FloatField(default=0)
    adjEffMargin = models.FloatField(default=0)
    adjOffEff = models.FloatField(default=0)
    adjDefEff = models.FloatField(default=0)
    adjOffEFGpct = models.FloatField(default=0)
    adjDefEFGpct = models.FloatField(default=0)
    adjTORate = models.FloatField(default=0)
    adjDefTORate = models.FloatField(default=0)
    adjORebpct = models.FloatField(default=0)
    adjDefORebpct = models.FloatField(default=0)
    adjFtaPerFga = models.FloatField(default=0)
    adjDefFtaPerFga = models.FloatField(default=0)

# class GameData(models.Model):
#     homeTeam = models.CharField(max_length=100)
#     awayTeam = models.CharField(max_length=100)

class D1Averages(models.Model):
    offensiveEfficiency = models.FloatField(default=0)
    defensiveEfficiency = models.FloatField(default=0)
    averageEfficiency = models.FloatField(default=0)
    tempo = models.FloatField(default=0)
    eFGpct = models.FloatField(default=0)
    oppEFGpct = models.FloatField(default=0)
    turnoverRate = models.FloatField(default=0)
    oppTurnoverRate = models.FloatField(default=0)
    oRebpct = models.FloatField(default=0)
    oppORebpct = models.FloatField(default=0)
    ftaPerFga = models.FloatField(default=0)
    oppFtaPerFga = models.FloatField(default=0)
    

class AdjustedStats(models.Model):
    teamName = models.CharField(max_length=100)
    teamAbbreviation = models.CharField(max_length=100)
    adjOffEff = models.FloatField(default=0)
    adjDefEff = models.FloatField(default=0)
    adjEffMargin = models.FloatField(default=0)
    adjTempo = models.FloatField(default=0)
    adjOffEFGpct = models.FloatField(default=0)
    adjDefEFGpct = models.FloatField(default=0)
    adjTORate = models.FloatField(default=0)
    adjDefTORate = models.FloatField(default=0)
    adjORebpct = models.FloatField(default=0)
    adjDefORebpct = models.FloatField(default=0)
    adjFtaPerFga = models.FloatField(default=0)
    adjDefFtaPerFga = models.FloatField(default=0)


class SavedDataframe(models.Model):
    gameIndex = models.CharField(max_length=100)
    winning_abbr = models.CharField(max_length=100)
    losing_abbr = models.CharField(max_length=100)
    home_offensive_rating = models.FloatField(default=0)
    home_defensive_rating = models.FloatField(default=0)
    away_offensive_rating = models.FloatField(default=0)
    away_defensive_rating = models.FloatField(default=0)
    tempo = models.FloatField(default=0)
    home_effective_field_goal_percentage = models.FloatField(default=0)
    away_effective_field_goal_percentage = models.FloatField(default=0)
    home_turnover_percentage = models.FloatField(default=0)
    away_turnover_percentage = models.FloatField(default=0)
    home_offensive_rebound_percentage = models.FloatField(default=0)
    away_offensive_rebound_percentage = models.FloatField(default=0)
    home_free_throw_attempt_rate = models.FloatField(default=0)
    away_free_throw_attempt_rate = models.FloatField(default=0)

class TeamSchedule(models.Model):
    teamName = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    location = models.CharField(max_length=25)
    date = models.CharField(max_length=100)
    scorePrediction = models.IntegerField(default=0)
    oppScorePrediction = models.IntegerField(default=0)
    tempoPrediction = models.IntegerField(default=0)
    wOrL = models.CharField(max_length=20, default="")

class CompletedGame(models.Model):
    teamName = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    location = models.CharField(max_length=25)
    date = models.CharField(max_length=100)
    tempo = models.IntegerField(default=0)
    teamScore = models.IntegerField(default=0)
    opponentScore = models.IntegerField(default=0)
    seasonWins = models.IntegerField(default=0)
    seasonLosses = models.IntegerField(default=0)
    wOrL = models.CharField(max_length=20, default="")