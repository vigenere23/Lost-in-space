import { PlayerId } from '../playerId'
import { Player } from '../player'

export abstract class PlayerRepository {
  abstract findById(id: PlayerId): Player
  abstract save(player: Player): void
  abstract update(player: Player): void
  abstract delete(player: Player): void
}
