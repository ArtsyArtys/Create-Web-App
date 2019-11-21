const fastify = require('fastify')
const static = require('fastify-static')
const compression = require('compression')
const app = fastify({logger: {prettyPrint: true}})
const PORT = process.env.PORT || 1234

// compression middleware
app.use(compression())

// static file serving middleware
app.register(require('fastify-static'), {
  root: path.join(__dirname, 'public'),
  prefix: '/public/'
})

app.listen(PORT, process.env.IP || '127.0.0.1', (err) => {
  if (err) {
    app.log.error(err)
    process.exit(1)
  }
})
