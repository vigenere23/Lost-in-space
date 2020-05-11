import { PlayerId } from './playerId'
import { GameId } from '../games/gameId'
import { Equalable } from '../../utils/equalable'
import { Position } from '../position'


export class Player implements Equalable<Player> {
    readonly id: PlayerId
    private gameId: GameId
    public position: Position

    constructor(
        readonly username: string,
        socketId: string
    ) {
        this.id = PlayerId.fromSocketId(socketId)
    }

    setGameId(gameId: GameId) {
        if (this.gameId) {
            throw new Error("this player is already assigned to a game!")
        }

        this.gameId = gameId
    }

    equals(other: Player): boolean {
        return this.id.equals(other.id)
    }
}
