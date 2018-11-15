import React, { Component } from 'react';
import { withRouter } from "react-router";
import { Link } from 'react-router-dom';
import { Button, Jumbotron } from 'react-bootstrap';
import axios from 'axios';

//import logo from './logo.svg';
import './Root.css';
          var y = 0;

class Articles extends Component {
   
  constructor(props) {
    super(props);
    this.state = {
      articles:Array.apply(null, Array(10)).map(Number.prototype.valueOf,0),
      connect:0
    };

    this.getData = this.getData.bind(this);

  }
  componentWillMount() {
        this.getData(this.props.location.state.tag)
  }
  getData(tag) {
        axios.get('https://mediumg-api.herokuapp.com', {
          params: {
            tag: tag
          }
        })      
        .then((response) => {
          var articles = Array.apply(null, Array(10)).map(Number.prototype.valueOf,0);
          response.data.map((i,index) => {
            if(index<=10) {
            axios.get('https://mediumg-api.herokuapp.com/data1', {
              params: {
                tag: tag,
                i: i
              }
            })
            .then((res) => {
              articles[index] = res.data;
              this.setState({articles:articles})
              y = y + 1
            })
          }
          })
      })
    };
  render() {
    
    return (
      <div className="container App">
        <div className="row navbar"><h1 className="title">MediumG</h1></div>
        <div className="col-md-6 col-md-offset-3">     
          <div className="row">
              {this.state.articles.map((x, index) => {
              if (index==y && y<10) 
                return(
                <Jumbotron className="jumbo">
                  <h1>Crawling...</h1>
                </Jumbotron> 
                )
                else if (index >y && y<10) return(
                <Jumbotron className="jumbo">
                  <h1>Pending...</h1>
                </Jumbotron>
                )
                else 
                  return (
                <Jumbotron className="jumbo">
                <h4>{x.name1}</h4>
                <div className="time">
                <p>{new Date(x.time).getDate() + " " + new Date(x.time).toLocaleString("en-us", { month: "short" })} </p>
                <p>{Math.ceil(x.readingTime/275)} min</p>
                </div>
                <Link to={"/article/"+ x.username + "/" + x.slug} params={{uname: x.username, artid:x.slug}} target="_blank"><h2>
                {x.title}
                </h2></Link>
                </Jumbotron>
                )
              
        }
            )
          }
          </div>
        </div>
      </div>
    );
  }
}

export default withRouter(Articles);




