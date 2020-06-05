import { Injectable } from '@nestjs/common'
import { PlayerRepository } from './player.repository'
import { InMemoryRepository } from '../../shared/repository.inmemory'
import { PlayerId } from '../playerId'
import { Player } from '../player'

// TODO add custom exception
@Injectable()
export class InMemoryPlayerRepository
  implements PlayerRepository, InMemoryRepository {
  private playersById: Map<string, Player> = new Map()
  private usernames: Set<string> = new Set()

  findById(id: PlayerId): Player {
    const player = this.playersById.get(id.toString())

    if (!player) {
      throw new Error(`player with id '${id}' does not exist`)
    }

    return player
  }

  save(player: Player): void {
    if (this.playersById.has(player.id.toString())) {
      throw new Error(`player with id '${player.id}' already exists`)
    }

    if (this.usernames.has(player.username)) {
      throw new Error(
        `player with username '${player.username}' already exists`
      )
    }

    this.playersById.set(player.id.toString(), player)
    this.usernames.add(player.username)
  }

  update(player: Player): void {
    if (!this.playersById.has(player.id.toString())) {
      throw new Error(`player with id '${player.id}' does not exist`)
    }

    this.playersById.set(player.id.toString(), player)
  }

  delete(player: Player): void {
    if (!this.playersById.has(player.id.toString())) {
      throw new Error(`player with id '${player.id}' does not exist`)
    }

    this.playersById.delete(player.id.toString())
    this.usernames.delete(player.username)
  }

  clear(): void {
    this.playersById.clear()
    this.usernames.clear()
  }
}
