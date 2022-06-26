import React from 'react';
import './App.css';
import SearchTable from './components/filtertable';
import Header from "./Header"
import Searchbar from './Searchbar';
import Sidebar from './Sidebar';

function App() {
  return (
    <div className="app">
    <Header />
    <div className = "app_body">
   <Sidebar />
   <Searchbar/>
   <SearchTable/>
    </div>
    </div>
  );
}

export default App;
