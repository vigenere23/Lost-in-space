import { GameRepository } from '../../domain/games/gameRepository'
import { InMemoryGameRepository } from '../../infra/repositories/inMemoryGameRepository'


export const gameRepositoryProvider = {
    provide: GameRepository,
    useClass: InMemoryGameRepository
}
