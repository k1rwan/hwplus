import React from 'react';
import ReactDOM from 'react-dom';
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
       console.log(courseid);
       this.setState({
           specificCourse:_.filter(this.props.courselist,(info)=>{return info["id"]==courseid})
       })
    }

    componentWillReceiveProps(nextProps){
       this.setState({
            specificCourse:_.filter(nextProps.courselist,(info)=>{return info["id"]==courseid})
       })
    }

    render(){
        console.log(this.state.specificCourse)
        return(
            <div/>
        )
    }
}

export default Specificclass;