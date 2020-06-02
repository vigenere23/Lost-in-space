import 'reflect-metadata'
import { NestServer } from './nest-server'
import { ConfigProvider } from './config/config.provider'

async function main() {
  const server = await NestServer.create(ConfigProvider.get())

  server.start()
  console.log(`server running at ${server.address()}`)
}

main()
