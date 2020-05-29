import { setup, socket } from './apiTest';

setup('/game')

describe('game api', () => {
    describe('when updating status with invalid payload', () => {
        test('it returns an exception event', async done => {
            socket.emit('updatePlayer', 'invalid payload')
            socket.on('exception', (exception: any) => {
                done()
            })
        })
    })
})
