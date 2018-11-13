import React, { Component } from 'react';
import { withRouter } from "react-router";
import { Link } from 'react-router-dom';
import { Button, Jumbotron } from 'react-bootstrap';
//import logo from './logo.svg';
import './Root.css';

class Article extends Component {
  
  render() {
 
    return (
      <div className="container App">
        <div className="row navbar"><h1 className="title">MediumG</h1></div>
        <div className="col-md-6 col-md-offset-3">     
          <div className="row">
            {this.props.data.map((x) => 
            	{if(x.article_id == this.props.match.params.artid) {
          	  		return (<Jumbotron className="jumbo">
  						<h4>{x.name1}</h4>
  						<div className="time">
  							<p>{x.time}</p>
  							<p>{x.readingTime}</p>
  						</div>
  						<h2>
  				  			{x.title}
  						</h2>
  						
  						{x["article"].map((y) =>
  							<p>{y}</p>
  						)}
  						{x["tags"].map((y) =>
  							<p>{y}</p>
  						)}
  						
					</Jumbotron> )             		
            	}})}
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(Article);




