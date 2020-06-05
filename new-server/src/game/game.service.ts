import { Injectable } from '@nestjs/common'
import { Game } from './game'
import { GameId } from './gameId'
import { GameRepository } from './repository/game.repository'
import { PlayerRepository } from '../player/repository/player.repository'
import { Player } from '../player/player'

export class GameDto {
  readonly id: string
  readonly playersRemaining: number

  constructor(game: Game) {
    this.id = game.id.toString()
    this.playersRemaining = game.playersRemaining()
  }
}

@Injectable()
export class GameService {
  constructor(
    private gameRepository: GameRepository,
    private playerRepository: PlayerRepository
  ) {}

  listGames(): Array<GameDto> {
    return this.gameRepository.findAllAvailable().map(game => new GameDto(game))
  }

  createGame(
    hostUsername: string,
    nbPlayers: number,
    world: string,
    socketId: string
  ): void {
    const player = new Player(hostUsername, socketId)
    this.playerRepository.save(player)

    const game = new Game(hostUsername, nbPlayers, world)

    try {
      this.gameRepository.save(game)
    } catch (exception) {
      this.playerRepository.delete(player)
      throw exception
    }

    game.addPlayer(player)

    this.gameRepository.update(game)
    this.playerRepository.update(player)
  }

  joinGame(
    gameIdString: string,
    playerUsername: string,
    socketId: string
  ): void {
    const gameId = GameId.fromString(gameIdString)
    const game = this.gameRepository.findById(gameId)

    const player = new Player(playerUsername, socketId)
    this.playerRepository.save(player)

    game.addPlayer(player)

    this.gameRepository.update(game)
    this.playerRepository.update(player)
  }
}
