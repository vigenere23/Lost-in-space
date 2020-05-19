import 'reflect-metadata'
import * as Koa from 'koa'
import * as cors from '@koa/cors'
import * as http from 'http'
import * as socketIO from 'socket.io'
import { useKoaServer, useContainer as routingUseContainer } from 'routing-controllers'
import { useSocketServer, useContainer as socketUseContainer } from 'socket-controllers'
import { Container } from 'typedi'
import { InfraContext } from './context/infraContext'


export class Server {
    private app: Koa
    private io: socketIO.Server
    private server: http.Server

    constructor(
        readonly host: string = '127.0.0.1',
        readonly port: number = 8080
    ) {
        this.app = this.createRestApp()
        this.server = this.createServer(this.app)
        this.io = this.createSocketApp(this.server)

        this.registerContexts(this.io)
    }

    start(): void {
        this.server.listen(this.port, this.host)
    }

    stop(): void {
        this.app.removeAllListeners()
        this.server.close()
        this.io.close()
    }

    address(): string {
        return `http://${this.host}:${this.port}`
    }

    private createRestApp(): Koa {
        const app = new Koa()
        app.use(cors())
    
        useKoaServer(app, {
            controllers: [__dirname + '/api/rest/*Controller.ts'],
            defaultErrorHandler: false
        })
        routingUseContainer(Container)
    
        return app
    }

    private createServer(app: Koa): http.Server {
        const server = http.createServer(app.callback())
    
        return server
    }
    
    private createSocketApp(server: http.Server): socketIO.Server {
        const io = socketIO(server, { origins: '*:*' })
        useSocketServer(io, {
            controllers: [__dirname + '/api/socket/*Controller.ts']
        })
        socketUseContainer(Container)
    
        return io
    }

    private registerContexts(io: socketIO.Server): void {
        new InfraContext(io).register()
    }
}
