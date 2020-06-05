import { Injectable } from '@nestjs/common'
import { Server } from 'socket.io'
import { GameGateway } from './game.gateway'
import { Player } from '../../player/player'
import { PlayerId } from '../../player/playerId'
import { WebSocketServer, WebSocketGateway } from '@nestjs/websockets'

@Injectable()
@WebSocketGateway({ namespace: 'game' })
export class SocketIoGameGateway implements GameGateway {
  @WebSocketServer()
  private io: Server

  sendStartGame(world: string, socketIds: Array<string>): void {
    socketIds.forEach(socketId => {
      this.io.to(socketId).emit('start', {
        world
      })
    })
  }

  sendPlayerUpdate(player: Player, socketIds: Array<string>): void {
    socketIds
      .filter(socketId => !PlayerId.fromSocketId(socketId).equals(player.id))
      .forEach(socketId => {
        this.io.to(socketId).emit('update', {
          username: player.id.toString(),
          ...player.position
        })
      })
  }
}
