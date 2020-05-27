import { setup, socket } from '../apiTest'


setup('/games')

describe('games api', () => {
    describe('when updating status with invalid payload', () => {
        test('it returns an exception event', async done => {
            socket.emit('updatePlayer', 'invalid payload')
            socket.on('exception', (exception: any) => {
                expect(exception.status).toEqual('error')
                done()
            })
        })
    })
})
