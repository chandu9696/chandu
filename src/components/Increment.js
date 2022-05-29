import './Increment.css'
import {useState} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import { incNumber,decNumber,Add,Push,Delete,Star, FAV_ADD, FAV_REMOVE,Set_Index,Set_Update,Update_Main_List,Set_Update1,Set_Index1,Update_Main_List1} from '../Actions/action'
//import {change}
export default function Increment()
{
   // const [value,setValue]=useState(0)
   const mystate=useSelector((state)=>state.changeTheNumber)
   const mylist=useSelector((state)=>state.changeThelist)
   const mylist_item=useSelector((state)=>state.changeThelist_Item)
   const fav_list=useSelector((state)=>state.addFav_List)
   const index=useSelector((state)=>state.Set_Index1)
   const text=useSelector((state)=>state.Set_Update_T)
   const index1=useSelector((state)=>state.Set_Index2)
   const text1=useSelector((state)=>state.Set_Update_T1)
   
    const dispatch=useDispatch();
   const renderlist=(item,i)=>{
       if(item=='')
       {
           return
       }
        return (<div key={i}>
            <h1>{item}</h1>
            {console.log(item)}
            <button  onClick={()=>{
                     dispatch(Set_Index(i))
                     dispatch(Set_Update(item))
                     console.log('update call')
                 }
             }>update</button>
            <button onClick={()=>
            {
                dispatch(Delete(i))
            }}>Delete</button>
             <button onClick={()=>
            {
                dispatch(FAV_ADD(item))
                dispatch(Star(item,i))
               
            }}>Star</button>
            </div>)

    }
    function renderfav(item,i)
    {
       
         return (<div key={i}>
             <h1>{item}</h1>
             {console.log(item)}
             <button onClick={()=>{
                     dispatch(Set_Index1(i))
                     dispatch(Set_Update1(item))
                     console.log('update call')
                 }}>update</button>
             <button onClick={()=>
             {
                 dispatch(FAV_REMOVE(i))
             }}>Delete</button>
              <button disabled={fav_list.indexOf(item)!=-1?true:false}onClick={()=>
             {
                 dispatch(FAV_ADD(item))
                 dispatch(Star(item,i))
                
             }}>Star</button>
             </div>)
    }
    function onupdate(item,i)
    {
        const newlist=[...mylist_item]
        newlist[i]=item;
        dispatch(Update_Main_List(newlist))
        dispatch(Set_Update(''))
        dispatch(Set_Index(null))

    }
    function onupdate1(item,i)
    {
        const newlist=[...fav_list]
        newlist[i]=item;
        dispatch(Update_Main_List1(newlist))
        dispatch(Set_Update1(''))
        dispatch(Set_Index1(null))

    }
    function updatelist(i)
    {
        return(
            <div key={i}>
         <input type='text' value={text} onChange={(e)=>dispatch(Set_Update(e.target.value))}></input>
        <button onClick={()=>onupdate(text,i)}>done</button> 
        </div>)
    }
    function updatelist1(i)
    {
        return(
            <div key={i}>
         <input type='text' value={text1} onChange={(e)=>dispatch(Set_Update1(e.target.value))}></input>
        <button onClick={()=>onupdate1(text1,i)}>done</button> 
        </div>)

    }
    return(
        <div>
            <h1>This is increment Operator</h1>
            <div className='content'>
                <button onClick={()=>
                dispatch(incNumber(5)) }>+</button>
                <p>{mystate}</p>
                <button onClick={()=>
                dispatch(decNumber()) }>-</button>
                <input type='text' onChange={(e)=>dispatch(Add(e.target.value))}></input>
                <button onClick={()=>{
                    dispatch(Push(mylist))
                }}>Add</button>

               
            </div>
            {fav_list.map((item,i)=>index1==i?updatelist1(i):renderfav(item,i))}
            {mylist_item.map((item,i)=>index==i?updatelist(i):renderlist(item,i))}
        </div>
    )
}