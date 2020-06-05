import { NestApplicationOptions } from '@nestjs/common'

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
  options: NestApplicationOptions
}
