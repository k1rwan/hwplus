import React from 'react';
import ReactDOM from 'react-dom';
import {Row,Col,Card} from'antd'
import './studentspecificclass.css';
import {_} from 'underscore'
var courseid;//特定课程的id
var re=/^\/studentcenter\/class\/(.*)\/$/;
class Specificclass extends React.Component{
    constructor(props){
        super(props);
        this.state={
            specificCourse:{},//特定课程，为一个对象
        }
    }

    componentWillMount(){
       courseid=re.exec(window.location.pathname)[1];
       this.setState({
           specificCourse:_.filter(this.props.courselist,(info)=>{return info["id"]==courseid})
       })
    }

    componentWillReceiveProps(nextProps){
       if(JSON.stringify(_.filter(nextProps.courselist,(info)=>{return info["id"]==courseid}))!==
          JSON.stringify(_.filter(this.props.courselist,(info)=>{return info["id"]==courseid}))){
         this.setState({
            specificCourse:_.filter(nextProps.courselist,(info)=>{return info["id"]==courseid})
         })
       }
    }

    render(){
        console.log(this.state.specificCourse)
        const gridStyle={
            width:"33.3%",
            textAlign:'center',
        }
        var courseTeacher=[];
        var courseAssistant=[];
        for(let i=0;i<this.state.specificCourse[0].teachers.length;i++){
            courseTeacher.push(
              <span key={i} style={{marginLeft:"5px",marginRight:"5px"}}>
                  {this.state.specificCourse[0].teachers[i]["name"]}
              </span>
            )
        }
        for(let i=0;i<this.state.specificCourse[0].teachingAssistants.length;i++){
          courseAssistant.push(
            <span key={i} style={{marginLeft:"5px",marginRight:"5px"}}>
                {this.state.specificCourse[0].teachingAssistants[i]["name"]}
            </span>
          )
        }
        return(
         <div>
           <Card hoverable>
              <Card.Grid style={gridStyle}>
                  <Col xs={24} sm={20}>{this.state.specificCourse[0]["name"]}</Col>
                  <Col xs={24} sm={4}>{this.state.specificCourse[0].students.length}人</Col>
                  <Col xs={24} sm={12}>教师: {courseTeacher}</Col>
                  <Col xs={24} sm={12}>助教: {courseAssistant}</Col>
              </Card.Grid>
              <Card.Grid style={gridStyle}/>
              <Card.Grid style={gridStyle}/>
           </Card>
         </div>
        )
    }
}

export default Specificclass;