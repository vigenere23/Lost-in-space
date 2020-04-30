import { Container } from 'typedi'
import { Context } from './context'
import { InMemoryGameRepository } from '../infra/repositories/inMemoryGameRepository'

export class MainContext implements Context {

    register(): void {
        Container.set('GameRepository', new InMemoryGameRepository())
    }
}
