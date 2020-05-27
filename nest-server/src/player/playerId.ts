export class PlayerId {
    private constructor(private value: string) {}

    static fromSocketId(socketId: string): PlayerId {
        return new PlayerId(socketId)
    }

    toString(): string {
        return this.value
    }

    equals(other: PlayerId): boolean {
        return this.value === other.value
    }
}
