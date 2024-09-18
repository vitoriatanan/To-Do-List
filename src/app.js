import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginPage from './loginpage';
import ToDoList from './ToDoList';


function PrivateRoute({ children }) {
  const token = localStorage.getItem('token');
  return token ? children : <Navigate to="/login" />;
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/tarefas"
          element={
            <PrivateRoute>
              <ToDoList />
            </PrivateRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;

