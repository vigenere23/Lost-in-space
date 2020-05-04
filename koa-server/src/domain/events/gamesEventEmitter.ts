export abstract class EventEmitter {
    abstract sendStartGame(world: string, socketIds: Array<string>): void
}
