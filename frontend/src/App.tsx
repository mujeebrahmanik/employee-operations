
import './App.css'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import DashboardLayout from './components/layout/DashboardLayout'
import HomePage from './components/pages/HomePage'

function App() {
 
  return (
    <>
    <BrowserRouter>
    <Routes>
      <Route element={<DashboardLayout/>} >
        <Route path='/' element={<HomePage/>} />
      </Route>
    </Routes>
    </BrowserRouter>
      
    </>
  )
}

export default App
