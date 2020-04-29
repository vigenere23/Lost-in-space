import { JsonController, Get } from 'routing-controllers'
import { GameSystem } from '../../application/gameSystem'

@JsonController('')
export class MainController {
    constructor(private gameSystem: GameSystem) {}

    @Get('/list')
    listGames(): Array<string> {
        return this.gameSystem.games.map(game => game.id)
    }
}
