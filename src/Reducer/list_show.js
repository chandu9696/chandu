const initialState = '';

const changeThelist = (state = initialState, action) => {
    switch (action.type) {
        case "ADD_LIST": return action.payload;
        default: return state;
    }
}

export default changeThelist;