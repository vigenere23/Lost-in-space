import { Provider as NestProvider } from '@nestjs/common'
import { Provider } from '../../shared/provider'
import { GameRepository } from './game.repository'
import { InMemoryGameRepository } from './game.repository.inmemory'


export class GameRepositoryProvider implements Provider<GameRepository> {
    provide(): NestProvider<GameRepository> {
        return {
            provide: GameRepository,
            useClass: InMemoryGameRepository
        }
    }
}
