import { Game } from '../domain/games/game'

export class GameSystem {
    readonly games: Array<Game>

    constructor () {
        this.games = [new Game()]
    }
}
