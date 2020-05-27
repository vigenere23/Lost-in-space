import { Provider as NestProvider } from '@nestjs/common'

export interface Provider<T> {
    provide(): NestProvider<T>
}
