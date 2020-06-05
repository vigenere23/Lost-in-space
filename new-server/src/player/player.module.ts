import { Module } from '@nestjs/common'
import { PlayerRepositoryProvider } from './repository/player.repository.provider'

const playerRepositoryProvider = new PlayerRepositoryProvider().provide()

@Module({
  providers: [playerRepositoryProvider],
  exports: [playerRepositoryProvider]
})
export class PlayerModule {}
