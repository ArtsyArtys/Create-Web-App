import axios from 'axios'
import history from '../history'

// this is merely an example file for redux store showing some basic
// outlines of what you might wish to do in this file

// ACTION TYPES
const GET_USER = 'GET_USER'
const REMOVE_USER = 'REMOVE_USER'

// INITIAL STATE
const defaultUser = {}

// ACTION CREATORS
const getUser = user => ({type: GET_USER, user})
const removeUser = () => ({type: REMOVE_USER})

// THUNK CREATORS
export const getUserThunk = id => async dispatch => {
  try {
    const res = await axios.get(`/users/${id}`)
    dispatch(getUser(res.data || defaultUser))
  } catch (err) {
    console.error(err)
  }
}

// REDUCER
export default function(state = defaultUser, action) {
  switch (action.type) {
    case GET_USER:
      return action.user
    case REMOVE_USER:
      return defaultUser
    default:
      return state
  }
}
