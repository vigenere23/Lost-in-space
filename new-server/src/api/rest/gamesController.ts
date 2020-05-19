import { JsonController, UseBefore, Get, Post, Body, OnUndefined } from 'routing-controllers'
import { ErrorMapping } from '../middlewares'
import { GameSystem, GameDto } from '../../application/gameSystem'


interface CreateGameRequest {
    username: string,
    nbPlayers: number,
    world: string
}

interface JoinGameRequest {
    username: string,
    gameId: string,
    socketId: string
}


@JsonController('/games')
@UseBefore(ErrorMapping)
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

    @Post('/join')
    @OnUndefined(200)
    joinGame(@Body() request: JoinGameRequest) {
        this.gameSystem.joinGame(request.gameId, request.username, request.socketId)
    }
}
