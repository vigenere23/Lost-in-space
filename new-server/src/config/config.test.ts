import { Config } from './config'

export const CONFIG_TEST: Config = {
  nest: {
    port: 8080,
    host: 'localhost',
    options: {
      logger: false // ['error']
    }
  },
  socket: {
    port: 8080
  }
}
