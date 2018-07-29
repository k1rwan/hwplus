import React from 'react';
import ReactDOM from 'react-dom';
import './studentclass.css';
import {Row,Col} from'antd'

class Studentclass extends React.Component{
    render(){
        console.log(this.props)
        return(
            <div style={{textAlign: 'center'}}>
              <Row>
                  <Col xs={24} sm={8}>
                   Hello world
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