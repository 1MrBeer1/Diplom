import React from "react";
import { useParams } from "react-router-dom";
import KanbanBoard from "../components/KanbanBoard";

export default function Board() {
  const { projectId } = useParams();
  return <KanbanBoard projectId={Number(projectId)} />;
}
