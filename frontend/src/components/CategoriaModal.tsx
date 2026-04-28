import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'
import type { Categoria } from '../types/categoria'

export interface CategoriaFormData {
  nombre: string
  descripcion: string
}

interface CategoriaModalProps {
  isOpen: boolean
  categoriaSeleccionada: Categoria | null
  onClose: () => void
  onSubmit: (data: CategoriaFormData) => void
}

const CategoriaModal = ({
  isOpen,
  categoriaSeleccionada,
  onClose,
  onSubmit,
}: CategoriaModalProps) => {
  const [nombre, setNombre] = useState('')
  const [descripcion, setDescripcion] = useState('')
  const [error, setError] = useState('')

  useEffect(() => {
    if (categoriaSeleccionada) {
      setNombre(categoriaSeleccionada.nombre)
      setDescripcion(categoriaSeleccionada.descripcion)
      setError('')
      return
    }

    setNombre('')
    setDescripcion('')
    setError('')
  }, [categoriaSeleccionada, isOpen])

  if (!isOpen) return null

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    const nombreTrim = nombre.trim()
    const descripcionTrim = descripcion.trim()

    if (!nombreTrim || !descripcionTrim) {
      setError('Nombre y descripción son obligatorios.')
      return
    }

    setError('')
    onSubmit({ nombre: nombreTrim, descripcion: descripcionTrim })
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4">
      <div className="w-full max-w-md rounded-lg bg-white p-6 shadow-xl">
        <h2 className="text-xl font-semibold text-slate-900">
          {categoriaSeleccionada ? 'Editar Categoría' : 'Nueva Categoría'}
        </h2>

        <form className="mt-4 space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="mb-1 block text-sm font-medium text-slate-700" htmlFor="nombre">
              Nombre
            </label>
            <input
              id="nombre"
              type="text"
              value={nombre}
              onChange={(event) => setNombre(event.target.value)}
              className="w-full rounded-md border border-slate-300 px-3 py-2 text-slate-900 outline-none ring-blue-500 focus:ring-2"
            />
          </div>

          <div>
            <label
              className="mb-1 block text-sm font-medium text-slate-700"
              htmlFor="descripcion"
            >
              Descripción
            </label>
            <textarea
              id="descripcion"
              value={descripcion}
              onChange={(event) => setDescripcion(event.target.value)}
              className="min-h-24 w-full rounded-md border border-slate-300 px-3 py-2 text-slate-900 outline-none ring-blue-500 focus:ring-2"
            />
          </div>

          {error && <p className="text-sm text-red-600">{error}</p>}

          <div className="flex justify-end gap-2 pt-2">
            <button
              type="button"
              onClick={onClose}
              className="rounded-md border border-slate-300 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100"
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
            >
              Guardar
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CategoriaModal