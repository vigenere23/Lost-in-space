import { Get, Controller, Post, Body, HttpCode } from '@nestjs/common'
import { IsNotEmpty, IsInt, Min, Max } from 'class-validator'
import { GameService } from '../game.service'

export class CreateGameRequest {
  @IsNotEmpty()
  username: string

  @Min(2)
  @Max(4)
  @IsInt()
  nbPlayers: number

  @IsNotEmpty()
  world: string

  @IsNotEmpty()
  socketId: string
}

export class JoinGameRequest {
  @IsNotEmpty()
  username: string

  @IsNotEmpty()
  gameId: string

  @IsNotEmpty()
  socketId: string
}

@Controller('game')
export class GameRestController {
  constructor(private gameService: GameService) {}

  @Get()
  async getAllGames() {
    return this.gameService.listGames()
  }

  @Post()
  @HttpCode(201)
  async createGame(@Body() request: CreateGameRequest) {
    const { username, nbPlayers, world, socketId } = request
    return this.gameService.createGame(username, nbPlayers, world, socketId)
  }

  @Post('/join')
  @HttpCode(200)
  async joinGame(@Body() request: JoinGameRequest) {
    const { gameId, username, socketId } = request
    return this.gameService.joinGame(gameId, username, socketId)
  }
}
