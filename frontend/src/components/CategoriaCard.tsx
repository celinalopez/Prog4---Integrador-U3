import type { Categoria } from '../types/categoria'

interface CategoriaCardProps {
  categoria: Categoria
  onEdit: (categoria: Categoria) => void
  onDelete: (id: number) => void
}

const CategoriaCard = ({ categoria, onEdit, onDelete }: CategoriaCardProps) => {
  return (
    <article className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm transition hover:shadow-md">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-start sm:justify-between">
        <div className="min-w-0">
          <h3 className="truncate text-base font-semibold text-slate-900">{categoria.nombre}</h3>
          <p className="mt-1 text-sm leading-relaxed text-slate-600">{categoria.descripcion}</p>
        </div>

        <div className="flex shrink-0 gap-2 sm:pl-4">
          <button
            type="button"
            onClick={() => onEdit(categoria)}
            className="rounded-md bg-blue-600 px-3 py-2 text-sm font-medium text-white transition hover:bg-blue-700"
          >
            Editar
          </button>
          <button
            type="button"
            onClick={() => onDelete(categoria.id)}
            className="rounded-md bg-red-600 px-3 py-2 text-sm font-medium text-white transition hover:bg-red-700"
          >
            Eliminar
          </button>
        </div>
      </div>
    </article>
  )
}

export default CategoriaCard