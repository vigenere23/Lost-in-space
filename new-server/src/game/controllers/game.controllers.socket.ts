import { WebSocketGateway, SubscribeMessage, MessageBody } from '@nestjs/websockets'
import { PlayerInfos } from '../../player/playerInfos'
import { GameService } from '../game.service'
import { UsePipes, ValidationPipe } from '@nestjs/common'


// TODO add validation
@UsePipes(new ValidationPipe())
@WebSocketGateway({ namespace: 'game' })
export class GameSocketController {
    constructor(
        private gameService: GameService
    ) {}

    @SubscribeMessage('updatePlayer')
    updatePlayer(@MessageBody() infos: PlayerInfos) {
        console.log('IT WORKS')
    }
}
