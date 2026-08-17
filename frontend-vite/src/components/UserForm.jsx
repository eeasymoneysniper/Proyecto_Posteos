import React, { useState } from 'react'

export default function UserForm({ onCreate }) {
  const [nombre, setNombre] = useState('')
  const [dni, setDni] = useState('')
  const [password, setPassword] = useState('')

  function submit(e) {
    e.preventDefault()
    if (!nombre || !dni || !password) return alert('Rellena todos los campos')
    onCreate({ nombre, dni: Number(dni), password })
    setNombre(''); setDni(''); setPassword('')
  }

  return (
    <form onSubmit={submit} className="post-form">
      <h3>Crear usuario</h3>
      <input value={nombre} onChange={e => setNombre(e.target.value)} placeholder="Nombre" />
      <input value={dni} onChange={e => setDni(e.target.value)} placeholder="DNI" />
      <input value={password} onChange={e => setPassword(e.target.value)} type="password" placeholder="Password" />
      <button type="submit">Crear</button>
    </form>
  )
}
