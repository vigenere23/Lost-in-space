import { Provider as NestProvider } from '@nestjs/common'
import { Provider } from '../../shared/provider'
import { GameGateway } from './game.gateway'
import { SocketIoGameGateway } from './game.gateway.socketio'


export class GameGatewayProvider implements Provider<GameGateway> {
    provide(): NestProvider<GameGateway> {
        return {
            provide: GameGateway,
            useClass: SocketIoGameGateway
        }
    }
}
