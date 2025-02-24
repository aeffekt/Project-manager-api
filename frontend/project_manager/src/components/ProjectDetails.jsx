import React from "react";

function ProjectDetails({ project, onBack }) {
  if (!project) return null;

  return (
    <div style={{ padding: "20px", border: "1px solid #ccc", borderRadius: "5px" }}>
      <h2>{project["name of project"]}</h2>
      <p><strong>ID:</strong> {project["project id"]}</p>
      <p><strong>Description:</strong> {project.description}</p>
      <p><strong>Start Date:</strong> {project.start_date}</p>
      <p><strong>Task Count:</strong> {project.task_count}</p>
      <button onClick={onBack} style={{ marginTop: "10px" }}>Back to List</button>
    </div>
  );
}

export default ProjectDetails;