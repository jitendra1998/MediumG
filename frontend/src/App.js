import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <div className="container App">
        <div className="row navbar"><h1 className="title">MediumG</h1></div>
        <div className="col-md-6 col-md-offset-3">     
          <div className="row search-bar">
            <div id="logo" className="text-center">
              <h2>Medium Scraper</h2><p>Search for the latest content on medium.com with the tags</p>
            </div>
            <form role="form" id="form-buscar" onSubmit={this.handleSubmit}>
              <div className="form-group">
                <div className="input-group">
                  <input id="1" className="form-control" type="text" name="search" placeholder="Enter tag" value={this.state.value} onChange={this.handleChange} required/>
                  <span className="input-group-btn">
                    <button className="btn btn-success" type="submit">
                      <i className="glyphicon glyphicon-search" aria-hidden="true"></i> Search
                    </button>
                  </span>
                </div>
              </div>
            </form>
          </div>            
        </div>
      </div>
    );
  }
}

export default App;




