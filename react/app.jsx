import React, { useState } from 'react';
import ToDoList from './ToDoList';
import Autenticação from '../loginpage';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  function handleLogin(email, password) {
    if (email === "admin@teste.com" && password === "1234") {
      setIsAuthenticated(true);
    } else {
      console.log("Credenciais incorretas");
    }
  }

  return (
    <div>
      {!isAuthenticated ? (
        <Autenticação onLogin={handleLogin} />
      ) : (
        <ToDoList />
      )}
    </div>
  );
}

export default App;
