import type { Categoria } from '../types/categoria'
import CategoriaCard from './CategoriaCard'

interface CategoriaListProps {
  categorias: Categoria[]
  onEdit: (categoria: Categoria) => void
  onDelete: (id: number) => void
}

const CategoriaList = ({ categorias, onEdit, onDelete }: CategoriaListProps) => {
  if (categorias.length === 0) {
    return (
      <section className="rounded-xl border border-dashed border-slate-300 bg-slate-50 p-8 text-center text-slate-600">
        No hay categorías cargadas.
      </section>
    )
  }

  return (
    <section className="space-y-3">
      {categorias.map((categoria) => (
        <CategoriaCard
          key={categoria.id}
          categoria={categoria}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </section>
  )
}

export default CategoriaList