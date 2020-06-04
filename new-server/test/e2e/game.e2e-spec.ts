import { serverSetup, socket, api } from './e2e-test'
import { AxiosResponse } from 'axios'

describe('game api', () => {
  serverSetup('/game')

  const CREATE_PAYLOAD_VALID = { username: 'a', nbPlayers: 2, world: 'any' }
  const JOIN_PAYLOAD_VALID = { username: 'b', gameId: 'a', socketId: 'any' }

  describe('when listing games', () => {
    describe('when no games were created', () => {
      it('should return an empty array', async done => {
        const response = await api.get('/game')
        expect(response.status).toEqual(200)
        expect(response.data).toEqual([])
        done()
      })
    })

    describe('when games were created', () => {
      beforeEach(async done => {
        await api.post('/game', CREATE_PAYLOAD_VALID)
        done()
      })
      it('should return an array of the games', async done => {
        const response = await api.get('/game')
        expect(response.status).toEqual(200)
        expect(response.data).not.toEqual([])
        expect(response.data).toHaveLength(1)
        done()
      })
    })
  })

  describe('when creating a game', () => {
    describe('when payload is invalid', () => {
      it('should return a 400 error', async done => {
        try {
          await api.post('/game', {})
          done(fail('an error 400 should be returned'))
        } catch (exception) {
          const response: AxiosResponse = exception.response
          expect(response.status).toEqual(400)
          expect(response.data).not.toBeNull()
          done()
        }
      })
    })

    describe('when game with same username already exists', () => {
      beforeEach(async done => {
        await api.post('/game', CREATE_PAYLOAD_VALID)
        done()
      })
      it('should return a 500 error', async done => {
        try {
          await api.post('/game', CREATE_PAYLOAD_VALID)
          done(fail('an error 500 should be returned'))
        } catch (exception) {
          const response: AxiosResponse = exception.response
          expect(response.status).toEqual(500)
          expect(response.data).not.toBeNull()
          done()
        }
      })
    })

    describe('when payload is valid', () => {
      it('should return a 201 created response', async done => {
        const response = await api.post('/game', CREATE_PAYLOAD_VALID)
        expect(response.status).toEqual(201)
        expect(response.data).toEqual('')
        done()
      })
    })
  })

  describe('when joining game', () => {
    describe('when payload is invalid', () => {
      it('should return a 400 error', async done => {
        try {
          await api.post('/game/join', {})
          done(fail('an error 400 should be returned'))
        } catch (exception) {
          const response: AxiosResponse = exception.response
          expect(response.status).toEqual(400)
          expect(response.data).not.toBeNull()
          done()
        }
      })
    })

    describe('when game to join does not exist', () => {
      it('should return an error 500', async done => {
        try {
          await api.post('/game/join', JOIN_PAYLOAD_VALID)
          done(fail('an error 500 should be returned'))
        } catch (exception) {
          const response: AxiosResponse = exception.response
          expect(response.status).toEqual(500)
          expect(response.data).not.toBeNull()
          done()
        }
      })
    })

    describe('when game to join exists', () => {
      beforeEach(async done => {
        await api.post('/game', CREATE_PAYLOAD_VALID)
        done()
      })

      // TODO
      // describe('when username is already taken', () => {
      //   const payload = JOIN_PAYLOAD_VALID
      //   payload.username = payload.gameId

      //   it('should return an error 500', async done => {
      //     try {
      //       await api.post('/game/join', payload)
      //       done(fail('an error 500 should be returned'))
      //     } catch (exception) {
      //       const response: AxiosResponse = exception.response
      //       expect(response.status).toEqual(500)
      //       expect(response.data).not.toBeNull()
      //       done()
      //     }
      //   })
      // })

      describe('when username is ok', () => {
        it('should return a status 200', async done => {
          const response = await api.post('/game/join', JOIN_PAYLOAD_VALID)
          expect(response.status).toEqual(200)
          expect(response.data).toEqual('')
          done()
        })
      })
    })
  })

  describe('when updating status', () => {
    describe('when payload is invalid', () => {
      it('should return an exception event', async done => {
        socket.emit('updatePlayer', 'invalid payload')
        socket.on('exception', () => {
          done()
        })
      })
    })

    describe('when game has not started', () => {
      it.todo('should return an error 403')
    })

    describe('when game has started', () => {
      it.todo('should send the updated info to other players')
    })
  })
})
