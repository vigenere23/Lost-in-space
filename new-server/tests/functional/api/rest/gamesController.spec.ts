import { socket, api } from '../serverSetup'
import { GamesController } from '../../../../src/api/rest/gamesController'

describe(GamesController.name + ' functionnal test', () => {
    describe('list games', () => {
        test('returns a status 200', async () => {
            return api
                .get('/games/list')
                .expect(200)
        })

        test('returns an array', async () => {
            return api
                .get('/games/list')
                .then(response => {
                    expect(Array.isArray(response.body)).toBe(true)
                })
        })
    })

    describe('create game', () => {
        describe('on success', () => {
            const payload = {
                username: 'player1',
                nbPlayers: 4,
                world: 'world1'
            }

            test('returns a status 201', async () => {
                return api
                    .post('/games/create')
                    .send(payload)
                    .expect(201)
            })
        })

        describe('on failure', () => {
            const payload = {}

            test('returns a status 400', async () => {
                return api
                    .post('/games/create')
                    .send(payload)
                    .expect(400)
                    // .then(response => {
                    //     console.log(response.body)
                    // })
            })
        })
    })
})
