import 'reflect-metadata'
import { NestServer } from './nestServer'


async function main() {
    const HOST = process.env.HOST
    const PORT = Number.parseInt(process.env.PORT) || undefined

    const server = await NestServer.create(HOST, PORT)

    server.start()
    console.log(`server running at ${server.address()}`)
}

main()
