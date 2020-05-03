import { JsonController, Get, Post, Body, OnUndefined } from 'routing-controllers'
import { GameSystem, GameDto } from '../../application/gameSystem'


type CreateGameRequest = {
    username: string,
    nbPlayers: number,
    world: string
}


@JsonController('/games')
export class GamesController {
    constructor(private gameSystem: GameSystem) {}

    @Get('/list')
    listGames(): Array<GameDto> {
        return this.gameSystem.listGames()
    }

    @Post('/create')
    @OnUndefined(201)
    createGame(@Body() request: CreateGameRequest) {
        this.gameSystem.createGame(request.username, request.nbPlayers, request.world)
    }
}
