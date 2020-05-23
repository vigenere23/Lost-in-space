import { Module } from '@nestjs/common'
import { gameRepositoryProvider } from './gameRepositoryProvider'


const providers = [
    gameRepositoryProvider
]

@Module({
    providers: providers,
    exports: providers
})
export class InfraModule {}
