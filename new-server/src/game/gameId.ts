export class GameId {
    private constructor(private value: string) {}

    static fromHostUsername(hostUsername: string): GameId {
        return new GameId(hostUsername)
    }

    static fromString(value: string): GameId {
        return new GameId(value)
    }

    toString(): string {
        return this.value
    }

    equals(other: GameId): boolean {
        return this.value === other.value
    }
}
