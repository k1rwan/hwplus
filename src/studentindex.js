import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {Modal,Button,Input,Tag,Form,Tooltip,Icon,Cascader,Select,Row,Col,Checkbox,AutoComplete,Radio,Layout,Icon,Menu}from'antd';
import axios from 'axios';
import {Route,Switch,Link,HashRouter,BrowserRouter,Redirect} from 'react-router-dom';

const { Header, Content, Footer, Sider } = Layout;



const StudentIndex=()=>(
    <main>
        <Switch>
           <Route exact path='/studentcenter/' component={Studentcenter}/>
           <Route exact path='/studentcenter/class/' component={Studentclass}/>
           <Route path='/studentcenter/class/courseid/' component={StudentclassID}/>
           <Route path='/studentcenter/feedback/' component={StudentFeedback}/>
           <Route path='/studentcenter/homework/' component={Studenthomework}/>
           <Route path='/studentcenter/message/' component={StudentMessage}/>
           <Route path='/studentcenter/showhomework/' component={Showhomework}/>
           <Route path='/studentcenter/handling/' component={Handling}/>
           <Route path='/aboutus/' component={Introducing}/>
        </Switch>
    </main>    
)

export default StudentIndex;