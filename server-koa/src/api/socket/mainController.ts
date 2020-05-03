import { SocketController, OnMessage, MessageBody, SocketId, SocketIO } from 'socket-controllers'
import { GameSystem } from '../../application/gameSystem'


type JoinGameRequest = {
    username: string,
    gameId: string
}


@SocketController()
export class MainController {
    constructor(private gameSystem: GameSystem) {}

    @OnMessage('join')
    joinGame(@SocketId() socketId: string, @MessageBody() request: JoinGameRequest) {
        this.gameSystem.joinGame(request.gameId, request.username, socketId)
    }
}
