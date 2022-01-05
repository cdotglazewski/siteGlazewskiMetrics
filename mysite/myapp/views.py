from types import NoneType
from django import db
from django.http.response import JsonResponse
from django.shortcuts import render
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn import linear_model
from sportsipy.ncaab.teams import Teams
from sportsipy.ncaab.schedule import Schedule
from sportsipy.ncaab.boxscore import Boxscores
from django.conf import settings

from datetime import date, datetime, timedelta
from sqlalchemy import create_engine

import sys

from django.http import HttpResponse

from .models import AdjustedStats, Book, CompletedGame, D1Averages, SavedDataframe, Team, TeamSchedule

def index(request):
    allTeamsData = Team.objects.order_by('-adjEffMargin')
    adjStatistics = AdjustedStats.objects.all()
    context = {'allTeamsData': allTeamsData, 'adjStats': adjStatistics}
    return render(request, 'index.html', context)

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book': book})

def team_wins(request):
    teams = Teams()
    winTotal = []
    for team in teams:
        winTotal.append(team.wins)
    return JsonResponse(winTotal, safe=False)

def load_teams(request):
    # initTeams()
    # i = 0
    # while (i < 3):
    #     adjustStats()
    #     i += 1
    # getSchedules()

    

#### IMPORTANT: the code from this line to 359 can be uncommented and run when the entire db/dataframe needs to be refreshed

    # allTeamObjects = Teams()
    # allTeamNames = []
    # for team in allTeamObjects:
    #     allTeamNames.append(team.name)

#     # creates dataframe of all game data for the entire year
#     gamesDataFrame = pd.DataFrame()
#     for team in allTeamObjects:
#         teamSchedule = Schedule(team.abbreviation)
#         for game in teamSchedule:
#             if ((game.boxscore_index != None) and (game.opponent_name in allTeamNames) and (game.boxscore_index not in gamesDataFrame.index)):
#                 gamesDataFrame = gamesDataFrame.append(game.dataframe_extended)
#                 print(gamesDataFrame)

# # Purdue example for testing
#     # for game in Schedule('PURDUE'):
#     #     if ((game.boxscore_index != None) and (game.opponent_name in allTeamNames) and (game.boxscore_index not in gamesDataFrame)):
#     #         gamesDataFrame = gamesDataFrame.append(game.dataframe_extended)
#     #         print(gamesDataFrame)

#     # print(gamesDataFrame)

#     gamesDataFrame.drop_duplicates()


#     dataForRegression = pd.DataFrame()
#     dataForRegression = gamesDataFrame[["date", "pace", "winning_abbr", "losing_abbr", "home_offensive_rating", "home_defensive_rating", "away_offensive_rating", "away_defensive_rating", "home_effective_field_goal_percentage", "away_effective_field_goal_percentage", "home_turnover_percentage", "away_turnover_percentage", "home_offensive_rebound_percentage", "away_offensive_rebound_percentage", "home_free_throw_attempt_rate", "away_free_throw_attempt_rate"]]

#     print(dataForRegression)

#     for row in dataForRegression.itertuples():
#         instance = SavedDataframe(
#             gameIndex = row.winning_abbr + "-" + row.losing_abbr + "-" + row.date,
#             winning_abbr = row.winning_abbr,
#             losing_abbr = row.losing_abbr,
#             home_offensive_rating = row.home_offensive_rating,
#             home_defensive_rating = row.home_defensive_rating,
#             away_offensive_rating = row.away_offensive_rating,
#             away_defensive_rating = row.away_defensive_rating,
#             tempo = row.pace,
#             home_effective_field_goal_percentage = row.home_effective_field_goal_percentage,
#             away_effective_field_goal_percentage = row.away_effective_field_goal_percentage,
#             home_turnover_percentage = row.home_turnover_percentage,
#             away_turnover_percentage = row.away_turnover_percentage,
#             home_offensive_rebound_percentage = row.home_offensive_rebound_percentage,
#             away_offensive_rebound_percentage = row.away_offensive_rebound_percentage,
#             home_free_throw_attempt_rate = row.home_free_throw_attempt_rate,
#             away_free_throw_attempt_rate = row.away_free_throw_attempt_rate
#         )
#         instance.save()

    # dbToDf = SavedDataframe.objects.all()
    # q = dbToDf.values().all()
    # df = pd.DataFrame.from_records(q)
    # print(df)

    # # statsToUse = pd.DataFrame()
    # # statsToUse = ({
    # #     "statName": []
    # # })

    # teamGames = pd.DataFrame()
    # teamGames = df

    # for team in allTeamObjects:
    #     for game in teamGames.itertuples():
    #         if (team.abbreviation == game.winning_abbr):
    #             if (game.home_offensive_rating > game.away_offensive_rating):
    #                 # then our team is home team and they won
    #             if (game.home_offensive_rating < game.away_offensive_rating):
    #                 # then our team is the away team and they won
    #         if (team.abbreviation == game.losing_abbr):
    #             if ()

    # game_stats = teamGames[['winning_abbr', 'losing_abbr', 'home_offensive_rating']]

    # dummyVars = pd.get_dummies(game_stats[['winning_abbr', 'losing_abbr']])


    # reg = linear_model.Ridge(alpha=1, fit_intercept=True)
    # reg_results_collection = pd.DataFrame(columns= ['stat_name', 'coef_name', 'ridge_reg_coef', 'ridge_reg_value'])

    # reg.fit(
    #     X = dummyVars,
    #     y = game_stats['home_offensive_rating']
    # )

    # regResults = pd.DataFrame({
    #     'stat_name': game_stats['home_offensive_rating'],
    #     # Coef name, which contains both season and tm_code
    #     'coef_name': dummyVars.columns.values,
    #     # Coef that results from ridge regression
    #     'ridge_reg_coef': reg.coef_
    # })

    # print(regResults)

    # regResults['ridge_reg_value'] = (regResults['ridge_reg_coef'] + reg.intercept_)

    # reg_results_collection = pd.concat([
    #     reg_results_collection,
    #     regResults
    # ],
    #     ignore_index = True
    # )
  
    # print(reg_results_collection)


    # user = settings.DATABASES['default']['USER']
    # password = settings.DATABASES['default']['PASSWORD']
    # database_name = settings.DATABASES['default']['NAME']

    # database_url = 'postgresql://{user}:{password}@localhost:8000/{database_name}'.format(
    #     user = user,
    #     password = password,
    #     database_name = database_name
    # )
    # engine = create_engine(database_url, echo=False)
    # dataForRegression.to_sql(SavedDataframe, con=engine)



    return ("hello there")

def team_statistics(request, team_name):
    desiredTeam = Team.objects.get(name=team_name)
    avgNationalData = D1Averages.objects.first()
    adjStats = AdjustedStats.objects.get(teamName=team_name)
    teamSchedule = TeamSchedule.objects.filter(teamName=team_name)
    completedGame = CompletedGame.objects.filter(teamName=team_name)
    return render(request, 'team_details.html', {'team': desiredTeam, 'avgNationalData': avgNationalData, 'adjStats': adjStats, 'teamSchedule': teamSchedule, 'completedGame': completedGame})


    
def adjustStats():

    # # code used to get team schedules and calculate adjusted stats
    # # idea:
    # # for each team, you need to get a box score and figure out their adjusted stats for that game (offensive and defensive)
    # # then, you can iteratively add these together, divide by the number of games to get an average, and use this as the team's new efficiency ratings
    nationalAvg = D1Averages.objects.first()
    nationalAvgOffEff = nationalAvg.offensiveEfficiency
    nationalAvgDefEff = nationalAvg.defensiveEfficiency
    nationalAvgEff = (nationalAvgOffEff + nationalAvgDefEff) / 2
    teamsToSiftThrough = Teams()


    for team in teamsToSiftThrough:
        # calculate adjusted stats here
        teamSchedule = Schedule(team.abbreviation)
        teamAdjustedAlready = AdjustedStats.objects.filter(teamName=team.name).first()
        avgNumPossessions = team.pace
        nationalAveragesToUpdate = D1Averages.objects.first()
        nationalAvgEff = (nationalAveragesToUpdate.offensiveEfficiency + nationalAveragesToUpdate.defensiveEfficiency) / 2
        nationalAvgEFGpct = (nationalAveragesToUpdate.eFGpct + nationalAveragesToUpdate.oppEFGpct) / 2
        nationalTurnoverRate = (nationalAveragesToUpdate.turnoverRate + nationalAveragesToUpdate.oppTurnoverRate) / 2
        nationalORebpct = (nationalAveragesToUpdate.oRebpct + nationalAveragesToUpdate.oppORebpct) / 2
        nationalFtaPerFga = (nationalAveragesToUpdate.ftaPerFga + nationalAveragesToUpdate.oppFtaPerFga) / 2
        # nonD1TeamsPlayed = 0
        gameCounted = 0
        offEffNotDivided = 0
        defEffNotDivided = 0
        offEFGNotDivided = 0
        defEFGNotDivided = 0
        offTORateNotDivided = 0
        defTORateNotDivided = 0
        offORebpctNotDivided = 0
        defORebpctNotDivided = 0
        offFtaPerFgaNotDivided = 0
        defFtaPerFgaNotDivided = 0
        # if the team has had its stats adjusted before, use its current adjusted stats and update them
        if (teamAdjustedAlready != None):
            # gets the season adjusted offensive/defensive efficiencies for the team we are on in the loop
            thisTeamObject = AdjustedStats.objects.filter(teamAbbreviation=team.abbreviation).first()
            thisTeamObjectToSave = Team.objects.filter(name=team.name).first()
            teamSeasonAdjOffEfficiency = thisTeamObject.adjOffEff
            teamSeasonAdjDefEfficiency = thisTeamObject.adjDefEff 
            for game in teamSchedule:
                if (game.datetime <= datetime.now() - timedelta(hours=3)):
                    # need to calculate efficiencies for each game (team and opponent) and use opponent adjusted or raw efficiencies in adjustments
                    oppName = game.opponent_name
                    # gets a boxscore object for this game
                    oppTeamObject = AdjustedStats.objects.filter(teamName=oppName).first()
                    # this means a non-D1 opponent was played
                    if (oppTeamObject == None):
                        continue
                    # gets the season adjusted offensive/defensive efficiencies for this opponent
                    oppSeasonAdjOffEfficiency = oppTeamObject.adjOffEff
                    oppSeasonAdjDefEfficiency = oppTeamObject.adjDefEff
                    oppOffEFGpct = oppTeamObject.adjOffEFGpct
                    oppDefEFGpct = oppTeamObject.adjDefEFGpct
                    oppTORate = oppTeamObject.adjTORate
                    oppDefTORate = oppTeamObject.adjDefTORate
                    oppORebpct = oppTeamObject.adjORebpct
                    oppDefORebpct = oppTeamObject.adjDefORebpct
                    oppFtaPerFga = oppTeamObject.adjFtaPerFga
                    oppDefFtaPerFga = oppTeamObject.adjDefFtaPerFga
                    # calculations done below
                    ################################################### DO CALCULATIONS HERE NOW
                    # used for calculating game efficiencies for each team
                    teamPointsScored = game.points_for
                    # this means this game wasn't played (probably due to covid)
                    if (teamPointsScored == None):
                        continue
                    opponentPointsScored = game.points_against
                    boxscore = game.boxscore
                    if ((team.name == boxscore.winning_name and boxscore.home_offensive_rating > boxscore.away_offensive_rating) or (team.name == boxscore.losing_name and boxscore.home_offensive_rating < boxscore.away_offensive_rating)):
                        # then our team is the home team
                        rawOppEFGpctThisGame = boxscore.away_effective_field_goal_percentage * 100
                        rawEFGpctThisGame = boxscore.home_effective_field_goal_percentage * 100
                        rawOppTORateThisGame = boxscore.away_turnover_percentage
                        rawTORateThisGame = boxscore.home_turnover_percentage
                        rawOppORebpctThisGame = boxscore.away_offensive_rebound_percentage
                        rawORebpctThisGame = boxscore.home_offensive_rebound_percentage
                        rawOppFtaPerFgaThisGame = boxscore.away_free_throw_attempt_rate * 100
                        rawFtaPerFgaThisGame = boxscore.home_free_throw_attempt_rate * 100
                    else:
                        rawOppEFGpctThisGame = boxscore.home_effective_field_goal_percentage * 100
                        rawEFGpctThisGame = boxscore.away_effective_field_goal_percentage * 100
                        rawOppTORateThisGame = boxscore.home_turnover_percentage
                        rawTORateThisGame = boxscore.away_turnover_percentage
                        rawOppORebpctThisGame = boxscore.home_offensive_rebound_percentage
                        rawORebpctThisGame = boxscore.away_offensive_rebound_percentage
                        rawOppFtaPerFgaThisGame = boxscore.home_free_throw_attempt_rate * 100
                        rawFtaPerFgaThisGame = boxscore.away_free_throw_attempt_rate * 100
                    # possessions = boxscore.pace
                    # need possessions for raw efficiencies for this game, then need to adjust
                    rawTeamEfficiencyThisGame = (teamPointsScored / avgNumPossessions) * 100
                    # this variable functions as the team's defensive efficiency for the game
                    rawOppEfficiencyThisGame = (opponentPointsScored / avgNumPossessions) * 100
                    # adjust efficiencies here (use already existing adjusted stats for both team and opponent)
                    # national averages = nationalAvgOffEff and nationalAvgDefEff
                    # deltas for this game:
                    # teamOffEffDifference = teamSeasonAdjOffEfficiency - nationalAvgEff
                    oppOffEffDifference = oppSeasonAdjOffEfficiency - nationalAvgEff
                    # teamDefEffDifference = teamSeasonAdjDefEfficiency - nationalAvgEff
                    oppDefEffDifference = oppSeasonAdjDefEfficiency - nationalAvgEff
                    oppOffEFGDifference = oppOffEFGpct - nationalAvgEFGpct
                    oppDefEFGDifference = oppDefEFGpct - nationalAvgEFGpct
                    oppOffTORateDifference = oppTORate - nationalTurnoverRate
                    oppDefTORateDifference = oppDefTORate - nationalTurnoverRate
                    oppOffORebpctDifference = oppORebpct - nationalORebpct
                    oppDefORebpctDifference = oppDefORebpct - nationalORebpct
                    oppOffFtaPerFgaDifference = oppFtaPerFga - nationalFtaPerFga
                    oppDefFtaPerFgaDifference = oppDefFtaPerFga - nationalFtaPerFga

                    # adjusted stats below - add deltas to each game efficiency
                    # off eff for this game - oppDefEffDifference
                    adjustedTeamEfficiencyThisGame = rawTeamEfficiencyThisGame - oppDefEffDifference
                    adjustedOppEfficiencyThisGame = rawOppEfficiencyThisGame - oppOffEffDifference
                    adjustedEFGpctThisGame = rawEFGpctThisGame - oppDefEFGDifference
                    adjustedDefEFGpctThisGame = rawOppEFGpctThisGame - oppOffEFGDifference
                    adjustedTORateThisGame = rawTORateThisGame - oppDefTORateDifference
                    adjustedDefTORateThisGame = rawOppTORateThisGame - oppOffTORateDifference
                    adjustedORebpctThisGame = rawORebpctThisGame - oppDefORebpctDifference
                    adjustedDefORebpctThisGame = rawOppORebpctThisGame - oppOffORebpctDifference
                    adjustedFtaPerFgaThisGame = rawFtaPerFgaThisGame - oppDefFtaPerFgaDifference
                    adjustedDefFtaPerFgaThisGame = rawOppFtaPerFgaThisGame - oppOffFtaPerFgaDifference

                    # add efficiencies to offEffNotDivided and defEffNotDivided here, to be averaged later
                    offEffNotDivided += adjustedTeamEfficiencyThisGame
                    defEffNotDivided += adjustedOppEfficiencyThisGame
                    offEFGNotDivided += adjustedEFGpctThisGame
                    defEFGNotDivided += adjustedDefEFGpctThisGame
                    offTORateNotDivided += adjustedTORateThisGame
                    defTORateNotDivided += adjustedDefTORateThisGame
                    offORebpctNotDivided += adjustedORebpctThisGame
                    defORebpctNotDivided += adjustedDefORebpctThisGame
                    offFtaPerFgaNotDivided += adjustedFtaPerFgaThisGame
                    defFtaPerFgaNotDivided += adjustedDefFtaPerFgaThisGame
                    gameCounted += 1

            # here, outside the for loop, can divide the efficiences by the number of games (length of teamSchedule) if adding method is used
            # (possibly below)
            # this is where all fields of the AdjustedStats object need to be reassinged and then saved
            teamAdjustedAlready.teamName = team.name
            teamAdjustedAlready.teamAbbreviation = team.abbreviation
            teamAdjustedAlready.adjOffEff = round(offEffNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjDefEff = round(defEffNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjEffMargin = round((offEffNotDivided / gameCounted) - (defEffNotDivided / gameCounted), 2)
            teamAdjustedAlready.adjOffEFGpct = round(offEFGNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjDefEFGpct = round(defEFGNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjTORate = round(offTORateNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjDefTORate = round(defTORateNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjORebpct = round(offORebpctNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjDefORebpct = round(defORebpctNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjFtaPerFga = round(offFtaPerFgaNotDivided / gameCounted, 1)
            teamAdjustedAlready.adjDefFtaPerFga = round(defFtaPerFgaNotDivided / gameCounted, 1)
            # not worrying about tempo yet
            # teamAdjustedAlready.adjTempo =
            # add other fields
            teamAdjustedAlready.save()
            thisTeamObjectToSave.adjEffMargin = round((offEffNotDivided / gameCounted) - (defEffNotDivided / gameCounted), 2)
            thisTeamObjectToSave.adjOffEff = round(offEffNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjDefEff = round(defEffNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjOffEFGpct = round(offEFGNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjDefEFGpct = round(defEFGNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjTORate = round(offTORateNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjDefTORate = round(defTORateNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjORebpct = round(offORebpctNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjDefORebpct = round(defORebpctNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjFtaPerFga = round(offFtaPerFgaNotDivided / gameCounted, 1)
            thisTeamObjectToSave.adjDefFtaPerFga = round(defFtaPerFgaNotDivided / gameCounted, 1)
            thisTeamObjectToSave.save()
        # otherwise, if the team has never had its stats adjusted, use the raw stats and adjust for the first time
        else:
            # stat calculations can largely be copied from above, they're just saved differently below
            thisTeamObject = Team.objects.filter(abbreviation=team.abbreviation).first()
            teamSeasonRawOffEfficiency = thisTeamObject.pointsPerPossession
            teamSeasonRawDefEfficiency = thisTeamObject.oppPointsPerPossession
            for game in teamSchedule:
                # need to calculate efficiencies for each game (team and opponent) and use opponent adjusted or raw efficiencies in adjustments
                if (game.datetime <= datetime.now() - timedelta(hours=3)):
                    oppName = game.opponent_name
                    # gets a boxscore object for this game
                    oppTeamObject = Team.objects.filter(name=oppName).first()
                    # this means a non-D1 opponent was played
                    if (oppTeamObject == None):
                        continue
                    # gets the season adjusted offensive/defensive efficiencies for this opponent
                    oppSeasonRawOffEfficiency = oppTeamObject.pointsPerPossession
                    oppSeasonRawDefEfficiency = oppTeamObject.oppPointsPerPossession
                    oppOffEFGpct = oppTeamObject.eFGpct
                    oppDefEFGpct = oppTeamObject.oppEFGpct
                    oppTORate = oppTeamObject.turnoverRate
                    oppDefTORate = oppTeamObject.oppTurnoverRate
                    oppORebpct = oppTeamObject.oRebpct
                    oppDefORebpct = oppTeamObject.oppORebpct
                    oppFtaPerFga = oppTeamObject.ftaPerFga
                    oppDefFtaPerFga = oppTeamObject.oppFtaPerFga
                    # calculations done below
                    ################################################### DO CALCULATIONS HERE NOW
                    # used for calculating game efficiencies for each team
                    teamPointsScored = game.points_for
                    # this means this game wasn't played (probably due to covid)
                    if (teamPointsScored == None):
                        continue
                    opponentPointsScored = game.points_against
                    boxscore = game.boxscore
                    if ((team.name == boxscore.winning_name and boxscore.home_offensive_rating > boxscore.away_offensive_rating) or (team.name == boxscore.losing_name and boxscore.home_offensive_rating < boxscore.away_offensive_rating)):
                        # then our team is the home team
                        rawOppEFGpctThisGame = boxscore.away_effective_field_goal_percentage * 100
                        rawEFGpctThisGame = boxscore.home_effective_field_goal_percentage * 100
                        rawOppTORateThisGame = boxscore.away_turnover_percentage
                        rawTORateThisGame = boxscore.home_turnover_percentage
                        rawOppORebpctThisGame = boxscore.away_offensive_rebound_percentage
                        rawORebpctThisGame = boxscore.home_offensive_rebound_percentage
                        rawOppFtaPerFgaThisGame = boxscore.away_free_throw_attempt_rate * 100
                        rawFtaPerFgaThisGame = boxscore.home_free_throw_attempt_rate * 100
                    else:
                        rawOppEFGpctThisGame = boxscore.home_effective_field_goal_percentage * 100
                        rawEFGpctThisGame = boxscore.away_effective_field_goal_percentage * 100
                        rawOppTORateThisGame = boxscore.home_turnover_percentage
                        rawTORateThisGame = boxscore.away_turnover_percentage
                        rawOppORebpctThisGame = boxscore.home_offensive_rebound_percentage
                        rawORebpctThisGame = boxscore.away_offensive_rebound_percentage
                        rawOppFtaPerFgaThisGame = boxscore.home_free_throw_attempt_rate * 100
                        rawFtaPerFgaThisGame = boxscore.away_free_throw_attempt_rate * 100
                    # possessions = boxscore.pace
                    # need possessions for raw efficiencies for this game, then need to adjust
                    rawTeamEfficiencyThisGame = (teamPointsScored / avgNumPossessions) * 100
                    # this variable functions as the team's defensive efficiency for the game
                    rawOppEfficiencyThisGame = (opponentPointsScored / avgNumPossessions) * 100
                    # adjust efficiencies here (use already existing adjusted stats for both team and opponent)
                    # national averages = nationalAvgOffEff and nationalAvgDefEff
                    # deltas for this game:
                    # teamOffEffDifference = teamSeasonRawOffEfficiency - nationalAvgEff
                    oppOffEffDifference = oppSeasonRawOffEfficiency - nationalAvgEff
                    # teamDefEffDifference = teamSeasonRawDefEfficiency - nationalAvgEff
                    oppDefEffDifference = oppSeasonRawDefEfficiency - nationalAvgEff
                    oppOffEFGDifference = oppOffEFGpct - nationalAvgEFGpct
                    oppDefEFGDifference = oppDefEFGpct - nationalAvgEFGpct
                    oppOffTORateDifference = oppTORate - nationalTurnoverRate
                    oppDefTORateDifference = oppDefTORate - nationalTurnoverRate
                    oppOffORebpctDifference = oppORebpct - nationalORebpct
                    oppDefORebpctDifference = oppDefORebpct - nationalORebpct
                    oppOffFtaPerFgaDifference = oppFtaPerFga - nationalFtaPerFga
                    oppDefFtaPerFgaDifference = oppDefFtaPerFga - nationalFtaPerFga
                    # adjusted stats below - add deltas to each game efficiency
                    # off eff for this game - oppDefEffDifference
                    adjustedTeamEfficiencyThisGame = rawTeamEfficiencyThisGame - oppDefEffDifference
                    adjustedOppEfficiencyThisGame = rawOppEfficiencyThisGame - oppOffEffDifference
                    adjustedEFGpctThisGame = rawEFGpctThisGame - oppDefEFGDifference
                    adjustedDefEFGpctThisGame = rawOppEFGpctThisGame - oppOffEFGDifference
                    adjustedTORateThisGame = rawTORateThisGame - oppDefTORateDifference
                    adjustedDefTORateThisGame = rawOppTORateThisGame - oppOffTORateDifference
                    adjustedORebpctThisGame = rawORebpctThisGame - oppDefORebpctDifference
                    adjustedDefORebpctThisGame = rawOppORebpctThisGame - oppOffORebpctDifference
                    adjustedFtaPerFgaThisGame = rawFtaPerFgaThisGame - oppDefFtaPerFgaDifference
                    adjustedDefFtaPerFgaThisGame = rawOppFtaPerFgaThisGame - oppOffFtaPerFgaDifference
                    # add efficiencies to offEffNotDivided and defEffNotDivided here, to be averaged later
                    offEffNotDivided += adjustedTeamEfficiencyThisGame
                    defEffNotDivided += adjustedOppEfficiencyThisGame
                    offEFGNotDivided += adjustedEFGpctThisGame
                    defEFGNotDivided += adjustedDefEFGpctThisGame
                    offTORateNotDivided += adjustedTORateThisGame
                    defTORateNotDivided += adjustedDefTORateThisGame
                    offORebpctNotDivided += adjustedORebpctThisGame
                    defORebpctNotDivided += adjustedDefORebpctThisGame
                    offFtaPerFgaNotDivided += adjustedFtaPerFgaThisGame
                    defFtaPerFgaNotDivided += adjustedDefFtaPerFgaThisGame
                    gameCounted += 1


            # need to create a new AdjustedStats object here for the team we are on in the for loop
            adjustedStatsForTeam = AdjustedStats(
                teamName = team.name,
                teamAbbreviation = team.abbreviation,
                adjOffEff = round(offEffNotDivided / gameCounted, 1),
                adjDefEff = round(defEffNotDivided / gameCounted, 1),
                adjEffMargin = round((offEffNotDivided / gameCounted) - (defEffNotDivided / gameCounted), 2),
                # skipping adjTempo for now
                # adjTempo = 
                adjOffEFGpct = round(offEFGNotDivided / gameCounted, 1),
                adjDefEFGpct = round(defEFGNotDivided / gameCounted, 1),
                adjTORate = round(offTORateNotDivided / gameCounted, 1),
                adjDefTORate = round(defTORateNotDivided / gameCounted, 1),
                adjORebpct = round(offORebpctNotDivided / gameCounted, 1),
                adjDefORebpct = round(defORebpctNotDivided / gameCounted, 1),
                adjFtaPerFga = round(offFtaPerFgaNotDivided / gameCounted, 1),
                adjDefFtaPerFga = round(defFtaPerFgaNotDivided / gameCounted, 1)
            )
            adjustedStatsForTeam.save()
            thisTeamObject.adjEffMargin = round((offEffNotDivided / gameCounted) - (defEffNotDivided / gameCounted), 2)
            thisTeamObject.adjOffEff = round(offEffNotDivided / gameCounted, 1)
            thisTeamObject.adjDefEff = round(defEffNotDivided / gameCounted, 1)
            thisTeamObject.adjOffEFGpct = round(offEFGNotDivided / gameCounted, 1)
            thisTeamObject.adjDefEFGpct = round(defEFGNotDivided / gameCounted, 1)
            thisTeamObject.adjTORate = round(offTORateNotDivided / gameCounted, 1)
            thisTeamObject.adjDefTORate = round(defTORateNotDivided / gameCounted, 1)
            thisTeamObject.adjORebpct = round(offORebpctNotDivided / gameCounted, 1)
            thisTeamObject.adjDefORebpct = round(defORebpctNotDivided / gameCounted, 1)
            thisTeamObject.adjFtaPerFga = round(offFtaPerFgaNotDivided / gameCounted, 1)
            thisTeamObject.adjDefFtaPerFga = round(defFtaPerFgaNotDivided / gameCounted, 1)
            thisTeamObject.save()
    offTotal = 0
    defTotal = 0
    offEFGTotal = 0
    defEFGTotal = 0
    offTORateTotal = 0
    defTORateTotal = 0
    offORebRateTotal = 0
    defORebRateTotal = 0
    ftaPerFgaTotal = 0
    defFtaPerFgaTotal = 0
    allAdjustedStats = AdjustedStats.objects.all()
    for adjTeam in allAdjustedStats:
        offTotal += adjTeam.adjOffEff
        defTotal += adjTeam.adjDefEff
        offEFGTotal += adjTeam.adjOffEFGpct
        defEFGTotal += adjTeam.adjDefEFGpct
        offTORateTotal += adjTeam.adjTORate
        defTORateTotal += adjTeam.adjDefTORate
        offORebRateTotal += adjTeam.adjORebpct
        defORebRateTotal += adjTeam.adjDefORebpct
        ftaPerFgaTotal += adjTeam.adjFtaPerFga
        defFtaPerFgaTotal += adjTeam.adjDefFtaPerFga

    nationalAveragesToUpdate = D1Averages.objects.first()
    nationalAveragesToUpdate.offensiveEfficiency = round(offTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.defensiveEfficiency = round(defTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.averageEfficiency = round(((offTotal / len(allAdjustedStats)) + (defTotal / len(allAdjustedStats))) / 2, 2)
    nationalAveragesToUpdate.eFGpct = round(offEFGTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.oppEFGpct = round(defEFGTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.turnoverRate = round(offTORateTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.oppTurnoverRate = round(defTORateTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.oRebpct = round(offORebRateTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.oppORebpct = round(defORebRateTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.ftaPerFga = round(ftaPerFgaTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.oppFtaPerFga = round(defFtaPerFgaTotal / len(allAdjustedStats), 1)
    nationalAveragesToUpdate.save()


def initTeams():
    # # code used to get all raw team statistics and put them in the Team model
    teamNamesTest = []
    teamsToSiftThrough = Teams()
    # for ncaaTeams in teamsToSiftThrough:
    # # need an "if" check to see if the team already exists
    #     testExists = Team.objects.filter(name=ncaaTeams.name).first()
    #     if (testExists != None):
    #         testExists.wins = ncaaTeams.wins
    #         testExists.losses = ncaaTeams.losses
    #         testExists.tempo = round(ncaaTeams.pace, 1)
    #         # used to calculate points per possession
    #         tempPointsPerGame = ncaaTeams.points / ncaaTeams.games_played
    #         tempPPP = tempPointsPerGame / ncaaTeams.pace
    #         testExists.pointsPerPossession = round((tempPPP * 100), 2)
    #         # used to calculate opponent points per possesion
    #         tempOppPointsPerGame = ncaaTeams.opp_points / ncaaTeams.games_played
    #         tempOppPPP = tempOppPointsPerGame / ncaaTeams.pace
    #         testExists.oppPointsPerPossession = round((tempOppPPP * 100), 2) 
    #         testExists.efficiencyMargin = round((tempPPP * 100) - (tempOppPPP * 100), 2)
    #         testExists.eFGpct = round((ncaaTeams.effective_field_goal_percentage * 100), 2)
    #         testExists.oppEFGpct = round((ncaaTeams.opp_effective_field_goal_percentage * 100), 2)
    #         testExists.turnoverRate = round(ncaaTeams.turnover_percentage, 1)
    #         testExists.oppTurnoverRate = round(ncaaTeams.opp_turnover_percentage, 1)
    #         testExists.oRebpct = round(ncaaTeams.offensive_rebound_percentage, 1)
    #         testExists.oppORebpct = round(ncaaTeams.opp_offensive_rebound_percentage, 1)
    #         testExists.ftaPerFga = round((ncaaTeams.free_throw_attempt_rate * 100), 2)
    #         testExists.oppFtaPerFga = round((ncaaTeams.opp_free_throw_attempt_rate * 100), 2)
    #         testExists.stealpct = round(ncaaTeams.steal_percentage, 1)
    #         testExists.oppStealpct = round(ncaaTeams.opp_steal_percentage, 1)
    #         testExists.assistRate = round(ncaaTeams.assist_percentage, 1)
    #         testExists.oppAssistRate = round(ncaaTeams.opp_assist_percentage, 1)
    #         testExists.save()
    #     else:
    #         tempPointsPerGame = ncaaTeams.points / ncaaTeams.games_played
    #         tempPPP = tempPointsPerGame / ncaaTeams.pace
    #         tempOppPointsPerGame = ncaaTeams.opp_points / ncaaTeams.games_played
    #         tempOppPPP = tempOppPointsPerGame / ncaaTeams.pace
    #         t = Team(
    #             name = ncaaTeams.name, 
    #             abbreviation = ncaaTeams.abbreviation, 
    #             wins = ncaaTeams.wins, 
    #             losses = ncaaTeams.losses,
    #             tempo = round(ncaaTeams.pace, 1),
    #             pointsPerPossession = round((tempPPP * 100), 2),
    #             oppPointsPerPossession = round((tempOppPPP * 100), 2),
    #             efficiencyMargin = round((tempPPP * 100) - (tempOppPPP * 100), 2),
    #             eFGpct = round((ncaaTeams.effective_field_goal_percentage * 100), 2),
    #             oppEFGpct = round((ncaaTeams.opp_effective_field_goal_percentage * 100), 2),
    #             turnoverRate = round(ncaaTeams.turnover_percentage, 1),
    #             oppTurnoverRate = round(ncaaTeams.opp_turnover_percentage, 1),
    #             oRebpct = round(ncaaTeams.offensive_rebound_percentage, 1),
    #             oppORebpct = round(ncaaTeams.opp_offensive_rebound_percentage, 1),
    #             ftaPerFga = round((ncaaTeams.free_throw_attempt_rate * 100), 2),
    #             oppFtaPerFga = round((ncaaTeams.opp_free_throw_attempt_rate * 100), 2),
    #             stealpct = round(ncaaTeams.steal_percentage, 1),
    #             oppStealpct = round(ncaaTeams.opp_steal_percentage, 1),
    #             assistRate = round(ncaaTeams.assist_percentage, 1),
    #             oppAssistRate = round(ncaaTeams.opp_assist_percentage, 1)
    #             )
    #         t.save()
    #         teamNamesTest.append(ncaaTeams.name)
    # # code used to calculate D1 averages and put them in the D1Averages model
    # offEfficiencyTotal = 0
    # defEfficiencyTotal = 0
    # tempoTotal = 0
    # eFGpctTotal = 0
    # oppEFGpctTotal = 0
    # toRatetotal = 0
    # oppToRateTotal = 0
    # oRebpctTotal = 0
    # oppORebpctTotal = 0
    # ftaPerFgaTotal = 0
    # oppFtaPerFgaTotal = 0
    # allTeamsToLoopThrough = Team.objects.all()
    # for team in allTeamsToLoopThrough:
    #     offEfficiencyTotal += team.pointsPerPossession
    #     defEfficiencyTotal += team.oppPointsPerPossession
    #     tempoTotal += team.tempo
    #     eFGpctTotal += team.eFGpct
    #     oppEFGpctTotal += team.oppEFGpct
    #     toRatetotal += team.turnoverRate
    #     oppToRateTotal += team.oppTurnoverRate
    #     oRebpctTotal += team.oRebpct
    #     oppORebpctTotal += team.oppORebpct
    #     ftaPerFgaTotal += team.ftaPerFga
    #     oppFtaPerFgaTotal += team.oppFtaPerFga
    # if (D1Averages.objects.count() == 0):
    #     avgs = D1Averages(
    #         offensiveEfficiency = offEfficiencyTotal / len(allTeamsToLoopThrough),
    #         defensiveEfficiency = defEfficiencyTotal / len(allTeamsToLoopThrough),
    #         averageEfficiency = ((offEfficiencyTotal / len(allTeamsToLoopThrough)) + (defEfficiencyTotal / len(allTeamsToLoopThrough))) / 2,
    #         tempo = round(tempoTotal / len(allTeamsToLoopThrough), 1),
    #         eFGpct = eFGpctTotal / len(allTeamsToLoopThrough),
    #         oppEFGpct = oppEFGpctTotal / len(allTeamsToLoopThrough),
    #         turnoverRate = toRatetotal / len(allTeamsToLoopThrough),
    #         oppTurnoverRate = oppToRateTotal / len(allTeamsToLoopThrough),
    #         oRebpct = oRebpctTotal / len(allTeamsToLoopThrough),
    #         oppORebpct = oppORebpctTotal / len(allTeamsToLoopThrough),
    #         ftaPerFga = ftaPerFgaTotal / len(allTeamsToLoopThrough),
    #         oppFtaPerFga = oppFtaPerFgaTotal / len(allTeamsToLoopThrough)
    #     )
    #     avgs.save()
    # else:
    #     dataToModify = D1Averages.objects.first()
    #     dataToModify.offensiveEfficiency = offEfficiencyTotal / len(allTeamsToLoopThrough)
    #     dataToModify.defensiveEfficiency = defEfficiencyTotal / len(allTeamsToLoopThrough)
    #     dataToModify.averageEfficiency = ((offEfficiencyTotal / len(allTeamsToLoopThrough)) + (defEfficiencyTotal / len(allTeamsToLoopThrough))) / 2
    #     dataToModify.tempo = round(tempoTotal / len(allTeamsToLoopThrough), 1)
    #     dataToModify.eFGpct = eFGpctTotal / len(allTeamsToLoopThrough)
    #     dataToModify.oppEFGpct = oppEFGpctTotal / len(allTeamsToLoopThrough)
    #     dataToModify.turnoverRate = toRatetotal / len(allTeamsToLoopThrough)
    #     dataToModify.oppTurnoverRate = oppToRateTotal / len(allTeamsToLoopThrough)
    #     dataToModify.oRebpct = oRebpctTotal / len(allTeamsToLoopThrough)
    #     dataToModify.oppORebpct = oppORebpctTotal / len(allTeamsToLoopThrough)
    #     dataToModify.ftaPerFga = ftaPerFgaTotal / len(allTeamsToLoopThrough)
    #     dataToModify.oppFtaPerFga = oppFtaPerFgaTotal / len(allTeamsToLoopThrough)
    #     dataToModify.save()
    

def getSchedules():
    teamsToSiftThrough = Team.objects.all()
    nationalAvgs = D1Averages.objects.first()
    averageTempo = nationalAvgs.tempo
    averageEfficiency = nationalAvgs.averageEfficiency
    for team in teamsToSiftThrough:
        teamSchedule = Schedule(team.abbreviation)
        for game in teamSchedule:
            if (game.datetime >= datetime.today()):
                # case in which the game has yet to be played, in which the predicted stats are added to the TeamSchedule table
                teamORTG = team.adjOffEff
                teamDRTG = team.adjDefEff
                teamTempo = team.tempo
                if (Team.objects.filter(name=game.opponent_name).exists()):
                    oppObject = Team.objects.get(name=game.opponent_name)
                    oppORTG = oppObject.adjOffEff
                    oppDRTG = oppObject.adjDefEff
                    oppTempo = oppObject.tempo
                else:
                    oppORTG = 75
                    oppDRTG = 120
                    oppTempo = averageTempo
                # calculating game predictions
                if (game.location == "Home"):
                    teamOffense = teamORTG + (.014 * teamORTG)
                    teamDefense = teamDRTG - (.014 * teamDRTG)
                    oppOffense = oppORTG - (.014 * oppORTG)
                    oppDefense = oppDRTG + (.014 * oppDRTG)
                if (game.location == "Away"):
                    teamOffense = teamORTG - (.014 * teamORTG)
                    teamDefense = teamDRTG + (.014 * teamDRTG)
                    oppOffense = oppORTG + (.014 * oppORTG)
                    oppDefense = oppDRTG - (.014 * oppDRTG)
                else:
                    teamOffense = teamORTG
                    teamDefense = teamDRTG
                    oppOffense = oppORTG
                    oppDefense = oppDRTG
                expectedTempo = (teamTempo * oppTempo) / averageTempo
                teamOffenseThisGame = (teamOffense * oppDefense) / averageEfficiency
                oppOffenseThisGame = (oppOffense * teamDefense) / averageEfficiency
                teamPointsThisGame = (teamOffenseThisGame * expectedTempo) / 100
                oppPointsThisGame = (oppOffenseThisGame * expectedTempo) / 100
                if (teamPointsThisGame == oppPointsThisGame):
                    if (game.location == "Home" or (game.location == "Neutral" and teamORTG > oppORTG)):
                        teamPointsThisGame += 1
                    else:
                        oppPointsThisGame += 1
                if (teamPointsThisGame > oppPointsThisGame):
                    result = "Win"
                else:
                    result = "Loss"
                thisGameSchedule = TeamSchedule(
                    teamName = team.name,
                    opponent = game.opponent_name,
                    location = game.location,
                    date = game.date,
                    scorePrediction = round(teamPointsThisGame, 0),
                    oppScorePrediction = round(oppPointsThisGame, 0),
                    tempoPrediction = round(expectedTempo, 0),
                    wOrL = result
                )
                thisGameSchedule.save()
            else:
                # case if the game is already completed, in which the game stats are added to the CompletedGame table
                thisBoxscore = game.boxscore
                if (thisBoxscore.home_offensive_rating == None):
                    continue
                if ((thisBoxscore.winning_name == team.name and thisBoxscore.home_offensive_rating > thisBoxscore.away_offensive_rating) or (thisBoxscore.losing_name == team.name and thisBoxscore.home_offensive_rating < thisBoxscore.away_offensive_rating)):
                    teamScore = thisBoxscore.home_points
                    oppScore = thisBoxscore.away_points
                else:
                    teamScore = thisBoxscore.away_points
                    oppScore = thisBoxscore.home_points
                thisGameCompleted = CompletedGame(
                    teamName = team.name,
                    opponent = game.opponent_name,
                    location = game.location,
                    date = game.date,
                    tempo = round(thisBoxscore.pace, 0),
                    teamScore = teamScore,
                    opponentScore = oppScore,
                    seasonWins = game.season_wins,
                    seasonLosses = game.season_losses,
                    wOrL = game.result
                )
                thisGameCompleted.save()
    
    # nationalAvgs = D1Averages.objects.first()
    # averageTempo = nationalAvgs.tempo
    # averageEfficiency = nationalAvgs.averageEfficiency

    # teamsToSiftThrough = Team.objects.all()
    # thisTeam = teamsToSiftThrough[0]
    # teamSchedule = Schedule(thisTeam.abbreviation)
    # for game in teamSchedule:
    #         if (game.datetime >= datetime.today()):
    #             # case in which the game has yet to be played, in which the predicted stats are added to the TeamSchedule table
    #             teamORTG = thisTeam.adjOffEff
    #             teamDRTG = thisTeam.adjDefEff
    #             teamTempo = thisTeam.tempo
    #             oppObject = Team.objects.get(name=game.opponent_name)
    #             oppORTG = oppObject.adjOffEff
    #             oppDRTG = oppObject.adjDefEff
    #             oppTempo = oppObject.tempo
    #             # calculating game predictions
    #             if (game.location == "Home"):
    #                 teamOffense = teamORTG + (.014 * teamORTG)
    #                 teamDefense = teamDRTG - (.014 * teamDRTG)
    #                 oppOffense = oppORTG - (.014 * oppORTG)
    #                 oppDefense = oppDRTG + (.014 * oppDRTG)
    #             if (game.location == "Away"):
    #                 teamOffense = teamORTG - (.014 * teamORTG)
    #                 teamDefense = teamDRTG + (.014 * teamDRTG)
    #                 oppOffense = oppORTG + (.014 * oppORTG)
    #                 oppDefense = oppDRTG - (.014 * oppDRTG)
    #             else:
    #                 teamOffense = teamORTG
    #                 teamDefense = teamDRTG
    #                 oppOffense = oppORTG
    #                 oppDefense = oppDRTG
    #             expectedTempo = (teamTempo * oppTempo) / averageTempo
    #             teamOffenseThisGame = (teamOffense * oppDefense) / averageEfficiency
    #             oppOffenseThisGame = (oppOffense * teamDefense) / averageEfficiency
    #             teamPointsThisGame = (teamOffenseThisGame * expectedTempo) / 100
    #             oppPointsThisGame = (oppOffenseThisGame * expectedTempo) / 100
    #             if (teamPointsThisGame == oppPointsThisGame):
    #                 if (game.location == "Home" or (game.location == "Neutral" and teamORTG > oppORTG)):
    #                     teamPointsThisGame += 1
    #                 else:
    #                     oppPointsThisGame += 1
    #             if (teamPointsThisGame > oppPointsThisGame):
    #                 result = "Win"
    #             else:
    #                 result = "Loss"
    #             thisGameSchedule = TeamSchedule(
    #                 teamName = thisTeam.name,
    #                 opponent = game.opponent_name,
    #                 location = game.location,
    #                 date = game.date,
    #                 scorePrediction = round(teamPointsThisGame, 0),
    #                 oppScorePrediction = round(oppPointsThisGame, 0),
    #                 tempoPrediction = round(expectedTempo, 0),
    #                 wOrL = result
    #             )
    #             thisGameSchedule.save()
    #         else:
    #             # case if the game is already completed, in which the game stats are added to the CompletedGame table
    #             thisBoxscore = game.boxscore
    #             if (thisBoxscore.home_offensive_rating == None):
    #                 continue
    #             if ((thisBoxscore.winning_name == thisTeam.name and thisBoxscore.home_offensive_rating > thisBoxscore.away_offensive_rating) or (thisBoxscore.losing_name == thisTeam.name and thisBoxscore.home_offensive_rating < thisBoxscore.away_offensive_rating)):
    #                 teamScore = thisBoxscore.home_points
    #                 oppScore = thisBoxscore.away_points
    #             else:
    #                 teamScore = thisBoxscore.away_points
    #                 oppScore = thisBoxscore.home_points
    #             thisGameCompleted = CompletedGame(
    #                 teamName = thisTeam.name,
    #                 opponent = game.opponent_name,
    #                 location = game.location,
    #                 date = game.date,
    #                 tempo = round(thisBoxscore.pace, 0),
    #                 teamScore = teamScore,
    #                 opponentScore = oppScore,
    #                 seasonWins = game.season_wins,
    #                 seasonLosses = game.season_losses,
    #                 wOrL = game.result
    #             )
    #             thisGameCompleted.save()