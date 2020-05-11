import { Socket } from 'socket.io'
import { SocketController, OnMessage, MessageBody, SocketId, SocketIO } from 'socket-controllers'
import { GameSystem } from '../../application/gameSystem'
import { PlayerInfos } from '../../domain/players/playerInfos'


interface JoinGameRequest {
    username: string,
    gameId: string
}


@SocketController('/games')
export class GamesController {
    constructor(private gameSystem: GameSystem) {}

    @OnMessage('join')
    joinGame(@MessageBody() request: JoinGameRequest, @SocketId() socketId: string, @SocketIO() socket: Socket) {
        this.gameSystem.joinGame(request.gameId, request.username, socketId, socket)
    }

    @OnMessage('update')
    update(@MessageBody() request: PlayerInfos, @SocketId() socketId: string, @SocketIO() socket: Socket) {
        // TODO
    }
}
