import React from 'react';
import ReactDOM from 'react-dom';
import './validateEmail.css';
import axios from 'axios';
import {Route,Switch,Link,HashRouter,BrowserRouter,Redirect} from 'react-router-dom';
var gotToken='';
var postToken=axios.create({
    url:"http://106.14.148.208:8080/account/activate/",
    headers:{"content-type":"application/json","token":gotToken},
    method:'post',
    timeout:1000,
})
var re=/^([0-9a-zA-Z\_\.\/\:]*)\?token=([0-9A-Za-z\.]*)$/;
class ValidateEmail extends React.Component{
   componentDidMount(){
       if(gotToken===''){
           gotToken=re.exec(window.location.href)[2];
           console.log(gotToken);
           postToken().then(function(response){
               console.log(response);
           })
           .catch(function(error){
               console.log(error);
           })
       }
   }

   componentWillUnmount(){
       gotToken='';
   }

   render(){
       return(<p>您注册的用户已通过验证!</p>)
   }
}

export default ValidateEmail;