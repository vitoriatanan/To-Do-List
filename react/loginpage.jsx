import React, { useState } from 'react';
import api from "./api";


function Autenticação({ onLogin }) {
  const [isLogin, setIsLogin] = useState(true); 
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");
  const [matricula, setMatricula] = useState("");

  function handleSubmit() {
    if (isLogin) {
      onLogin(usuario, password); 
    } else {
      console.log("Cadastrando com", usuario, password);
    }
  }

  return (
    <div>

      <h2>{isLogin ? "Login" : "Cadastro"}</h2>
      <input
        type="text"
        placeholder="usuario"
        value={usuario}
        onChange={(e) => setUsuario(e.target.value)}
      />

      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

<input
        type="matricula"
        placeholder="Matrícula"
        value={matricula}
        onChange={(e) => setMatricula(e.target.value)}
      />

      <button onClick={handleSubmit}>
        {isLogin ? "Entrar" : "Cadastrar"}
      </button>

      <p>
        {isLogin ? "Não tem uma conta?" : "Já tem uma conta?"}
        <button onClick={() => setIsLogin(!isLogin)}>
          {isLogin ? "Cadastre-se aqui" : "Faça login"}
        </button>
      </p>
    </div>
  );
}

export default Autenticação;
