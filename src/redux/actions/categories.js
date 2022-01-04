import {
    GET_CATEGORY_FAIL,GET_CATEGORY_SUCCESS
} from './types'
import axios from 'axios'

export const get_categories =() => async dispatch =>{
    
   
    const config ={
        headers:{
            'content-type': 'application/json'
        }

    };

    try{
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/category/categories`,config)

        if (res.status===200){
            dispatch({
                type: GET_CATEGORY_SUCCESS,
                payload: res.data
            });

        }else{
            dispatch({
                type: GET_CATEGORY_FAIL,
            });

        }
    }
    catch (err){
        dispatch({
            type: GET_CATEGORY_FAIL,
        });
      
    }

};
