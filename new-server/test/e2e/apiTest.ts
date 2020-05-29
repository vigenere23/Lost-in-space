import  * as io from 'socket.io-client';
import { NestServer } from '../../src/nest-server';

let server: NestServer
export let socket: SocketIOClient.Socket

export function setup(socketNamespace: string): void {
    beforeAll(async done => {
        // TODO load config for host, port and logger
        server = await NestServer.create()
        server.start()
        done()
    })
    
    afterAll(() => {
        server.stop()
    })
    
    beforeEach(done => {
        socket = io.connect(server.address() + socketNamespace)
        socket.on('connect', () => {
            done()
        })
    })
    
    afterEach(() => {
        if (socket.connected) {
            socket.disconnect()
        }
    })
}
