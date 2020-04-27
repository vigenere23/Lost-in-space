import * as Koa from 'koa'
import * as Router from 'koa-router'

const app = new Koa()
const router = new Router()

router.get('/', async (context) => {
  context.body = 'Hello world!'
})

app.use(router.routes())

const PORT = 8080
app.listen(PORT)

console.log(`server running on port ${PORT}`)
