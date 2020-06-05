import { Injectable } from '@nestjs/common'
import { Game } from '../game'
import { GameId } from '../gameId'
import { GameRepository } from './game.repository'
import { InMemoryRepository } from '../../shared/repository.inmemory'

// TODO add custom exception
@Injectable()
export class InMemoryGameRepository
  implements GameRepository, InMemoryRepository {
  private games: Map<string, Game> = new Map()

  findAllAvailable(): Array<Game> {
    return Array.from(this.games.values()).filter(game => game.isAvailable)
  }

  findById(id: GameId): Game {
    const game = this.games.get(id.toString())

    if (!game) {
      throw new Error(`game with id '${id}' does not exist`)
    }

    return game
  }

  save(game: Game): void {
    if (this.games.has(game.id.toString())) {
      throw new Error(`game with id '${game.id}' already exists`)
    }

    this.games.set(game.id.toString(), game)
  }

  update(game: Game): void {
    if (!this.games.has(game.id.toString())) {
      throw new Error(`game with id '${game.id}' does not exist`)
    }

    this.games.set(game.id.toString(), game)
  }

  delete(game: Game): void {
    if (!this.games.has(game.id.toString())) {
      throw new Error(`game with id '${game.id}' does not exist`)
    }

    this.games.delete(game.id.toString())
  }

  clear() {
    this.games.clear()
  }
}
