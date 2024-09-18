import React,{UseState} from 'react'

import  Autenticação from './loginpage';

Autenticação();

function ToDoList(){

    const [tarefas,setarTarefas] =UseState([]);
    const [novaTarefa,setarNovaTarefa]=UseState("");

    function mudançasDeEntrada(event){
        setarNovaTarefa(event.target.value);
    }
    function adicionarTarefa(){
        setarTarefas([...tarefas, novaTarefa]); 
        setarNovaTarefa(""); 
    }
    
    function deletarTarefa(index){
        const novasTarefas = [...tarefas];
        novasTarefas.splice(index, 1);
        setTarefas(novasTarefas);
    }

    
    return (
    <div className="To-do-list">
        <h1>To-Do-List</h1>
        <div>
            <input
            type="text"
            placeholder="Entre com a tarefa:"
            value={novaTarefa}
            onChange={mudançasDeEntrada}
        />
        
        <buttom className="botãoRemover"> onClick={deletarTarefa} Remover Tarefa </buttom>
        <button className='botaoAdd' onClick={adicionarTarefa}>Adicionar Tarefa</button>
        

        </div>
        <ol>
            {tarefas.map((tarefas,index)=>(
            <li>
                key={index}
                <span className="text">{tarefa}</span>
                <button onClick={() =>
                 deletarTarefa(index)}
                 >Deletar
                 </button>
            </li>            
            ))}
        </ol>
        
        <ol>
            {tarefas.map((tarefa,index)=>(
            <li>
                key={index}
                <span className="text">{tarefas}</span>
                <button onClick={() =>adicionarTarefa(index)}>Adicionar</button>
            </li>            
            ))}
        </ol>
        
    
        </div>
    );
    
}
    
export default ToDoList