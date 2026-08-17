import React from 'react'

export default function UsersList({ users = [], onDelete, onOpenLanguages }) {
  if (!users.length) return <p>No hay usuarios aún.</p>

  return (
    <ul className="post-list">
      {users.map(u => (
        <li key={u.user_id} className="post-item">
          <div className="post-header">
            <strong>{u.nombre} (DNI: {u.dni})</strong>
            <div style={{display:'flex',gap:8}}>
              <button onClick={() => onOpenLanguages(u)}>Lenguajes</button>
              <button onClick={() => onDelete(u.user_id)}>Eliminar</button>
            </div>
          </div>
          <small>Creado: {u.created_at ? new Date(u.created_at).toLocaleString() : '—'}</small>
        </li>
      ))}
    </ul>
  )
}
