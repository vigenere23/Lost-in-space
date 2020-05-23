import { Module } from '@nestjs/common'
import { GamesController } from '../../../api/rest/gamesController'
import { ApplicationModule } from '../../application/applicationModule'


@Module({
    controllers: [
        GamesController
    ],
    imports: [
        ApplicationModule
    ]
})
export class RestModule {}
