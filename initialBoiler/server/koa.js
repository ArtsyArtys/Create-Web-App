const Koa = require('koa')
const Router = require('koa-router')
const logger = require('koa-logger')
const app = new Koa()
const router = new Router()
const PORT = process.env.PORT || 1234

app.use(logger())

function requestBodyJson(req) {
  return new Promise((resolve, reject) => {
    let body = ''

    req.on('data', (data) => {
      // This function is called as chunks of body are received
      body += data
    })

    req.on('end', () => {
      // This function is called once the body has been fully received
      let parsed

// Example route:

// router.post('/user', async (ctx) => {
//   try {
//     const parsed = await requestBodyJson(ctx.req)
//     ctx.body = {
//       error: false,
//       username: parsed.username
//     }
//   } catch (e) {
//     ctx.status = 400
//     ctx.body = {
//       error: 'CANNOT_PARSE'
//     }
//   }
// })

app.use(router.routes())
app.listen(PORT)
