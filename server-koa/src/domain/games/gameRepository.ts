import { Game } from './game'

export abstract class GameRepository {
    abstract findAllAvailableGames(): Array<Game>
    // findGameById(id: string): Array<Game>
    abstract addGame(game: Game): void
}
