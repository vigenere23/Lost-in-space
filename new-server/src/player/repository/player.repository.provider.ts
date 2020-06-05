import { Provider as NestProvider } from '@nestjs/common'
import { Provider } from '../../shared/provider'
import { PlayerRepository } from './player.repository'
import { InMemoryPlayerRepository } from './player.repository.inmemory'

export class PlayerRepositoryProvider implements Provider<PlayerRepository> {
  provide(): NestProvider<PlayerRepository> {
    return {
      provide: PlayerRepository,
      useClass: InMemoryPlayerRepository
    }
  }
}
