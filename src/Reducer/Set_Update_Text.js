const initialState = '';

const Set_Update_T= (state = initialState, action) => {
    switch (action.type) {
        case "SET_UPDATE_TEXT": return action.payload
        default: return state;
    }
}

export default Set_Update_T;