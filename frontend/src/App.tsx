import { useEffect, useState } from 'react'
import CategoriaList from './components/CategoriaList'
import CategoriaModal from './components/CategoriaModal'
import type { CategoriaFormData } from './components/CategoriaModal'
import Navbar from './components/Navbar'
import type { Categoria } from './types/categoria'

const API_BASE_URL = 'http://localhost:8000'

function App() {
  const [categorias, setCategorias] = useState<Categoria[]>([])
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [categoriaSeleccionada, setCategoriaSeleccionada] = useState<Categoria | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const cargarCategorias = async () => {
    setIsLoading(true)
    setError(null)

    try {
      const response = await fetch(`${API_BASE_URL}/categorias`)

      if (!response.ok) {
        throw new Error('No se pudieron cargar las categorías.')
      }

      const data: Categoria[] = await response.json()
      setCategorias(data)
    } catch {
      setError('Ocurrió un error al cargar las categorías.')
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(() => {
    void cargarCategorias()
  }, [])

  const handleCreate = async (data: CategoriaFormData) => {
    setError(null)

    try {
      const response = await fetch(`${API_BASE_URL}/categorias`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error('No se pudo crear la categoría.')
      }

      await cargarCategorias()
      handleCloseModal()
    } catch {
      setError('Ocurrió un error al crear la categoría.')
    }
  }

  const handleUpdate = async (id: number, data: CategoriaFormData) => {
    setError(null)

    try {
      const response = await fetch(`${API_BASE_URL}/categorias/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error('No se pudo actualizar la categoría.')
      }

      await cargarCategorias()
      handleCloseModal()
    } catch {
      setError('Ocurrió un error al actualizar la categoría.')
    }
  }

  const handleDelete = async (id: number) => {
    setError(null)

    try {
      const response = await fetch(`${API_BASE_URL}/categorias/${id}`, {
        method: 'DELETE',
      })

      if (!response.ok) {
        throw new Error('No se pudo eliminar la categoría.')
      }

      await cargarCategorias()
    } catch {
      setError('Ocurrió un error al eliminar la categoría.')
    }
  }

  const handleOpenCreateModal = () => {
    setCategoriaSeleccionada(null)
    setIsModalOpen(true)
  }

  const handleOpenEditModal = (categoria: Categoria) => {
    setCategoriaSeleccionada(categoria)
    setIsModalOpen(true)
  }

  const handleCloseModal = () => {
    setIsModalOpen(false)
    setCategoriaSeleccionada(null)
  }

  const handleSubmitCategoria = async (data: CategoriaFormData) => {
    if (categoriaSeleccionada) {
      await handleUpdate(categoriaSeleccionada.id, data)
      return
    }

    await handleCreate(data)
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <main className="mx-auto w-full max-w-5xl px-4 py-8 sm:px-6">
        <section className="mx-auto w-full max-w-4xl rounded-2xl border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
          <header className="mb-6 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <h1 className="text-2xl font-semibold text-slate-900">Categorías</h1>

            <button
              type="button"
              onClick={handleOpenCreateModal}
              className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-blue-700"
            >
              + Añadir Categoría
            </button>
          </header>

          {isLoading && (
            <div className="rounded-lg border border-slate-200 bg-slate-50 p-4 text-sm text-slate-700">
              Cargando categorías...
            </div>
          )}

          {error && (
            <div className="mb-4 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-700">
              {error}
            </div>
          )}

          {!isLoading && (
            <CategoriaList
              categorias={categorias}
              onEdit={handleOpenEditModal}
              onDelete={handleDelete}
            />
          )}
        </section>
      </main>

      <CategoriaModal
        isOpen={isModalOpen}
        categoriaSeleccionada={categoriaSeleccionada}
        onClose={handleCloseModal}
        onSubmit={handleSubmitCategoria}
      />
    </div>
  )
}

export default App