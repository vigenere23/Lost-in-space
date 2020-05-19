import 'reflect-metadata'
import { Server } from './server'


const HOST = process.env.HOST
const PORT = Number.parseInt(process.env.PORT) || undefined

const server = new Server(HOST, PORT)

server.start()
console.log(`server running at ${server.address()}`)
