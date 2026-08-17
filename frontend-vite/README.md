Vite + React frontend minimal para conectar con el backend en PRACTICA

Archivos incluidos:
- package.json
- index.html
- src/main.jsx
- src/App.jsx
- src/components/UsersList.jsx
- src/components/UserForm.jsx
- src/components/LanguagesModal.jsx
- src/styles.css
- .env (opcional)

Instrucciones:
1) Copiar a tu máquina o dejar en el repo en la rama frontend-vite
2) Instalar dependencias: npm install
3) Crear .env si quieres cambiar la URL del backend:
   VITE_API_URL=http://localhost:8000
4) Ejecutar: npm run dev

Endpoints esperados (se basan en el backend presente en PRACTICA):
- GET  /usuarios                  -> lista de usuarios
- POST /usuarios                  -> crear usuario (JSON {nombre,dni,password})
- DELETE /usuarios/{id}           -> eliminar usuario (requiere autenticación JWT)
- POST /login                     -> login (form-urlencoded username=dni&password=...)
- GET  /usuarios/{user_id}/lenguajes
- POST /usuarios/{user_id}/lenguajes  -> { lenguaje }
- DELETE /lenguajes/{leng_id}     -> eliminar lenguaje (requiere auth)

Notas importantes:
- El frontend usa localStorage para guardar el token JWT (key: token)
- Acciones protegidas (crear/eliminar lenguajes, eliminar usuario) envían el header Authorization: Bearer <token>
- Asegúrate de que el backend tenga CORS habilitado. En FastAPI puedes usar:
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:5173"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"]
    )

Qué hice:
- Añadí un frontend minimal a la rama frontend-vite con componentes para gestionar usuarios y lenguajes y login.

Cómo revertir (si no quieres mantener los archivos):
- Borrar la rama remota: git push origin --delete frontend-vite
- Borrar la rama local: git checkout main && git branch -D frontend-vite

Cuando quieras, puedo abrir un Pull Request desde esta rama o ajustar la UI/funcionalidad según prefieras.
