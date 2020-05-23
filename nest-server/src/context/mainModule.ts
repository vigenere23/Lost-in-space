import { Module } from '@nestjs/common'
import { RestModule } from './api/rest/restModule'


@Module({
    imports: [
        RestModule
    ]
})
export class MainModule {}
