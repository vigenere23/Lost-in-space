import { Container } from 'typedi'
import { Context } from './context'
import { GameRepository } from '../domain/games/gameRepository'
import { InMemoryGameRepository } from '../infra/repositories/inMemoryGameRepository'

export class MainContext implements Context {

    register(): void {
        Container.set(GameRepository, new InMemoryGameRepository())
    }
}
