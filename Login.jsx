import React from 'react'
import {FaAddressCard,FaLock, FaLaptopCode} from "react-icons/fa";  
import { useState } from 'react';


const Login = () => {

  const [username,setUsername] =useState("");  
  const [password,setPassword] =useState(""); 

  const handleSubmit=(event)=>{               // lidar com login
    event.preventDefault();                   // n lembro mas tem a ver com recarregar pg e salvar informações de cadastro
    console.log("Envio");                     // mandar informações
    alert("Salvando usuário"+username+"-"+password) // recado de cadastro
  };

  return(
  <div className="container">
      <form onSubmit={handleSubmit}></form>    {/* lidar com submissoes */}
        <form>
            <h1>Acesse o sistema <FaLaptopCode className='Laptop'/></h1>
            <div>
                <input type="matrícula" placeholder='matrícula' onChange={(e)=>setUsername(e.target.value)}/> {/* pegar matricula */}
                <FaAddressCard className='AdressedCard'/> {/* icon */}
            </div>
            
            <div>
                <input type="password" placeholder='Senha' onChange={(e)=>setPassword(e.target.value)}/>  {/* pegar senha */}
                <FaLock className='Lock'/>  {/* icon */}
            </div>

            <div className='recall-forget'>
              <label>
                <input type='checkbox'/>
                Lembre de mim                     {/* caixa de salvar user*/}
              </label>
            </div>

            <div className="singup-link"></div>
              <p>Não tem uma conta?               {/* "redirecionamento"*/}
                <a href='#'>Cadastrar </a>
              </p>



            <button>Entrar</button>
        </form>
    </div>
  )
}

export default Login

