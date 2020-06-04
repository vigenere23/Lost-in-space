import 'reflect-metadata'
import { NestFactory } from '@nestjs/core'
import { INestApplication, ValidationPipe } from '@nestjs/common'
import { NestExpressApplication } from '@nestjs/platform-express'
import { AppModule } from './app.module'
import { Config } from './config/config'

export class NestServer {
  constructor(readonly app: INestApplication, private config: Config) {}

  static async create(config: Config): Promise<NestServer> {
    const app = await this.createRestApp(config)

    return new this(app, config)
  }

  start(): void {
    this.app.listen(this.config.nest.port, this.config.nest.host)
  }

  stop(): void {
    this.app.close()
  }

  address(): string {
    return `http://${this.config.nest.host}:${this.config.nest.port}`
  }

  private static async createRestApp(
    config: Config
  ): Promise<INestApplication> {
    const nestServerConfig = { logger: config.nest.logger }
    const app = await NestFactory.create<NestExpressApplication>(
      AppModule,
      nestServerConfig
    )
    app.useGlobalPipes(new ValidationPipe())
    return app
  }
}
