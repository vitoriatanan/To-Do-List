import './App.css'
import Login from './Components/Login/Login';
import cadastro from './Components/Login/cadastro';   
import { useState } from 'react';


function App() {
  
  const [mostrarCadastro, setMostrarCadastro] = useState(false);
  return (
    <div className="App">
      <Login />
      
      
      {mostrarCadastro ? <Cadastro /> : <Login />}
      
      {/* Botão para alternar entre Login e Cadastro */}
      <button onClick={() => setMostrarCadastro(!mostrarCadastro)}>
        {mostrarCadastro ? "Ir para Login" : "Ir para Cadastro"}
      </button>
    </div>
  );
}

export default App;

 

  