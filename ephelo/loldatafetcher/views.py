from django.shortcuts import render
from django.http import HttpResponse
from .models import GameData
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def match_complete(request):
    match_result = request.POST
    tournament_code = match_result["shortCode"]
    match_id = match_result["gameId"]
    # fetch GameData object from tournament_code - exceptions?
    game_data = GameData.objects.get(tournament_code__exact = tournament_code)
    participants = Participant.objects.filter(game_data__exact = game_data.id)
    # TODO send api request to match v3 api to match_data
    match_data_json = None
    game_data.json = match_data_json
    game_data.save()
    # exception?
    match_data = json.loads(match_data_json)
    # create riot participant id to EphElo Participant object dictionary
    participant_from_id = {}
    for identity in match_data["participantIdentities"]:
        summoner_id = identity["player"]["summonerId"];
        participant = Participant.objects.get(
            game_data__tournament_code__exact = tournament_code,
            summoner_id__exact = summoner_id)
        participant_from_id[identity["participantId"]] = participant
    winning_team = []
    losing_team = []
    # populate participant data
    for participant_info in match_data["participants"]:
        participant = participant_from_id[participant_info["participantId"]]
        participant.championId = participant_info["championId"]
        participant.lane = calculateLane(participant_info)
        participant.save()
        if participant_info["stats"]["win"]:
            winning_team.append(participant)
        else:
            losing_team.append(participant)
    calculateElo(winning_team, losing_team)

def calculateLane(participant_info):
    # TODO calculateLane
    pass

def calculateElo(winning_team, losing_team):
    # TODO calculateElo
    pass
