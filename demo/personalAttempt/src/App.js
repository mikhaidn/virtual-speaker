import './App.css';
import React, { useState, useEffect } from 'react';
import WebPlayback from './WebPlayback'
import Login from './Login'
import './App.css';

function App() {

  const [token, setToken] = useState('');

  useEffect(() => {

    async function getToken() {
      const response = await fetch('/auth/token');
      const json = await response.json();
      setToken(json.access_token);
    }

    getToken();

  }, []);

  return (
    <div className="App">
      <header className="App-header">
         <>
        { (token === '') ? <Login/> : <WebPlayback token={token} /> }
        </>
      </header>
    </div>
  );
}

export default App;

