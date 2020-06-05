import {
  WebSocketGateway,
  SubscribeMessage,
  MessageBody,
  OnGatewayDisconnect
} from '@nestjs/websockets'
import { Socket } from 'socket.io'
import { PlayerInfos } from '../../player/playerInfos'
import { GameService } from '../game.service'
import { UsePipes, ValidationPipe } from '@nestjs/common'

@UsePipes(new ValidationPipe())
@WebSocketGateway({ namespace: 'game' })
export class GameSocketController implements OnGatewayDisconnect {
  constructor(private gameService: GameService) {}

  @SubscribeMessage('updatePlayer')
  updatePlayer(@MessageBody() infos: PlayerInfos) {
    console.log('IT WORKS')
  }

  handleDisconnect(socket: Socket) {
    this.gameService.removePlayer(socket.id)
  }
}
