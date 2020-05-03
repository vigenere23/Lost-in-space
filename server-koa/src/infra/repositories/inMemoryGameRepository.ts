import { Game } from '../../domain/games/game'
import { GameId } from '../../domain/games/gameId'
import { GameRepository } from '../../domain/games/gameRepository'
import { Service } from 'typedi'

@Service()
export class InMemoryGameRepository implements GameRepository {
    private games: Map<string, Game> = new Map()

    findAllAvailable(): Array<Game> {
        return Array
            .from(this.games.values())
            .filter(game => game.isAvailable)
    }

    findById(id: GameId) {
        return this.games.get(id.toString())
    }

    save(game: Game): void {
        if (this.games.has(game.id.toString())) {
            throw new Error(`game with id '${game.id}' already exists`)
        }

        this.games.set(game.id.toString(), game)
    }
}
