const initialState=null;

const Set_Index1= (state = initialState, action) => {
    switch (action.type) {
        case "SET_INDEX": { console.log(action.payload)
            return action.payload}
        default: return state;
    }
}

export default Set_Index1;