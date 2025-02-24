import React, { useEffect, useState } from "react";
import ProjectDetails from "./ProjectDetails";

function Projects() {
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null); // State for selected project

  useEffect(() => {
    // Request GET to API
    fetch("http://localhost:8000/v1/projects")
      .then((response) => response.json())
      .then((data) => setProjects(data))
      .catch((error) => console.error("Error fetching projects:", error));
  }, []);

  const handleProjectClick = (project) => {
    setSelectedProject(project); // Save State for selected project
  };

  return (
    <div>
      <h1>Projects</h1>
      {selectedProject ? (
        <ProjectDetails 
          project={selectedProject} 
          onBack={() => setSelectedProject(null)} // Back to list
        />
      ) : (
        <ul  style={{border: "1px solid #ccc", borderRadius: "5px"}} >
          {projects.map((project) => (
            <li
              key={project["project id"]}
              onClick={() => handleProjectClick(project)} // Click on item
              style={{ cursor: "pointer", margin: "10px 0" }}
            >
              {project["name of project"]}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Projects;