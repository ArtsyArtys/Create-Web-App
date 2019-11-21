import {createStore, combineReducers, applyMiddleware} from 'redux'
import {createLogger} from 'redux-logger'
import thunkMiddleware from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
import user from './user'

const reducer = combineReducers({user})

// This assumes you have redux-devtools installed as an extension.
// If you aren't using it, simply remove the compose with dev tools function wrapper
const middleware = composeWithDevTools(
  applyMiddleware(thunkMiddleware, createLogger({collapsed: true}))
)
const store = createStore(reducer, middleware)

export default store

// you can export each part of redux state so you can use functions
// from each of the files all from here.
export * from './user'
