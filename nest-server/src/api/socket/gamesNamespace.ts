import { WebSocketGateway, SubscribeMessage, MessageBody } from '@nestjs/websockets'
import { PlayerInfos } from '../../domain/players/playerInfos'
import { GameSystem } from '../../application/gameSystem'
import { UsePipes, ValidationPipe } from '@nestjs/common'


// TODO add validation
@UsePipes(new ValidationPipe())
@WebSocketGateway({ namespace: 'games' })
export class GamesNamespace {
    constructor(
        private gameSystem: GameSystem
    ) {}

    @SubscribeMessage('updatePlayer')
    updatePlayer(@MessageBody() infos: PlayerInfos) {
        console.log('IT WORKS')
    }
}
