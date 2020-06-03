import * as io from 'socket.io-client'
import axios, { AxiosInstance } from 'axios'
import { NestServer } from '../../src/nest-server'
import { ConfigProvider } from '../../src/config/config.provider'

let server: NestServer
export let api: AxiosInstance
export let socket: SocketIOClient.Socket

export function serverSetup(socketNamespace?: string): void {
  beforeEach(async done => {
    server = await NestServer.create(ConfigProvider.get())
    api = axios.create({
      baseURL: server.address()
    })
    server.start()

    if (socketNamespace) {
      socket = io.connect(server.address() + socketNamespace)
      socket.on('connect', () => {
        done()
      })
    } else {
      done()
    }
  })

  afterEach(() => {
    if (socket && socket.connected) {
      socket.disconnect()
    }
    server.stop()
  })
}
