import React, {useState, useEffect} from 'react'
import axios from  'axios'
import './App.css'
import AddTask from './components/AddTask/AddTask'
import List from './components/List/List'

function App() {


    const[todos, setTodos] = useState([])

    const fetchTasks = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/v1/users/1/tarefas/')
            setTodos(response.data)
        } catch (error) {
            console.error('Erro ao buscar tarefas: ', error)
        }
    }

    // Adiciona uma nova tarefa na lista
    const onAddTask = async (value) => { 
        const response = await axios.post('http://127.0.0.1:8000/api/v1/users/1/tarefas/', {
            description: value,
        });

        setTodos([...todos, response.data]); // Atualiza a lista de tarefas com a nova tarefa

    };


    // risca a tarefa como concluída 
    const onToggle = (todo) => {
        setTodos (
            todos.map((obj) => obj.id === todo.id ? {...obj, checked: !todo.checked} : obj)
        )
    }

    // remover tarefa ao clicar no icone da lixeira
    const onRemove = (todo) => {
        setTodos(todos.filter((item) => item.id !== todo.id));
        } 


    useEffect(() => {
        fetchTasks(); // Chamando a função para buscar tarefas ao montar o componente
    }, []);
    

  return (

    <div>
        <nav className='navbar'>
            <h2>To-do-List</h2>
        </nav>

        <section id='app' className='container'>
            <header>
                <h1 className='title'>Suas Tarefas!</h1>
            </header>
            <div className='main'>
                <AddTask onAddTask={onAddTask} />
                <List todos={todos} onRemove={onRemove} onToggle={onToggle} />
            </div>
        </section>

    </div>
  )
}


export default App
