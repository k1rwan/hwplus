import React from 'react';
import ReactDOM from 'react-dom';
import './studentclass.css';
import {Row,Col,Button,Card} from'antd'

class Studentclass extends React.Component{
    render(){
        const gridStyle={
            width:"33.3%",
            textAlign:'center',
        }
        return(
            <div>
            <div style={{"font-size":"28px",marginLeft:"20px",marginTop:"10px",marginBottom:"5px"}}>概览</div>
            <Card hoverable="true" style={{marginLeft:"20px",marginRight:"20px"}}>
              <Card.Grid style={gridStyle}>
              <p style={{"font-size":"20px"}}>已加入课程数:</p>
              <span style={{"font-size":'30px'}}>{this.props.courselist.length}  </span>
              个
              </Card.Grid>
              <Card.Grid style={gridStyle}>
              <p style={{"font-size":"20px"}}>待提交作业数:</p>
              <span style={{"font-size":'30px'}}>5  </span>
              个
              </Card.Grid>
              <Card.Grid style={gridStyle}>
              <p style={{"font-size":"20px"}}>未完成作业数:</p>
              <span style={{"font-size":'30px'}}>10  </span>
              个
              </Card.Grid>
            </Card>
            <div style={{"font-size":"28px",marginLeft:"20px",marginTop:"10px",marginBottom:"10px"}}>已加入课程班</div>
            <Row gutter={16}>
      <Col xs={24} sm={8}>
        <Card title="Card title" style={{marginLeft:"20px",marginRight:"20px",marginBottom:"20px"}}>Card content</Card>
      </Col>
      <Col xs={24} sm={8}>
        <Card title="Card title" style={{marginLeft:"20px",marginRight:"20px",marginBottom:"20px"}}>Card content</Card>
      </Col>
      <Col xs={24} sm={8}>
        <Card title="Card title" style={{marginLeft:"20px",marginRight:"20px",marginBottom:"20px"}}>Card content</Card>
      </Col>
      <Col xs={24} sm={8}>
        <Card title="Card title" style={{marginLeft:"20px",marginRight:"20px",marginBottom:"20px"}}>Card content</Card>
      </Col>
      <Col xs={24} sm={8}>
        <Card title="Card title" style={{marginLeft:"20px",marginRight:"20px",marginBottom:"20px"}}>Card content</Card>
      </Col>
      <Col xs={24} sm={8}>
        <Card title="Card title" style={{marginLeft:"20px",marginRight:"20px",marginBottom:"20px"}}>Card content</Card>
      </Col>
    </Row>
    <br/><br/><br/><br/><br/><br/><br/><br/>
            </div>
        )
    }
}
export default Studentclass;