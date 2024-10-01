import './App.css';
import Login from './Components/Login/Login';
import Cadastro from './Components/Login/cadastro';  // Renomear para Cadastro
import { useState } from 'react';

function App() {
  const [mostrarCadastro, setMostrarCadastro] = useState(false);
  
  return (
    <div className="App">
      {mostrarCadastro ? <Cadastro /> : <Login />}  {/* Usar Cadastro no JSX */}
      
      <button onClick={() => setMostrarCadastro(!mostrarCadastro)}>
        {mostrarCadastro ? "Ir para Login" : "Ir para Cadastro"}
      </button>
    </div>
  );
}

export default App;
