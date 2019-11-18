const fastify = require('fastify');
const compression = require('compression');
const app = fastify({logger: true});
const PORT = 3000

// compression middleware
app.use(compression())

app.listen(PORT).then(() => {
  console.log(`Server running at http://localhost:${PORT}/`);
})
