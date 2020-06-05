import { Injectable } from '@nestjs/common'
import { PlayerRepository } from './player.repository'
import { InMemoryRepository } from '../../shared/repository.inmemory'
import { PlayerId } from '../playerId'
import { Player } from '../player'

@Injectable()
export class InMemoryPlayerRepository
  implements PlayerRepository, InMemoryRepository {
  // TODO check for username uniqueness
  private players: Map<string, Player> = new Map()

  findById(id: PlayerId): Player {
    return this.players.get(id.toString())
  }

  save(player: Player): void {
    if (this.players.has(player.id.toString())) {
      throw new Error(`player with id '${player.id}' already exists`)
    }

    this.players.set(player.id.toString(), player)
  }

  update(player: Player): void {
    if (!this.players.has(player.id.toString())) {
      throw new Error(`player with id '${player.id}' does not exist`)
    }

    this.players.set(player.id.toString(), player)
  }

  delete(player: Player): void {
    if (!this.players.has(player.id.toString())) {
      throw new Error(`player with id '${player.id}' does not exist`)
    }

    this.players.delete(player.id.toString())
  }

  clear(): void {
    this.players.clear()
  }
}
