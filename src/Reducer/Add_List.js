const initialState = [];

const changeThelist_Item = (state = initialState, action) => {
    switch (action.type) {
        case "ADD_LIST_Item": return[...state,action.payload]
        case "Delete_LIST_Item": {
            const newlist=[...state]
            newlist.splice(action.payload,1)
            return newlist;
                }
        case "UPDATE_LIST":return action.payload
        case "STAR":{
            state.splice(action.index,1)
            const newlist=[...state]
            
            return newlist;

        }
        default: return state;
    }
}

export default changeThelist_Item;