import 'reflect-metadata'
import { NestFactory } from '@nestjs/core'
import { INestApplication, ValidationPipe } from '@nestjs/common'
import { NestExpressApplication } from '@nestjs/platform-express'
import { MainModule } from './context/mainModule'


export class NestServer {
    constructor(
        private app: INestApplication,
        // private io: socketIO.Server,
        readonly host: string = '127.0.0.1',
        readonly port: number = 8080
    ) {
        // this.registerContexts(this.io)
    }

    static async create(host: string = '127.0.0.1', port: number = 8080): Promise<NestServer> {
        const app = await this.createRestApp()
        // const io = this.createSocketApp(server)

        return new this(app, host, port)
    }

    start(): void {
        this.app.listen(this.port, this.host)
    }

    stop(): void {
        this.app.close()
        // this.io.close()
    }

    address(): string {
        return `http://${this.host}:${this.port}`
    }

    private static async createRestApp(): Promise<INestApplication> {
        const app = await NestFactory.create<NestExpressApplication>(MainModule)
        app.useGlobalPipes(new ValidationPipe())
        return app
    }
}
