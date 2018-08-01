import React from 'react';
import ReactDOM from 'react-dom';
import './studentindex.css';
import {Modal,Button,Input,Tag,Icon,Layout,Menu,Breadcrumb,Avatar,Badge,Row,Col}from'antd';
import axios from 'axios';
import {Route,Switch,Link,HashRouter,BrowserRouter,Redirect} from 'react-router-dom';
import WrappedStudentcenter from './studentcenter.js'
import Studentclass from './studentclass.js'

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;
var userinformation={bupt_id:"",class_number:"",email:"",gender:"",id:"",name:"",username:"",usertype:"",phone:"",wechat:""};

class StudentIndex extends React.Component{
   constructor(props){
    super(props);
    this.state={
        key:1,
        norepeatkey1:true,
        norepeatkey2:true,
        norepeatkey3:true,
        norepeatkey4:true,
        norepeatkey5:true,
        clickmenu:true,//确保是在点击侧边菜单的操作
        bupt_id:"",
        class_number:"",
        email:"",
        gender:"",
        id:"",
        name:"",
        phone:"",
        username:"",
        usertype:"",
        wechat:"",
    }
 }
   
   componentWillMount(){
    if(window.location.pathname==='/studentcenter'){
      this.setState({norepeatkey1:false})
    }
    if(window.location.pathname==='/studentcenter/class'){
       this.setState({norepeatkey2:false})
    }
    //后续随着路径的添加而增加
   }

   componentDidMount(){
     var getbuptId=axios.create({
      url:"http://106.14.148.208:8080/data/users/"+localStorage.getItem("userloginKey"),
      headers:{"content-type":"application/json","token":localStorage.getItem('token')},
      method:'get',
      timeout:1000,
     })
     var that=this;
     getbuptId().then(function(response){
       console.log(response);
       that.setState({
         bupt_id:response.data.data.bupt_id,
         class_number:response.data.data.class_number,
         email:response.data.data.email,
         gender:response.data.data.gender,
         id:response.data.data["id"],
         name:response.data.data["name"],
         phone:response.data.data.phone,
         username:response.data.data.username,
         usertype:response.data.data.usertype,
         wechat:response.data.data.wechat,
         clickmenu:false,
        })
     })
     .catch(function(error){
       console.log(error);
     })
   }

   componentDidUpdate(){
    if(this.state.key==1&&this.state.norepeatkey1){
      this.setState({norepeatkey1:false,norepeatkey2:true,norepeatkey3:true,norepeatkey4:true,norepeatkey5:true,});
     }
    if(this.state.key==2&&this.state.norepeatkey2){
     this.setState({norepeatkey1:true,norepeatkey2:false,norepeatkey3:true,norepeatkey4:true,norepeatkey5:true,});
    }
    if(this.state.key==3&&this.state.norepeatkey3){
      this.setState({norepeatkey1:true,norepeatkey2:true,norepeatkey3:false,norepeatkey4:true,norepeatkey5:true,});
     }
    if(this.state.key==4&&this.state.norepeatkey4){
     this.setState({norepeatkey1:true,norepeatkey2:true,norepeatkey3:true,norepeatkey4:false,norepeatkey5:true,});
    }
    if(this.state.key==5&&this.state.norepeatkey5){
      this.setState({norepeatkey1:true,norepeatkey2:true,norepeatkey3:true,norepeatkey4:true,norepeatkey5:false,});
     }
   }

   changehref=({ item, key, keyPath })=>{
      this.setState({key:key,clickmenu:true,});
   }
  
    render(){
      console.log(localStorage.getItem('token'));
      console.log(window.location)
      userinformation.bupt_id=this.state.bupt_id;
      userinformation.class_number=this.state.class_number;
      userinformation.email=this.state.email;
      userinformation.gender=this.state.gender;
      userinformation["id"]=this.state["id"];
      userinformation["name"]=this.state["name"];
      userinformation.username=this.state.username;
      userinformation.phone=this.state.phone;
      userinformation.usertype=this.state.usertype;
      userinformation.wechat=this.state.wechat;
      if(this.state.key==1&&this.state.norepeatkey1&&this.state.clickmenu){
        return (<Redirect exact push to='/studentcenter'/>);
       }
      if(this.state.key==2&&this.state.norepeatkey2&&this.state.clickmenu){
       return (<Redirect exact push to='/studentcenter/class'/>);
      }
      //后续随着路径的添加而增加
        return(
          <Layout>
          <Header  className="header" style={{marginLeft:'200px',zIndex:1,position:'fixed',width:'100%',background:'#fff'}}>
          <div className="logo">Homework+</div>
            <Menu
              theme="light"
              mode="horizontal"
              style={{ lineHeight: '64px' }}
            >
            <Row>
             <Col xs={10} sm={24}>
             <div className="avatar">
             <Button className="info">5通知</Button>
             <a><Badge count={5} ><Avatar shape="circle" icon="user" size="large" /></Badge></a>
             <Tag className="username" color="geekblue">{this.state.username}</Tag>
             </div>
             </Col>
            </Row>
            </Menu>
          </Header>
          <Layout>
            <Sider style={{overflow: 'auto', height: '100vh', position: 'fixed', left: 0 ,top:'64px',background:'#fff' }}>
              <Menu
                mode="inline"
                theme='light'
                defaultSelectedKeys={[this.state.key]}
                style={{ height: '100%'}}
                onClick={this.changehref}
              >
                  <Menu.Item key="1"><span><Icon type="user" />我的</span></Menu.Item>
                  <Menu.Item key="2"><span><Icon type="usergroup-add" />课程组</span></Menu.Item>
                  <Menu.Item key="3"><span><Icon type="form" />我的作业</span></Menu.Item>
                  <Menu.Item key="4"><span><Icon type="info-circle" />消息</span></Menu.Item>
                  <Menu.Item key="5" className="aboutus"><span className="aboutus2" >关于Homework+</span></Menu.Item>
              </Menu>
            </Sider>
            <Layout style={{ background:'#E6E6E6'}}>
              <Content style={{ background: '#E6E6E6',paddingLeft: 200,paddingTop:64, margin: 0, minHeight: 280 }}>
                <Switch>
                    <Route exact path='/studentcenter' render={(props)=>(
                      <WrappedStudentcenter {...props} userinformation={userinformation}/>
                    )}/>
                    <Route exact path='/studentcenter/class' render={(props)=>(
                      <Studentclass {...props} color="1"/> //传props
                    )}/>
                </Switch>
              </Content>
            </Layout>
          </Layout>
        </Layout>
        )
    }
}



//const StudentIndex=()=>(
//    <main>
//        <Switch>
//           <Route exact path='/studentcenter/' component={Studentcenter}/>
//           <Route exact path='/studentcenter/class/' component={Studentclass}/>
//           <Route path='/studentcenter/class/courseid/' component={StudentclassID}/>
//           <Route path='/studentcenter/feedback/' component={StudentFeedback}/>
//           <Route path='/studentcenter/homework/' component={Studenthomework}/>
//           <Route path='/studentcenter/message/' component={StudentMessage}/>
//           <Route path='/studentcenter/showhomework/' component={Showhomework}/>
//           <Route path='/studentcenter/handling/' component={Handling}/>
//           <Route path='/aboutus/' component={Introducing}/>
//        </Switch>
//    </main>    
//)


export default StudentIndex;