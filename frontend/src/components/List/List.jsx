import React from 'react'
import PropTypes from 'prop-types'
import { MdDelete } from 'react-icons/md'
import './List.css'

function List({todos, onRemove, onToggle}) {
  console.log('Tarefas passadas para o componente List:', todos); // Verifica se está recebendo os dados
  return (
    <ul className='todo-list'>
        {todos.map((item) => (
            <li key={item.id}>
            <span
                onClick={() => onToggle(item)}
                className={item.checked ? 'checked' : ''}
            >{item.description}</span>
            <button
                type='button'
                onClick={() => onRemove(item)}
            >
                <MdDelete size={24} />
            </button>
        </li>
        ))}
    </ul>
  );
}



  const onRemove = (todo) => {
    setTodos(todos.filter((item) => item.id !== todo.id));
  }
  

List.PropTypes = {
    todos: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            description: PropTypes.string.isRequired,
            checked: PropTypes.bool.isRequired
        })
    ).isRequired,
    onToggle: PropTypes.func.isRequired,
    onRemove: PropTypes.func.isRequired
}

export default List
