
import changeTheNumber from "./updown";

import { combineReducers } from "redux";
import changeThelist from "./list_show";
import changeThelist_Item from "./Add_List";
import addFav_List from "./Fav_List";
import Set_Index1 from "./Set_Index";
import Set_Update_T from "./Set_Update_Text";
import Set_Index2 from "./Set_Index1";
import Set_Update_T1 from "./Set_Update_Text1";
const reducers = combineReducers(
    {
    //   myNumber:changeTheNumber
        changeTheNumber,
        changeThelist,changeThelist_Item,addFav_List,Set_Index1,Set_Update_T,Set_Index2,Set_Update_T1
    }
);

export default reducers;