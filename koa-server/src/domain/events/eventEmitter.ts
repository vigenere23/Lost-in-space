export abstract class EventEmitter {
    abstract emitToRoom(room: string, message: any, excludeCurrent: boolean): void
}
