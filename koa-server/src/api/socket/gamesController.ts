import { Socket } from 'socket.io'
import { SocketController, OnMessage, MessageBody, SocketId, SocketIO } from 'socket-controllers'
import { GameSystem } from '../../application/gameSystem'


interface JoinGameRequest {
    username: string,
    gameId: string
}

interface UpdateStatusRequest {
    position: Array<Number>,
    angle: Number
}


@SocketController('/games')
export class GamesController {
    constructor(private gameSystem: GameSystem) {}

    @OnMessage('join')
    joinGame(@MessageBody() request: JoinGameRequest, @SocketId() socketId: string, @SocketIO() socket: Socket) {
        this.gameSystem.joinGame(request.gameId, request.username, socketId, socket)
    }

    @OnMessage('update')
    update(@MessageBody() request: UpdateStatusRequest, @SocketId() socketId: string, @SocketIO() socket: Socket) {
        // TODO
    }
}
