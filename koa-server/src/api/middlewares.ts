import * as Koa from 'koa'
import { KoaMiddlewareInterface } from 'routing-controllers'
import { ArgumentError } from '../domain/exceptions'

export class ErrorMapping implements KoaMiddlewareInterface {
    async use(context: Koa.Context, next: (err?: any) => Promise<any>): Promise<any> {
        // try {
        //     await next()
        // }
        // catch (error) {
        //     if (error instanceof ArgumentError) {
        //         const message = `${error.name}: ${error.message}`
        //         context.status = 400
        //         context.body = { error: message }
        //     }
        // }
        return await next()
    }
}
