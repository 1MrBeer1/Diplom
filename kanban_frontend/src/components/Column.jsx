import React from "react";
import { Droppable, Draggable } from "react-beautiful-dnd";
import TaskCard from "./TaskCard";

export default function Column({ droppableId, title, tasks }) {
  return (
    <div className="column">
      <h3>{title}</h3>
      <Droppable droppableId={droppableId}>
        {(provided) => (
          <div ref={provided.innerRef} {...provided.droppableProps} className="task-list">
            {tasks.map((task, index) => (
              <Draggable key={task.id} draggableId={task.id.toString()} index={index}>
                {(provided) => (
                  <div ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>
                    <TaskCard task={task} />
                  </div>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
          </div>
        )}
      </Droppable>
    </div>
  );
}
