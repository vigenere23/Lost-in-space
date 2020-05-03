import 'reflect-metadata'
import * as Koa from 'koa'
import * as http from 'http'
import * as socket from 'socket.io'
import { useKoaServer, useContainer as routingUseContainer } from 'routing-controllers'
import { useSocketServer, useContainer as socketUseContainer } from 'socket-controllers'
import { Container } from 'typedi'
import { InfraContext } from './context/infraContext'


function main(): void {
    const app = createRestApp()
    const server = createServer(app)
    const io = createSocketApp(server)

    registerContexts(io)
    startServer(server)
}


function createRestApp(): Koa {
    const app = new Koa()
    useKoaServer(app, {
        controllers: [__dirname + '/api/rest/*Controller.ts']
    })
    routingUseContainer(Container)

    return app
}

function createSocketApp(server: http.Server): socket.Server {
    const io = socket(server)
    useSocketServer(io, {
        controllers: [__dirname + '/api/socket/*Controller.ts']
    })
    socketUseContainer(Container)

    return io
}

function createServer(app: Koa): http.Server {
    const server = http.createServer(app.callback())

    return server
}


function registerContexts(io: socket.Server): void {
    new InfraContext(io).register()
}


function startServer(server: http.Server): void {
    const PORT: number = Number.parseInt(process.env.PORT) || 8080
    const HOST: string = process.env.HOST || '127.0.0.1'
    
    server.listen(PORT, HOST)
    
    console.log(`server running at ${HOST}:${PORT}`)
}


main()
