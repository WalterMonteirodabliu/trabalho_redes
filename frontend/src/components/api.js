// api.js
import axios from "axios";

const api = axios.create({
  baseURL: "https://api.meutrabalhoredes.online",
  withCredentials: true
});

export default api;

