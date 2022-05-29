
export const incNumber = (num) => {
    return {
        type: 'INCREMENT',
        payload:num
    }
}

export const decNumber = () => {
    return {
        type: 'DECREMENT'
    }
};
export const Add = (data) => {
    return {
        type: 'ADD_LIST',
        payload:data
    }
};
export const Push = (data) => {
    return {
        type: 'ADD_LIST_Item',
        payload:data
    }
};
export const Delete = (data) => {
    return {
        type: 'Delete_LIST_Item',
        payload:data
    }
};
export const Star = (data,i) => {
    return {
        type: 'STAR',
        payload:data,
        index:i
    }
};
export const Update_Main_List = (data) => {
    return {
        type: 'UPDATE_LIST',
        payload:data
    }
};
export const FAV_ADD = (data) => {
    return {
        type: 'ADD_FAV_LIST',
        payload:data,

    }
};
export const FAV_REMOVE = (data) => {
    return {
        type: 'REMOVE_FAV_LIST',
        payload:data

    }
};
export const Set_Index = (data) => {
    return {
        type: 'SET_INDEX',
        payload:data

    }
};
export const Set_Index1 = (data) => {
    return {
        type: 'SET_INDEX1',
        payload:data

    }
};
export const Set_Update= (data) => {
    return {
        type: 'SET_UPDATE_TEXT',
        payload:data

    }
};
export const Set_Update1= (data) => {
    return {
        type: 'SET_UPDATE_TEXT1',
        payload:data

    }
};
export const Update_Main_List1 = (data) => {
    return {
        type: 'UPDATE_LIST1',
        payload:data
    }
};