import { JsonController, Get, Post, Body, OnUndefined } from 'routing-controllers'
import { GameSystem, GameDto } from '../../application/gameSystem'


type GameRequest = {
    hostUsername: string,
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
    createGame(@Body() game: GameRequest) {
        this.gameSystem.createGame(game.hostUsername, game.nbPlayers, game.world)
    }
}
