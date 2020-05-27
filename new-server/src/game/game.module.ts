import { Module } from '@nestjs/common'
import { GameRestController } from './controllers/game.controller.rest'
import { GameService } from './game.service'
import { GameRepositoryProvider } from './repository/game.repository.provider'
import { GameGatewayProvider } from './gateway/game.gateways.provider'
import { GameSocketController } from './controllers/game.controllers.socket'


@Module({
    controllers: [
        GameRestController
    ],
    providers: [
        GameSocketController,
        GameService,
        new GameRepositoryProvider().provide(),
        new GameGatewayProvider().provide()
    ]
})
export class GameModule {}
