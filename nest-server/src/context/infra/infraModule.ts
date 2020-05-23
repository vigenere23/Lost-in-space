import { Module } from '@nestjs/common'
import { gameRepositoryProvider } from './gameRepositoryProvider'
import { gamesEventEmitterProvider } from './gamesEventEmitterProvider'


const providers = [
    gameRepositoryProvider,
    gamesEventEmitterProvider
]

@Module({
    providers: providers,
    exports: providers
})
export class InfraModule {}
