import { INestApplication } from '@nestjs/common'
import { InMemoryGameRepository } from '../../src/game/repository/game.repository.inmemory'
import { GameRepository } from '../../src/game/repository/game.repository'

export class InMemoryRepositoryCleaner {
  static resetRepositories(app: INestApplication) {
    app.get<GameRepository, InMemoryGameRepository>(GameRepository).clear()
  }
}
