import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import AddressSelect from './pages/AddressSelect';
import InfoPage from './pages/InfoPage';


function App() {
  return (
    <Router>
    <Routes>
        <Route exact path="/" element={<AddressSelect/>} />
        <Route path="/infopage" element={<InfoPage/>} />
    </Routes>
</Router>
  );
}

export default App;
