import { Game } from './game'
import { GameId } from './gameId'

export abstract class GameRepository {
    abstract findAllAvailable(): Array<Game>
    abstract findById(id: GameId): Game
    abstract save(game: Game): void
}
