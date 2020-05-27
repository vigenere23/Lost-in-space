import { Get, Controller, Post, Body, HttpCode } from '@nestjs/common'
import { IsNotEmpty, IsInt, Min, Max } from 'class-validator'
import { GameService } from '../game.service'


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
export class GameRestController {
    constructor(
        private gameService: GameService
    ) {}

    @Get()
    async getAllGames() {
        return this.gameService.listGames()
    }
    
    @Post()
    @HttpCode(201)
    async createGame(@Body() request: CreateGameRequest) {
        const { username, nbPlayers, world } = request
        this.gameService.createGame(username, nbPlayers, world)
    }

    @Post()
    async joinGame(@Body() request: JoinGameRequest) {
        const { gameId, username, socketId } = request
        try {
            this.gameService.joinGame(gameId, username, socketId)
        }
        catch (exception ) {
            
        }
    }
}
