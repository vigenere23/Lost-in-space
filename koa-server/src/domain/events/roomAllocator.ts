export abstract class RoomAllocator {
    abstract joinRoom(room: string): void
    abstract leaveRoom(room: string): void
}
