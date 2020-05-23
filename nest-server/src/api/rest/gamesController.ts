import { Get, Controller, Post, Body, HttpCode } from '@nestjs/common'
import { IsNotEmpty, IsInt, Min, Max } from 'class-validator'
import { GameSystem } from '../../application/gameSystem'


class CreateGameRequest {
    @IsNotEmpty()
    username: string

    @Min(1)
    @Max(4)
    @IsInt()
    nbPlayers: number
    
    @IsNotEmpty()
    world: string
}

class JoinGameRequest {
    @IsNotEmpty()
    username: string

    @IsNotEmpty()
    gameId: string

    @IsNotEmpty()
    socketId: string
}


@Controller('games')
export class GamesController {
    constructor(
        private gameSystem: GameSystem
    ) {}

    @Get()
    async getAllGames() {
        return this.gameSystem.listGames()
    }
    
    @Post()
    @HttpCode(201)
    async createGame(@Body() request: CreateGameRequest) {
        const { username, nbPlayers, world } = request
        this.gameSystem.createGame(username, nbPlayers, world)
    }

    @Post()
    async joinGame(@Body() request: JoinGameRequest) {
        const { gameId, username, socketId } = request
        try {
            this.gameSystem.joinGame(gameId, username, socketId)
        }
        catch (exception ) {
            
        }
    }
}
