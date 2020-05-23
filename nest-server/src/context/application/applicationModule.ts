import { Module } from '@nestjs/common'
import { InfraModule } from '../infra/infraModule'
import { gameSystemProvider } from './gameSystemProvider'


const providers = [
    gameSystemProvider
]

@Module({
    providers: providers,
    exports: providers,
    imports: [
        InfraModule
    ]
})
export class ApplicationModule {}
