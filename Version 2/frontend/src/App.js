import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import AddressSelect from './pages/AddressSelect';
import InfoPage from './pages/InfoPage';
import { useState } from 'react';

function App() {

  const [address, setAddress] = useState("");

  return (
    <Router>
      <Routes>
          <Route exact path="/" element={<AddressSelect setAdd={setAddress}/>} />
          <Route path="/infopage" element={<InfoPage address={address}/>} />
      </Routes>
    </Router>
  );
}

export default App;
