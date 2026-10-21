import React from 'react'
import { NavLink } from 'react-router-dom';
import {LayoutDashboard,Users,Building2,CalendarCheck,CalendarDays,ClipboardList,Settings,BriefcaseBusiness,PanelLeftClose,} from 'lucide-react'

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
  return (
    <aside className='flex flex-col shrink-0 w-64 border-r border-slate-200 bg-white h-screen '>
      <div className="flex h-20 items-center gap-3 border-b border-slate-100 px-6">
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
    </aside>
  )
}

export default Sidebar
