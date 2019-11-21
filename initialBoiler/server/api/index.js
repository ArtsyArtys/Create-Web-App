const router = require('express').Router()
module.exports = router


// example 'users' api route
// router.use('/users', require('./users'))


// 404 error handling
router.use((req, res, next) => {
  const error = new Error('Not Found')
  error.status = 404
  next(error)
})
