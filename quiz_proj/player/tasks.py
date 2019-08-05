from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from question.models import Category
from game.models import Game, GameParticipant
from player.models import Player,PlayerQueue


@task
def poll_queue():
    categories = Category.objects.all()
    for category in categories:
        query = PlayerQueue.objects.filter(category=category)[0:2]
        print(query.values())
        if len(query) == 2 :
            game = Game(category=category)
            game.save()
            for player in query.values('player_id'):
                game_participant = GameParticipant(player=Player.objects.get(id=player['player_id']))
                game_participant.save()
                game.participants.add(game_participant)
            PlayerQueue.objects.filter(id__in=query.values_list('id')).delete()
