import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import ConnectionForm from './pages/ConnectionForm'
import SchemaGraph from './pages/SchemaGraph'
import Findings from './pages/Findings'
import TableDetails from './pages/TableDetails'
import QueryLog from './pages/QueryLog'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/connection" element={<ConnectionForm />} />
        <Route path="/schema-graph" element={<SchemaGraph />} />
        <Route path="/findings" element={<Findings />} />
        <Route path="/table-details" element={<TableDetails />} />
        <Route path="/query-log" element={<QueryLog />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App