import React from 'react'
import "./Header.css"


function Header() {
    return (
        <div className = "header">
            <div className = "header_left">
            
            <img className = "header_logo" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSX40tA7QuZSMSx4q7wHekkrWQY2OqPclSnkg&usqp=CAU" alt="" height = "20px" />
            </div>
            <div className ="header_middle">
             <input className = "text" type = "text" />
             <button className = "Submit" >Submit>>></button>
             
            </div>
            <div className = "header_right">
            <img src ="data:image/jpeg;base64,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" alt = "" height = "30px" />
            </div>
        </div>
    )
}

export default Header