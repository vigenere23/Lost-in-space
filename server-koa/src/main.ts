import 'reflect-metadata'
import * as Koa from 'koa'
import * as http from 'http'
import * as socket from 'socket.io'
import { useKoaServer, useContainer as routingUseContainer } from 'routing-controllers'
import { Container } from 'typedi'

routingUseContainer(Container)

const app = new Koa()

useKoaServer(app, {
  controllers: [__dirname + '/api/rest/*Controller.ts']
})

const PORT: number = Number.parseInt(process.env.PORT) || 8080
const HOST: string = process.env.HOST || '127.0.0.1'

const server = http.createServer(app.callback())
const io = socket(server) // TODO use socket-controllers instead

server.listen(PORT, HOST)

console.log(`server running at ${HOST}:${PORT}`)
