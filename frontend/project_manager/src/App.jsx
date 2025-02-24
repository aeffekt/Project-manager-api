import './App.css'
import Projects from './components/Projects'

function App() {
  

  return (
    <>
      <h1>Project Manager</h1>      
      <Projects />      
      <footer>
        <h4 style={{ 
          position: "fixed",
          bottom: "0",
          left: "0",
          width: "100%",
          textAlign: "center",
          marginBottom: "10px",
          borderTop: "1px solid #aaa"
        }}>
          Developed by Agustin Arnaiz</h4>
      </footer>
      
    </>
  )
}

export default App
