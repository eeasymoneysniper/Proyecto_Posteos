import React, { useEffect, useState } from 'react'

export default function LanguagesModal({ apiBase, token, user, onClose }) {
  const [languages, setLanguages] = useState([])
  const [newLang, setNewLang] = useState('')

  async function fetchLanguages() {
    try {
      const res = await fetch(`${apiBase}/usuarios/${user.user_id}/lenguajes`)
      if (!res.ok) throw new Error('Error al obtener lenguajes')
      const data = await res.json()
      setLanguages(data)
    } catch (err) {
      alert(err.message)
    }
  }

  useEffect(() => { fetchLanguages() }, [])

  async function addLanguage() {
    if (!newLang.trim()) return
    try {
      const res = await fetch(`${apiBase}/usuarios/${user.user_id}/lenguajes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', ...(token ? { Authorization: `Bearer ${token}` } : {}) },
        body: JSON.stringify({ lenguaje: newLang })
      })
      if (!res.ok) {
        const txt = await res.text()
        throw new Error(txt || 'Error agregando lenguaje')
      }
      const created = await res.json()
      setLanguages(prev => [created, ...prev])
      setNewLang('')
    } catch (err) {
      alert(err.message)
    }
  }

  async function deleteLanguage(id) {
    if (!confirm('Eliminar lenguaje?')) return
    try {
      const res = await fetch(`${apiBase}/lenguajes/${id}`, {
        method: 'DELETE',
        headers: token ? { Authorization: `Bearer ${token}` } : {}
      })
      if (!res.ok) throw new Error('Error eliminando lenguaje')
      setLanguages(prev => prev.filter(l => l.leng_id !== id))
    } catch (err) {
      alert(err.message)
    }
  }

  return (
    <div className="modal">
      <div className="modal-content">
        <h3>Lenguajes de {user.nombre}</h3>
        <div style={{display:'flex',gap:8}}>
          <input value={newLang} onChange={e => setNewLang(e.target.value)} placeholder="Nuevo lenguaje" />
          <button onClick={addLanguage}>Agregar</button>
        </div>
        <ul>
          {languages.map(l => (
            <li key={l.leng_id} style={{display:'flex',justifyContent:'space-between',alignItems:'center',gap:8}}>
              <span>{l.lenguajes}</span>
              <div>
                <button onClick={() => deleteLanguage(l.leng_id)}>Eliminar</button>
              </div>
            </li>
          ))}
        </ul>
        <div style={{textAlign:'right'}}>
          <button onClick={onClose}>Cerrar</button>
        </div>
      </div>
    </div>
  )
}
