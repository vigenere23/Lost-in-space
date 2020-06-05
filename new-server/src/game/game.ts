import { ArgumentError } from '../shared/exceptions'
import { GameId } from './gameId'
import { Player } from '../player/player'
import { findIndexByEquality } from '../shared/arrayutils'
import { Equalable } from '../shared/equalable'

export class Game implements Equalable<Game> {
  readonly id: GameId
  private _isAvailable = true
  private nbPlayers: number
  private players: Array<Player> = []

  constructor(hostUsername: string, nbPlayers: number, private world: string) {
    if (nbPlayers !== Math.round(nbPlayers)) {
      throw new ArgumentError("'nb_players' should be an integer")
    }
    if (nbPlayers < 1 || nbPlayers > 4) {
      throw new ArgumentError("'nb_players' should be between 1 and 4")
    }
    this.id = GameId.fromHostUsername(hostUsername)
    this.nbPlayers = nbPlayers
  }

  playersRemaining(): number {
    return this.nbPlayers - this.players.length
  }

  addPlayer(player: Player): void {
    if (!this._isAvailable) {
      throw new ArgumentError('the game has no room for new players')
    }

    player.setGameId(this.id)
    this.players.push(player)

    if (this.playersRemaining() === 0) {
      this._isAvailable = false
      // TODO send start event with this.world
    }
  }

  removePlayer(player: Player): void {
    const index = findIndexByEquality(this.players, player)
    if (index === -1) {
      throw new ArgumentError("can't remove player: not present")
    }

    this.players.splice(index, 1)
  }

  isAvailable(): boolean {
    return this._isAvailable
  }

  equals(other: Game): boolean {
    return this.id.equals(other.id)
  }
}
