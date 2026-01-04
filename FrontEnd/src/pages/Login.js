import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import './Login.css';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [captcha, setCaptcha] = useState(null);
  const [captchaText, setCaptchaText] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCaptcha = async () => {
      try {
        const response = await axios.get(
          'http://52.55.206.54:5000/generate-captcha',
          { responseType: 'blob' }
        );
        const imageUrl = URL.createObjectURL(response.data);
        setCaptcha(imageUrl);
      } catch (err) {
        console.error('Error al cargar el captcha:', err);
      }
    };

    fetchCaptcha();
  }, []);

  const handleLogin = async () => {
    try {
      const res = await axios.post('http://52.55.206.54:8001/login', {
        email,
        password,
        captcha: captchaText
      });

      localStorage.setItem('token', res.data.token);
      alert('Login exitoso');
      navigate('/dashboard');
    } catch (err) {
      alert('Login fallido');
    }
  };

  return (
    <div className="login-container">

      <h1 className="main-title">
        Sistema de Gestión de Tutorías Académicas
      </h1>

      <div className="login-logo">
        <img src="logouce.png" alt="Logo" className="logo-image" />
      </div>

      <div className="login-box">
        <h2 className="login-title">Iniciar sesión</h2>

        <input
          type="text"
          placeholder="Usuario"
          className="login-input"
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Contraseña"
          className="login-input"
          onChange={(e) => setPassword(e.target.value)}
        />

        {captcha && (
          <>
            <img src={captcha} alt="Captcha" />
            <input
              type="text"
              placeholder="Ingrese el captcha"
              className="login-input"
              onChange={(e) => setCaptchaText(e.target.value)}
            />
          </>
        )}

        <button onClick={handleLogin} className="login-button">
          Iniciar sesión
        </button>

        <p className="login-footer">
          ¿No tienes una cuenta?{' '}
          <Link to="/register" className="login-link">
            Regístrate aquí
          </Link>
          <br />
          <Link to="/root-login" className="login-link">
            Usuario Root
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
