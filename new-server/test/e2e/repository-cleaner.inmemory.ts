import { INestApplication } from '@nestjs/common'
import { InMemoryGameRepository } from '../../src/game/repository/game.repository.inmemory'
import { GameRepository } from '../../src/game/repository/game.repository'
import { PlayerRepository } from '../../src/player/repository/player.repository'
import { InMemoryPlayerRepository } from '../../src/player/repository/player.repository.inmemory'

export class InMemoryRepositoryCleaner {
  static resetRepositories(app: INestApplication) {
    app.get<GameRepository, InMemoryGameRepository>(GameRepository).clear()
    app
      .get<PlayerRepository, InMemoryPlayerRepository>(PlayerRepository)
      .clear()
  }
}
