import { serverSetup, socket, api } from './e2e-test'
import { AxiosResponse } from 'axios'


describe('game api', () => {
  serverSetup('/game')

  const CREATE_PAYLOAD_VALID = {username: 'a', nbPlayers: 2, world: 'a'}

  describe('when listing games', () => {
    describe('when no games were created', () => {
      test('it should return an empty array', async (done) => {
        const response = await api.get('/game')
        expect(response.status).toEqual(200)
        expect(response.data).toEqual([])
        done()
      })
    })

    describe('when games were created', () => {
      beforeEach(async (done) => {
        await api.post('/game', CREATE_PAYLOAD_VALID)
        done()
      })
      test('it should return an array of the games', async (done) => {
        const response = await api.get('/game')
        expect(response.status).toEqual(200)
        expect(response.data).not.toEqual([])
        done()
      })
    })
  })

  describe('when creating a game', () => {
    describe('when payload is invalid', () => {
      test('it should return a 400 error', async (done) => {
        try {
          await api.post('/game', {})
          fail()
        }
        catch (exception) {
          const response: AxiosResponse = exception.response
          expect(response.status).toEqual(400)
          expect(response.data).not.toBeNull()
          done()
        }
      })
    })

    describe('when game with same username already exists', () => {
      beforeEach(async (done) => {
        await api.post('/game', CREATE_PAYLOAD_VALID)
        done()
      })
      test('it returns a 500 error', async (done) => {
        try {
          await api.post('/game', CREATE_PAYLOAD_VALID)
          fail()
        }
        catch (exception) {
          const response: AxiosResponse = exception.response
          expect(response.status).toEqual(500)
          expect(response.data).not.toBeNull()
          done()
        }
      })
    })

    describe('when payload is valid', () => {
      test('it returns a 201 created response', async (done) => {
        const response = await api.post('/game', CREATE_PAYLOAD_VALID)
        expect(response.status).toEqual(201)
        expect(response.data).toEqual("")
        done()
      })
    })
  })

  describe('when updating status with invalid payload', () => {
    test('it returns an exception event', async done => {
      socket.emit('updatePlayer', 'invalid payload')
      socket.on('exception', () => {
        done()
      })
    })
  })
})
