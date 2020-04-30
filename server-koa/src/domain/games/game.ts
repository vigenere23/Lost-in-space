export class GameId {
    private constructor(private value: string) {}

    static fromHostUsername(hostUsername: string): GameId {
        return new GameId(hostUsername)
    }

    toString(): string {
        return this.value
    }

    equals(other: GameId): boolean {
        return this.value === other.value
    }
}


export class Game {
    readonly id: GameId
    readonly isAvailable: boolean = true
    private nbPlayers: number
    private players: Array<string> = []
    
    constructor(
        hostUsername: string,
        nbPlayers: number,
        private world: string

    ) {
        if (nbPlayers !== Math.round(nbPlayers)) {
            throw new Error("'nb_players' should be an integer")
        }
        if (nbPlayers < 1 || nbPlayers > 4) {
            throw new Error("'nb_players' should be between 1 and 4")
        }
        this.id = GameId.fromHostUsername(hostUsername)
        this.nbPlayers = nbPlayers
    }

    playersRemaining(): number {
        return this.nbPlayers - this.players.length
    }
}
