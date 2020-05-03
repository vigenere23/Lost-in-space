import { Server } from 'socket.io'
import { Container } from 'typedi'
import { Context } from './context'
import { GameRepository } from '../domain/games/gameRepository'
import { InMemoryGameRepository } from '../infra/repositories/inMemoryGameRepository'

export class InfraContext implements Context {
    constructor(
        private io: Server
    ) {}

    register(): void {
        // TODO set events dependency injections with io instance
        Container.set(GameRepository, new InMemoryGameRepository())
    }
}
