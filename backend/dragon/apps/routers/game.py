from datetime import timedelta
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status

from dragon.apps.documents.document import Game, Round, GamePlayer
from dragon.config import settings


router = APIRouter(prefix="")



@router.post("/api/create/game", status_code=201, response_model=Game)
async def create_game(item: Game):
    return await item.save()


@router.get("/api/get/all/game")
async def get_all():
    return await Game.find_all().to_list()


@router.delete("/api/delete/all/game")
async def delete_all():
    return await Game.delete_all()


@router.post("/api/create/round", status_code=201)
async def get_all(item: Round):
    return await item.save()


@router.get("/api/get/all/round")
async def get_all():
    return await Round.find_all().to_list()


@router.delete("/api/delete/all/round")
async def delete_all():
    return await Round.delete_all()


@router.get("/api/get/all/game_player")
async def get_all():
    return await GamePlayer.find_all().to_list()


@router.delete("/api/delete/all/game_player")
async def delete_all():
    return await GamePlayer.delete_all()