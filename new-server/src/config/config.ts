export interface Config {
  socket: SocketConfig
  nest: NestConfig
}

interface SocketConfig {
  port: number
}

interface NestConfig {
  host: string
  port: number
  logger: boolean
}
