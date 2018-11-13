import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import * as serviceWorker from './serviceWorker';
import axios from 'axios';

import  Root  from './components/Root';
import Articles from './components/Articles';
//import { Article } from './components/Article';

        //<Route path={"article/:id"} component={Article} />

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data:''
    };

    this.setData = this.setData.bind(this);
    this.getData = this.getData.bind(this);
  }

  setData(newData) {
    this.setState({
      data: newData
    });
  }

  getData(tag) {
  	axios.get('http://localhost:5000', {
  		params: {
    		tag: tag
  		}
	})      
	.then((response) => {
      this.setState({data:response.data})
    })
  }

  shouldComponentUpdate(nextProps, nextState){
  	if (this.state.data === "") {
  		return true
  	}
  	else {
  		return false
  	}
    
  }

  render() {
    return (
      <BrowserRouter>
      	<div>
        <Route exact={true} path={"/"} component={ () => <Root />} />
        <Route path={"/articles/:tag"} component={ () => <Articles get = {this.getData} set={this.setData} data={this.state.data}/>} />
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
