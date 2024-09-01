<!-- resources/views/tasks/edit.blade.php -->
@extends('layouts.app')

@section('content')
<div class="container">
    <h1>Editar Tarefa</h1>

    <form action="{{ route('tasks.update', $task->id) }}" method="POST">
        @csrf
        @method('PUT')

        <div class="mb-3">
            <label for="title" class="form-label">Título</label>
            <input type="text" class="form-control" id="title" name="title" value="{{ $task->title }}" required>
        </div>

        <div class="mb-3">
            <label for="description" class="form-label">Descrição</label>
            <textarea class="form-control" id="description" name="description">{{ $task->description }}</textarea>
        </div>

        <div class="mb-3">
            <label for="status" class="form-label">Status</label>
            <select class="form-control" id="status" name="status">
                <option value="a_fazer" {{ $task->status == 'a_fazer' ? 'selected' : '' }}>A Fazer</option>
                <option value="em_progresso" {{ $task->status == 'em_progresso' ? 'selected' : '' }}>Em Progresso</option>
                <option value="concluido" {{ $task->status == 'concluido' ? 'selected' : '' }}>Concluído</option>
            </select>
        </div>

        <button type="submit" class="btn btn-primary">Atualizar</button>
    </form>
</div>
@endsection
