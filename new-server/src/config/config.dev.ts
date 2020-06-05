import { Config } from './config'

export const CONFIG_DEV: Config = {
  nest: {
    port: 8080,
    host: '127.0.0.1',
    options: {
      logger: ['error', 'warn']
    }
  },
  socket: {
    port: 8080
  }
}
