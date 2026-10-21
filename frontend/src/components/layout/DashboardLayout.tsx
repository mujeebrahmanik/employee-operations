import React from 'react'
import Sidebar from './Sidebar'
import { Outlet } from 'react-router-dom'

const DashboardLayout = () => {
  return (
    <div className='flex min-h-screen bg-slate-50'>
      <Sidebar/>
      <main className="min-w-0 flex-1">
        <Outlet/>
      </main>
    </div>
  )
}

export default DashboardLayout
