import { Game } from './game'
import { Service } from 'typedi';

export interface GameRepository {
    findAllAvailableGames(): Array<Game>
    // findGameById(id: string): Array<Game>
    addGame(game: Game): void
}
