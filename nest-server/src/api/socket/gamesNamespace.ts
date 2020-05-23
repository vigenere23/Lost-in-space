import { WebSocketGateway, SubscribeMessage, MessageBody } from '@nestjs/websockets'
import { PlayerInfos } from '../../domain/players/playerInfos'
import { GameSystem } from '../../application/gameSystem'


@WebSocketGateway(8081, { namespace: 'games' })
export class GamesNamespace {
    constructor(
        private gameSystem: GameSystem
    ) {}

    @SubscribeMessage('updatePlayer')
    updatePlayer(@MessageBody() infos: PlayerInfos) {

    }
}