import { Config } from './config'
import { CONFIG_DEV } from './config.dev'
import { CONFIG_TEST } from './config.test'

export class ConfigProvider {
  static get(): Config {
    switch (process.env.NODE_ENV) {
      case 'development':
        return CONFIG_DEV
      case 'test':
        return CONFIG_TEST
      default:
        return CONFIG_DEV
    }
  }
}
