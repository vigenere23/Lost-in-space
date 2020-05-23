export abstract class GamesEventEmitter {
    abstract sendStartGame(world: string, socketIds: Array<string>): void
}
