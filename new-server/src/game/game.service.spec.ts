import { Test, TestingModule } from '@nestjs/testing'
import { GameService } from './game.service'
import { GameRepositoryProvider } from './repository/game.repository.provider'

describe('GameService', () => {
  let service: GameService

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [GameService, new GameRepositoryProvider().provide()]
    }).compile()

    service = module.get<GameService>(GameService)
  })

  it('should be defined', () => {
    expect(service).toBeDefined()
  })
})
