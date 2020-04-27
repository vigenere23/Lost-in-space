import 'reflect-metadata'
import * as Koa from 'koa'
import * as Router from 'koa-router'
import * as http from 'http'
import * as socket from 'socket.io'

const app = new Koa()
const router = new Router() // TODO use routing-controllers instead

router.get('/', async (context) => {
  context.body = 'Hello world!'
})

app.use(router.routes())

const PORT: number = Number.parseInt(process.env.PORT) || 8080
const HOST: string = process.env.HOST || '127.0.0.1'

const server = http.createServer(app.callback())
const io = socket(server) // TODO use socket-controllers instead

server.listen(PORT, HOST)

console.log(`server running on port ${PORT}`)
