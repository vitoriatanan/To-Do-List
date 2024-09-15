import React,{UseState} from 'react'
function ToDoList(){

    const [tarefas,setarTarefas] =UseState([]);
    const [novaTarefa,setarNovaTarefa]=UseState("");

    function mudançasDeEntrada(event){
        setarNovaTarefa(event.target.value);
    }
    function adicionarTarefa(){

    }
    function deletarTarefa(index){

    }
    function cadastroUser(index){

    }
    function LoginUser(index){

    }
    function cadastroAdm(index){

    }
    function LoginAdm(index){

    }

    
    return (<div className="To-do-list">
        <h1>To-Do-List</h1>
        <div>
            <input
            type="text"
            placeholder="Entre com a tarefa:"
            value={novaTarefa}
            onChange={mudançasDeEntrada}
        />


        <buttom
            className="botãoadmlogin">
            onClick={LoginAdm}   
            Login de administrador
        </buttom>

        <buttom
            className="botãoadmcadastro">
            onClick={cadastroAdm}   
            Cadastro de administrador
        </buttom>

        <buttom
            className="botãouserlogin">
            onClick={LoginUser}   
            Login de usuário
        </buttom>

        <buttom
            className="botãousercadastro">
            onClick={cadastroUser}   
            Cadastro de usuário
        </buttom>
        

        <buttom
            className="botãoAdd"
            onClick={adicionarTarefa}
            Adicionar Tarefa>
        </buttom>
        
        <buttom
            className="botãoRemover">
            onClick={deletarTarefa}   
            Remover Tarefa
        </buttom>
        

        </div>
        <ol>
            {tasks.map((tarefas,index)=>
            <li>
                key={index}
                <span className="text">{task}</span>
                <button>
                    className="botaodeDeletar"
                    onClick={()=>deletarTarefa(index)}
                    Deletar
                </button>
            </li>            
            )}
        </ol>

    </div>);

}
    
export default ToDoList