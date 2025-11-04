import { useState } from "react";
import Login from "./components/Login";
import Perfil from "./components/Perfil";
import "./App.css";

function App() {
  const [userLogged, setUserLogged] = useState(false);

  return (
    <div className="container">
      {!userLogged ? <Login setUserLogged={setUserLogged} /> : <Perfil />}
    </div>
  );
}

export default App;
