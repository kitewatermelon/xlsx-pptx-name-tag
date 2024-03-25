import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Main from './Pages/Main.js';
import File from './Pages/File.js';
import Complete from './Pages/Complete.js';

const App = () => {
	return (
		<div className='App'>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main />}></Route>
          <Route path="/file" element={<File />}></Route>
          <Route path="/complete" element={<Complete />}></Route>
        </Routes>
      </BrowserRouter>
		</div>
	);
}

export default App;