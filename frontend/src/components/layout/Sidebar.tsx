import React from 'react'
import { NavLink } from 'react-router-dom';
import {LayoutDashboard,Users,Building2,CalendarCheck,CalendarDays,ClipboardList,Settings,BriefcaseBusiness,PanelLeftClose,} from 'lucide-react'
import { useState  } from 'react';
import { Menu } from 'lucide-react';


const navItems = [
    {
        label:'dashborad',
        path:'/',
        icon:LayoutDashboard
    },
    {
        label:'employees',
        path:'/employees',
        icon:Users
    },
    {
        label: "Departments",
        path: "/departments",
        icon: Building2,
    },
    {
        label: "Attendance",
        path: "/attendance",
        icon: CalendarCheck,
    },
    {
        label: "Leave Requests",
        path: "/leaves",
        icon: CalendarDays,
    },
    {
        label: "Tasks",
        path: "/tasks",
        icon: ClipboardList,
    },
]

const Sidebar = () => {
    const [collapsed,setCollapsed] = useState(false)
  return (
    <aside className={`flex flex-col shrink-0  border-r border-slate-200 bg-white h-screen ${collapsed ? 'w-[72px]':'w-64'}`}>
     
            
                 <div className={`flex h-20 items-center gap-3 border-b border-slate-100 ${collapsed ? 'justify-center px-2':'justify-between px-4'}`}>
                    {!collapsed && (
                        <div className="flex items-center gap-3">
                            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-indigo-600 text-white">
                            <BriefcaseBusiness size={22} />
                            </div>

                            <div>
                                <h1 className="text-lg font-bold tracking-tight text-slate-900">
                                    WorkFlow
                                </h1>
                                <p className="text-xs text-slate-500">Employee Operations</p>
                            </div>
                        </div>
                
                        )}

                <button
                type='button'
                onClick={()=>setCollapsed((current)=>!current)}
                className='rounded-lg cursor-pointer p-2 text-slate-500 hover:bg-slate-100 hover:text-slate-900'
                aria-label={collapsed ? 'Expand sidebar':'Collapse sidebar'}
                >
                    <Menu size={20}/>
                </button>

            </div>

            
            

        {/* navigation */}
        <nav className="flex-1 space-y-1 overflow-auto px-4 py-6">
           {!collapsed && (
             <p className="mb-3 text-xs font-semibold uppercase tracking-wider px-6">
                workspace
            </p>
           )}

            {navItems.map((i)=>{
                const Icon = i.icon;
                return(
                    <NavLink
                        key={i.path}
                        to={i.path}
                        end={i.path === '/'}
                        title={collapsed ? i.label :undefined}
                        className={({isActive})=>`flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium
                        transition-colors ${isActive ? 'bg-indigo-50 text-indigo-700'
                            : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900'
                        }`}
                    >
                        <Icon size={19} strokeWidth={1.8}/>
                        {!collapsed && <span className='capitalize'>{i.label}</span>}
                    </NavLink>
                )
            })}
        </nav>

        {/* bottom navigation */}

        <div className="border-t border-slate-100 p-4">
            <NavLink
                to='/settings'
                title={collapsed ? 'settings' :undefined}
                className={({ isActive }) =>
                `flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-colors ${
                isActive
                    ? "bg-indigo-50 text-indigo-700"
                    : "text-slate-600 hover:bg-slate-50 hover:text-slate-900"
                }`}>
                <Settings size={19} strokeWidth={1-8}/>
                {!collapsed && <span>Settings</span>}

            </NavLink>
            <div className={`flex items-center mt-4 rounded-lg bg-slate-50 p-3 ${collapsed ? 'justify-center px-0 flex-col gap-2' :'gap-3'}`}>
                <div className="flex h-9 w-9 rounded-full bg-indigo-100 items-center justify-center text-sm font-semibold text-indigo-700">A</div>
                {!collapsed && (
                    <div className="min-w-0 flex-1">
                    <p className="truncate text-sm font-semibold text-slate 800">Admin User</p>
                    <span className="text-xs text-slate-500">Admininstrator</span>
                </div>
                )}
                <PanelLeftClose size={17} className='text-slate-400'/>
            </div>
        </div>
    </aside>
  )
}

export default Sidebar
