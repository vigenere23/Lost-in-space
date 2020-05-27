export abstract class GameGateway {
    abstract sendStartGame(world: string, socketIds: Array<string>): void
}
