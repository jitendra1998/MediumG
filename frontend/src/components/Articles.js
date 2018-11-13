import React, { Component } from 'react';
import { withRouter } from "react-router";
import { Link } from 'react-router-dom';
import { Button, Jumbotron } from 'react-bootstrap';
import data from './data';
//import logo from './logo.svg';
import './Root.css';

class Articles extends Component {
  
  render() {
 
    return (
      <div className="container App">
        <div className="row navbar"><h1 className="title">MediumG</h1></div>
        <div className="col-md-6 col-md-offset-3">     
          <div className="row">
            {data.map((x) => 
          	  <Link to={"/article"+{x.article_id}}><Jumbotron className="jumbo">
  				<h4>{x.name1}</h4>
  				<div div className="time">
  				<p>{x.time}</p>
  				<p>{x.readingTime}</p>
  				</div>
  				<h2>
  				  {x.title}
  				</h2>
			</Jumbotron> </Link>       
            )
        	}
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(Articles);




