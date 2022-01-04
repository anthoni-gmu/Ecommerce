import {
    GET_CATEGORY_FAIL,GET_CATEGORY_SUCCESS
} from '../actions/types'

const initialState = {
    categories:null
}
export default function Categories(state = initialState, action){
    const {type,payload}=action;

    switch (type) {
        case GET_CATEGORY_SUCCESS:
            return {
                ...state,
                categories:payload.categories
            }
        case GET_CATEGORY_FAIL:
            return {
                ...state,
                categories:null
            }
    
        default:
            return state;
    }
}
