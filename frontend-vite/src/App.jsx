import React, { useEffect, useState } from 'react'
import UsersList from './components/UsersList'
import UserForm from './components/UserForm'
import LanguagesModal from './components/LanguagesModal'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function App() {
  const [users, setUsers] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [token, setToken] = useState(localStorage.getItem('token') || null)
  const [selectedUser, setSelectedUser] = useState(null)
  const [showLangModal, setShowLangModal] = useState(false)

  async function fetchUsers() {
    setLoading(true)
    setError(null)
    try {
      const res = await fetch(`${API_BASE}/usuarios`)
      if (!res.ok) throw new Error('Error al obtener usuarios')
      const data = await res.json()
      setUsers(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => { fetchUsers() }, [])

  async function handleCreateUser(user) {
    try {
      const res = await fetch(`${API_BASE}/usuarios`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user)
      })
      if (!res.ok) {
        const txt = await res.text()
        throw new Error(txt || 'Error creando usuario')
      }
      const created = await res.json()
      setUsers(prev => [created, ...prev])
    } catch (err) {
      alert(err.message)
    }
  }

  async function handleDeleteUser(id) {
    if (!confirm('Eliminar este usuario?')) return
    try {
      const res = await fetch(`${API_BASE}/usuarios/${id}`, {
        method: 'DELETE',
        headers: token ? { Authorization: `Bearer ${token}` } : {}
      })
      if (!res.ok) {
        const txt = await res.text()
        throw new Error(txt || 'Error eliminando usuario')
      }
      setUsers(prev => prev.filter(u => u.user_id !== id))
    } catch (err) {
      alert(err.message)
    }
  }

  async function handleLogin(dni, password) {
    try {
      const body = new URLSearchParams()
      body.append('username', dni)
      body.append('password', password)

      const res = await fetch(`${API_BASE}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: body.toString()
      })
      if (!res.ok) throw new Error('Credenciales inválidas')
      const data = await res.json()
      setToken(data.access_token)
      localStorage.setItem('token', data.access_token)
      alert('Login exitoso')
    } catch (err) {
      alert(err.message)
    }
  }

  function handleLogout() {
    setToken(null)
    localStorage.removeItem('token')
  }

  function openLanguages(user) {
    setSelectedUser(user)
    setShowLangModal(true)
  }

  return (
    <div className="container">
      <header style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h1>Gestión de Usuarios y Lenguajes</h1>
        <div>
          {token ? (
            <>
              <span className="token-badge">Autenticado</span>
              <button onClick={handleLogout}>Cerrar sesión</button>
            </>
          ) : (
            <div style={{display:'inline-block'}}>
              <form onSubmit={e => {e.preventDefault(); const f = e.target; handleLogin(f.dni.value, f.password.value)}}>
                <input name="dni" placeholder="DNI" />
                <input name="password" type="password" placeholder="Password" />
                <button type="submit">Ingresar</button>
              </form>
            </div>
          )}
        </div>
      </header>

      <section style={{marginTop:20}}>
        <UserForm onCreate={handleCreateUser} />
      </section>

      <section style={{marginTop:20}}>
        {loading && <p>Cargando usuarios...</p>}
        {error && <p className="error">{error}</p>}
        <UsersList users={users} onDelete={handleDeleteUser} onOpenLanguages={openLanguages} />
      </section>

      {showLangModal && selectedUser && (
        <LanguagesModal
          apiBase={API_BASE}
          token={token}
          user={selectedUser}
          onClose={() => { setShowLangModal(false); setSelectedUser(null) }}
        />
      )}

      <footer style={{marginTop:20,fontSize:12,color:'#666'}}>Asegúrate de habilitar CORS en el backend y ajustar VITE_API_URL si corresponde.</footer>
    </div>
  )
}
