import * as io from 'socket.io-client'
import * as supertest from 'supertest'
import { Server } from '../../../src/server'


let socket: SocketIOClient.Socket
// const server = new Server()
const address = 'http://localhost:8080'

// beforeAll(() => {
//     server.start()
// })

// afterAll(() => {
//     server.stop()
// })

beforeEach(done => {
    // socket = io.connect(server.address())
    socket = io.connect(address)

    socket.on('connect', () => {
        done()
    })
})

afterEach(() => {
    if (socket.connected) {
        socket.close()
    }
})

// const api = supertest(server.address())
const api = supertest(address)


export {
    socket,
    api
}
