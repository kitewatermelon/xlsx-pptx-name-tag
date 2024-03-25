import React, { Component } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import Header from './Header';
import Main from './Pages/Main.js';
import File from './Pages/File.js';
import Complete from './Pages/Complete.js';
// import Product from './Product';

const App = () => {
	return (
		<div className='App'>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main />}></Route>
          <Route path="/file" element={<File />}></Route>
          <Route path="/complete" element={<Complete />}></Route>
          {/* <Route path="/product/:productId" element={<Product />}></Route>
          <Route path="*" element={<NotFound />}></Route> */}
        </Routes>
      </BrowserRouter>
		</div>
	);
}

export default App;