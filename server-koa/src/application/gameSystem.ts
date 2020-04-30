import { Service, Inject } from 'typedi'
import { Game } from '../domain/games/game'
import { GameRepository } from '../domain/games/gameRepository'


export class GameDto {
    readonly id: string
    readonly playersRemaining: number

    constructor(game: Game) {
        this.id = game.id.toString()
        this.playersRemaining = game.playersRemaining()
    }
}


@Service()
export class GameSystem {
    private games: Array<Game> = []

    constructor(
        @Inject('GameRepository') private gameRepository: GameRepository
    ) {}

    listGames(): Array<GameDto> {
        return this.gameRepository
            .findAllAvailableGames()
            .map(game => new GameDto(game))
    }

    createGame(hostUsername: string, nbPlayers: number, world: string): void {
        const game = new Game(hostUsername, nbPlayers, world)
        this.gameRepository.addGame(game)
    }
}
