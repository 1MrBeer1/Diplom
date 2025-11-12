import React from "react";
import { Navigate } from "react-router-dom";
import { getToken } from "../api/auth";

export default function ProtectedRoute({ children }) {
  if (!getToken()) {
    return <Navigate to="/" replace />;
  }
  return children;
}
