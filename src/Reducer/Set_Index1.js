const initialState=null;

const Set_Index2= (state = initialState, action) => {
    switch (action.type) {
        case "SET_INDEX1": { console.log(action.payload)
            return action.payload}
        default: return state;
    }
}

export default Set_Index2;