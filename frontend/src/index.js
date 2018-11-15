import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';
//import data from './components/data';


import  Root  from './components/Root';
import Articles from './components/Articles';
import  Article  from './components/Article';


class App extends React.Component {

  


  render() {
    return (
      <BrowserRouter>
      	<div>
        <Route exact={true} path={"/"} component={ () => <Root /> } />
        <Route path={"/articles/:tag"} component={ () => <Articles /> } />
        <Route path="/article/:uname/:artid"  component={ () => <Article /> } />
      	
      	</div>
      </BrowserRouter>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
