const initialState = [];

const addFav_List = (state = initialState, action) => {
    switch (action.type) {
        case "ADD_FAV_LIST": return[...state,action.payload]
        case "UPDATE_LIST1":return action.payload
        case "REMOVE_FAV_LIST": {
            state.splice(action.payload,1)
            const newlist=[...state]
            return newlist;
        }
        default: return state;
    }
}

export default addFav_List;