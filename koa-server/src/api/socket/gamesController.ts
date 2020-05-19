import { SocketController, OnMessage, MessageBody, SocketId } from 'socket-controllers'
import { GameSystem } from '../../application/gameSystem'
import { PlayerInfos } from '../../domain/players/playerInfos'


export const namespace: string = '/games'

@SocketController(namespace)
export class GamesController {
    constructor(private gameSystem: GameSystem) {}

    @OnMessage('update')
    update(@MessageBody() request: PlayerInfos, @SocketId() socketId: string) {
        // TODO
    }
}
