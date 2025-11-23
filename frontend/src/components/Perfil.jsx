import { useState, useEffect } from "react";
import api from "./api";
import Card from "./Card";

export default function Perfil() {
  const [perfil, setPerfil] = useState(null);

  useEffect(() => {
    const getPerfil = async () => {
      try {
        const res = await api.get("/meu-perfil");
        setPerfil(res.data);
      } catch (err) {
        alert(err.response?.data?.error || "Erro ao carregar perfil");
      }
    };
    getPerfil();
  }, []);

  if (!perfil) return <p>Carregando...</p>;

  return (
    <Card>
      <h2 style={{ marginBottom: "20px" }}>Meu Perfil</h2>
      <p><strong>Nome:</strong> {perfil.nome}</p>
      <p><strong>Data login:</strong> {perfil.data_login}</p>
      <p><strong>Servidor:</strong> {perfil.servidor}</p>
      <p><strong>ID Sessão:</strong> {perfil.session_id}</p>
    </Card>
  );
}
