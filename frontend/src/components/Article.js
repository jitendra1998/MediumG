import React, { Component } from 'react';
import { withRouter } from "react-router";
import { Link } from 'react-router-dom';
import { Button, Jumbotron } from 'react-bootstrap';
import axios from 'axios'
//import logo from './logo.svg';
import './Root.css';

class Article extends Component {
  

  constructor(props) {
    super(props);
    this.state = {
    	article: {"arti":[],"tags":[],"res":[]}
    };

    this.getData = this.getData.bind(this);

  }
  componentWillMount() {
        this.getData(this.props.match.params.artid, this.props.match.params.uname)
  }
  getData(artid,uname) {
        axios.get('http://localhost:5000/data', {
          params: {
            artid: artid,
            uname: uname
          }
        })      
        .then((response) => {
        	console.log(response.data)
          this.setState({article:response.data})
      })
    };

  render() {
 
    return (
      <div className="container App">
        <div className="row navbar"><h1 className="title">MediumG</h1></div>
        <div className="col-md-6 col-md-offset-3">     
          <div className="row">
            
           			{
           				<div>
          	  		<Jumbotron className="jumbo">
  						<h4>{this.state.article.name1}</h4>
  						<div className="time">
  							<p>{this.state.article.time}</p>
  							<p>{this.state.article.readingTime}</p>
  						</div>
  						<h2>
  				  			{this.state.article.title}
  						</h2>
  						
  						{this.state.article.arti.map((y) =>
  							<p>{y}</p>
  						)}

  						
					</Jumbotron>  
					<p>Tags</p>

					<Jumbotron className="jumbo">
					<div class="time">
  						{this.state.article.tags.map((y) =>
  							<p onClick={(event) => {event.preventDefault(); this.props.history.push({pathname: '/articles/'+ y,state: { tag: y }});}}><a>{y}</a></p>
  						)}
  					</div>
  					</Jumbotron>

  							<p>Resposes</p>
  							{this.state.article.res.map((y) =>
  								<Jumbotron className="jumbo">
  								
  										<h4>{y.name}</h4>
  										<p>{y.title}</p>
  									
  								</Jumbotron>

  							)}
  						
  					</div>
				}      		
           
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(Article);




