import { Injectable } from '@nestjs/common'
import { WebSocketGateway, WebSocketServer } from '@nestjs/websockets'
import { Server } from 'socket.io'
import { GamesEventEmitter as GamesEventEmitter } from '../../domain/events/gamesEventEmitter'
import { Player } from '../../domain/players/player'
import { PlayerId } from '../../domain/players/playerId'


@Injectable()
@WebSocketGateway(8081, { namespace: 'games' })
export class SocketIoGamesEventEmitter implements GamesEventEmitter {
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
