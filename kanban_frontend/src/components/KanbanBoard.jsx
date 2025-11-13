import React, { useEffect, useState } from "react";
import { DragDropContext } from "react-beautiful-dnd";
import { fetchKanban, updateTasksBulk } from "../api/tasks";
import Column from "./Column";

const DEFAULT_COLUMNS = ["TODO", "IN_PROGRESS", "CHECING" ,"DONE"];

export default function KanbanBoard({ projectId, showEmptyColumns }) {
  const [columns, setColumns] = useState({});

  useEffect(() => {
    async function loadTasks() {
      try {
        const data = projectId ? await fetchKanban(projectId) : {};
        const cols = data || {};
        // Добавляем пустые колонки если их нет
        DEFAULT_COLUMNS.forEach((col) => {
          if (!cols[col]) cols[col] = [];
        });
        setColumns(cols);
      } catch (err) {
        console.error(err);
        if (showEmptyColumns) {
          const emptyCols = {};
          DEFAULT_COLUMNS.forEach((c) => (emptyCols[c] = []));
          setColumns(emptyCols);
        }
      }
    }
    loadTasks();
  }, [projectId, showEmptyColumns]);

  const onDragEnd = async (result) => {
    const { source, destination } = result;
    if (!destination) return;

    const sourceCol = source.droppableId;
    const destCol = destination.droppableId;

    const sourceItems = Array.from(columns[sourceCol] || []);
    const destItems = Array.from(columns[destCol] || []);

    const [movedItem] = sourceItems.splice(source.index, 1);
    movedItem.column = destCol;
    destItems.splice(destination.index, 0, movedItem);

    const newCols = { ...columns, [sourceCol]: sourceItems, [destCol]: destItems };
    setColumns(newCols);

    const updates = [];
    Object.keys(newCols).forEach((col) => {
      newCols[col].forEach((task, index) => updates.push({ id: task?.id, column: col, order: index }));
    });

    try {
      await updateTasksBulk(updates);
    } catch (err) {
      console.error("Failed to update tasks:", err);
    }
  };

  return (
    <div className="kanban-board">
      <DragDropContext onDragEnd={onDragEnd}>
        {DEFAULT_COLUMNS.map((colId) => (
          <Column key={colId} droppableId={colId} title={colId} tasks={columns[colId] || []} />
        ))}
      </DragDropContext>
    </div>
  );
}
