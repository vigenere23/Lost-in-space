import { Injectable } from '@nestjs/common'
import { Game } from './game'
import { GameId } from './gameId'
import { GameRepository } from './repository/game.repository'
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
        private gameRepository: GameRepository
    ) {}

    listGames(): Array<GameDto> {
        return this.gameRepository
            .findAllAvailable()
            .map(game => new GameDto(game))
    }

    createGame(hostUsername: string, nbPlayers: number, world: string): void {
        const game = new Game(hostUsername, nbPlayers, world)
        this.gameRepository.save(game)
    }

    joinGame(gameIdString: string, playerUsername: string, socketId: string): void {
        const gameId = GameId.fromString(gameIdString)
        const game = this.gameRepository.findById(gameId)
        const player = new Player(playerUsername, socketId)
        
        game.addPlayer(player)

        try {
            player.setGameId(game.id)
        }
        catch (e) {
            game.removePlayer(player, true)
            throw e
        }

        // if (game.)
    }
}
