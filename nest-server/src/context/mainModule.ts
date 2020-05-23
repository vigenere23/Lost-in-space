import { Module } from '@nestjs/common'
import { RestModule } from './api/rest/restModule'
import { SocketModule } from './api/socket/socketModule'


@Module({
    imports: [
        RestModule,
        SocketModule
    ]
})
export class MainModule {}
