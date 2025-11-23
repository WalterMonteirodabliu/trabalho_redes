import { useState } from "react";
import api from "./api";  // <<< usa o axios global
import Card from "./Card";
import Input from "./Input";
import Button from "./Button";

export default function Login({ setUserLogged }) {
  const [login, setLogin] = useState("");
  const [senha, setSenha] = useState("");

  const handleLogin = async () => {
    try {
      const res = await api.post("/login", { login, senha });
      alert(res.data.message);
      setUserLogged(true); 
    } catch (err) {
      alert(err.response?.data?.error || "Erro ao fazer login");
    }
  };

  return (
    <Card>
      <h2 style={{ marginBottom: "20px" }}>Login</h2>
      <Input placeholder="Login" value={login} onChange={e => setLogin(e.target.value)} />
      <Input type="password" placeholder="Senha" value={senha} onChange={e => setSenha(e.target.value)} />
      <Button onClick={handleLogin}>Entrar</Button>
    </Card>
  );
}
