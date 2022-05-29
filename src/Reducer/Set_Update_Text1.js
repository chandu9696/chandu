const initialState = '';

const Set_Update_T1= (state = initialState, action) => {
    switch (action.type) {
        case "SET_UPDATE_TEXT1": return action.payload
        default: return state;
    }
}

export default Set_Update_T1;