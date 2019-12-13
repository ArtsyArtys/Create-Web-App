import React from 'react'
import ReactDOM from 'react-dom'
import {Router} from 'react-router-dom'
import history from '../client/history'
import App from '../client/App'


export default ReactDOM.render(
  <Router history={history}>
    <App />
  </Router>,
  document.getElementById('app')
)
