import React from 'react'
import {FaUser,FaLock, FaAddressCard,} from "react-icons/fa";

const cadastro = () => {
  return (
    <div className="container">
        <form>
            <h1>Entre no sistema</h1>
            <div>
                <input type="nome" placeholder='nome' />
                <FaUser className='User'/>
            </div>
            <div>
                <input type="matrícula" placeholder='matrícula'/>
                <FaAddressCard className='AdressedCard'/>
            </div>
            <div>
                <input type="password" placeholder='Senha' />
                <FaLock className='Lock'/>
            </div>
            
            <button>Cadastrar</button>
        </form>
    </div>
  )
}

export default cadastro