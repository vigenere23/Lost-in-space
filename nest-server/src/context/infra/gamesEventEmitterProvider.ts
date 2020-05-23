import { GamesEventEmitter } from '../../domain/events/gamesEventEmitter'
import { SocketIoGamesEventEmitter } from '../../infra/events/socketIoGamesEventEmitter'


export const gamesEventEmitterProvider = {
    provide: GamesEventEmitter,
    useClass: SocketIoGamesEventEmitter
}
