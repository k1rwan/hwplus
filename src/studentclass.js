import React from 'react';
import ReactDOM from 'react-dom';
import './studentclass.css';
import {Row,Col,Button} from'antd'

class Studentclass extends React.Component{
    render(){
        console.log(this.props)
        return(
            <div style={{textAlign: 'center'}}>
              <Row >
                  <Col xs={24} sm={8}>
                   Hello world
                   <Button>fads</Button>
                   <br />
            Really
            <br />...<br />...<br />...<br />
            long
            <br />...<br />...<br />...<br />...<br />...<br />...
            <br />...<br />...<br />...<br />...<br />...<br />...
            <br />...<br />...<br />...<br />...<br />...<br />...
            <br />...<br />...<br />...<br />...<br />...<br />...
            <br />...<br />...<br />...<br />...<br />...<br />...
            <br />...<br />...<br />...<br />...<br />...<br />...
            <br />...<br />...<br />...<br />...<br />...<br />
            content
                   </Col>
                   <Col xs={24} sm={8}>
                   Hello world
                   </Col>
                   <Col xs={24} sm={8}>
                   Hello world
                   </Col>
              </Row>
            </div>
        )
    }
}
export default Studentclass;