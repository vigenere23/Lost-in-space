import { GameId } from './gameId'
import { Player } from '../players/player'
import { findIndexByEquality } from '../../utils/arrayutils'
import { Equalable } from '../../utils/equalable'


export class Game implements Equalable<Game> {
    readonly id: GameId
    private _isAvailable: boolean = true
    private nbPlayers: number
    private players: Array<Player> = []
    
    constructor(
        hostUsername: string,
        nbPlayers: number,
        private world: string
    ) {
        if (nbPlayers !== Math.round(nbPlayers)) {
            throw new Error("'nb_players' should be an integer")
        }
        if (nbPlayers < 1 || nbPlayers > 4) {
            throw new Error("'nb_players' should be between 1 and 4")
        }
        this.id = GameId.fromHostUsername(hostUsername)
        this.nbPlayers = nbPlayers
    }

    playersRemaining(): number {
        return this.nbPlayers - this.players.length
    }

    addPlayer(player: Player): void {
        if (!this._isAvailable) {
            throw new Error("the game has no room for new players")
        }

        this.players.push(player)
        if (this.playersRemaining() === 0) {
            this._isAvailable = false
        }
    }

    removePlayer(player: Player, becomesAvailable: boolean = false): void {
        const index = findIndexByEquality(this.players, player)
        if (index === -1) {
            throw new Error("can't remove player: not present")
        }

        this.players.splice(index, 1)

        if (becomesAvailable) {
            this._isAvailable = true
        }
    }

    isAvailable(): boolean {
        return this._isAvailable
    }

    equals(other: Game): boolean {
        return this.id.equals(other.id)
    }
}
