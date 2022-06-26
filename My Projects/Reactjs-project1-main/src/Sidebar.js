import React from 'react'
import './Sidebar';
import SidebarRow from './SidebarRow'
import HomeIcon from '@material-ui/icons/Home';
import GroupIcon from '@material-ui/icons/Group';
import PaymentIcon from '@material-ui/icons/Payment';

function Sidebar() {
    return (
        <div className = "sidebar">
         <SidebarRow Icon = {HomeIcon} title="Add Keywords" /> 
         <SidebarRow Icon = {GroupIcon} title="Matches" /> 
         <SidebarRow Icon = {PaymentIcon} title="Manage sources" />
          <SidebarRow Icon = {PaymentIcon} title="Integration " /> 
          <SidebarRow Icon = {PaymentIcon} title="Alerts" /> 
        </div>
    )
}

export default Sidebar
