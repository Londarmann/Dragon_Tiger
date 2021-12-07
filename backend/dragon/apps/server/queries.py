from dragon.apps.documents.document import GamePlayer




async def get_or_create_game_player(game_id):
    game_player = await GamePlayer.find_one(GamePlayer.game_round_id == game_id)
    if game_player:
        return game_player
    game_player = GamePlayer(game_round_id=game_id)
    return await game_player.save()
    
async def get_or_create_game_round(game_id: str):

    game_round = Round(game_id=game_id)
    return await game_round.save()


