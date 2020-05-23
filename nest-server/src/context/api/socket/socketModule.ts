import { Module } from '@nestjs/common'
import { ApplicationModule } from '../../application/applicationModule'
import { GamesNamespace } from '../../../api/socket/gamesNamespace'


@Module({
    imports: [
        ApplicationModule
    ],
    providers: [
        GamesNamespace
    ]
})
export class SocketModule {}
