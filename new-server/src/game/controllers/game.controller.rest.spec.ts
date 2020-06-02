import { Test, TestingModule } from '@nestjs/testing'
import { GameRestController } from './game.controller.rest'
import { GameService } from '../game.service'
import { GameRepositoryProvider } from '../repository/game.repository.provider'

describe('Game Controller', () => {
  let controller: GameRestController

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [GameRestController],
      providers: [GameService, new GameRepositoryProvider().provide()]
    }).compile()

    controller = module.get<GameRestController>(GameRestController)
  })

  it('should be defined', () => {
    expect(controller).toBeDefined()
  })
})
