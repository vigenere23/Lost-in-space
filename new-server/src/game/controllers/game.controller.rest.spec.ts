import { Test, TestingModule } from '@nestjs/testing'
import { GameRestController } from './game.controller.rest'
import { GameModule } from '../game.module'

describe('Game Controller', () => {
  let controller: GameRestController

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      // TODO mocking
      imports: [GameModule]
    }).compile()

    controller = module.get<GameRestController>(GameRestController)
  })

  it('should be defined', () => {
    expect(controller).toBeDefined()
  })
})
