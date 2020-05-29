import 'reflect-metadata'
import { NestFactory } from '@nestjs/core'
import { INestApplication, ValidationPipe } from '@nestjs/common'
import { NestExpressApplication } from '@nestjs/platform-express'
import { AppModule } from './app.module'


export class NestServer {
    constructor(
        private app: INestApplication,
        readonly host: string = '127.0.0.1',
        readonly port: number = 8080
    ) {}

    // TODO add config for adresses
    static async create(host = '127.0.0.1', port = 8080): Promise<NestServer> {
        const app = await this.createRestApp()

        return new this(app, host, port)
    }

    start(): void {
        this.app.listen(this.port, this.host)
    }

    stop(): void {
        this.app.close()
    }

    address(): string {
        return `http://${this.host}:${this.port}`
    }

    private static async createRestApp(): Promise<INestApplication> {
        const app = await NestFactory.create<NestExpressApplication>(AppModule)
        app.useGlobalPipes(new ValidationPipe())
        return app
    }
}
