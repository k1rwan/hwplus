import React from 'react';
import ReactDOM from 'react-dom';
import './studentindex.css';
import {Modal,Button,Input,Tag,Icon,Layout,Menu,Breadcrumb,Avatar,Badge,Row,Col}from'antd';
import axios from 'axios';
import {Route,Switch,Link,HashRouter,BrowserRouter,Redirect} from 'react-router-dom';
import WrappedStudentcenter from './studentcenter.js'
import Studentclass from './studentclass.js'
import {_} from 'underscore'

const { SubMenu } = Menu;
const { Header, Content, Sider,Footer } = Layout;
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
        courselist:[],//学生加入的课程班信息，为一个数组，数组里面的每个元素均为单个课程班的信息
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
    const gridStyle={
      width:'100%',
      textAlign:'center',
    }
     var getbuptId=axios.create({
      url:"http://homeworkplus.cn/data/users/"+localStorage.getItem("userloginKey")+"/",
      headers:{"content-type":"application/json","token":localStorage.getItem('token')},
      method:'get',
      timeout:1000,
     })
     var that=this;
     getbuptId().then(function(response){
       var str=JSON.stringify(response.data.data);
       localStorage.setItem("user",str);//将对象转换为字符串，这样可以存储在localStorage里
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
      var lastUpdatestudentcourse=[];
      this.getCourse=setInterval(()=>{
      var getUserCourse=axios.create({
        url:"http://homeworkplus.cn/data/user_with_course/student/"+that.state["id"]+"/",
        headers:{"content-type":"application/json","token":localStorage.getItem('token')},
        method:'get',
        timeout:1000,
      })
      getUserCourse().then(function(response){
        //获得该用户拥有的所有的课程版的ID
        if(JSON.stringify(lastUpdatestudentcourse)!==JSON.stringify(response.data.students_course)){
          lastUpdatestudentcourse=response.data.students_course;
          var courselist2=[];
          for(let i=0;i<lastUpdatestudentcourse.length;i++){
            var getCourseInfo=axios.create({
              url:"http://homeworkplus.cn/data/courses/"+lastUpdatestudentcourse[i]+"/",
              headers:{"content-type":"application/json","token":localStorage.getItem('token')},
              method:'get',
              timeout:1000,
             })
            getCourseInfo().then(function(response2){
              courselist2[i]=response2.data;
              that.setState({courselist: courselist2});
              console.log(that.state.courselist);
            })
            .catch(function(error2){
              console.log(error2);
            })
          }          
        }
      })
      .catch(function(error){
        console.log(error);
      });
     },1000)
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

   componentWillUnmount(){
     clearInterval(this.getCourse);
   }

   changehref=({ item, key, keyPath })=>{
      this.setState({key:key,clickmenu:true,});
   }

   //修改用户信息
   changeinformation=(info)=>{
      this.setState({username:info.username,class_number:info.class_number,phone:info.phone});
   }
  
    render(){
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
          <div>
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
          </Layout>
          <Layout style={{ background:'#E6E6E6'}}>
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
            <Content style={{ background: '#E6E6E6',paddingLeft: 200,paddingTop:64, margin: 0, minHeight: 280 }}>
                <Switch>
                    <Route exact path='/studentcenter' render={(props)=>(
                      <WrappedStudentcenter {...props} 
                       userinformation={userinformation}
                       changeinformation={this.changeinformation}
                       courselist={this.state.courselist}
                       //studentCourse={this.state.studentCourse}
                       />
                    )}/>
                    <Route exact path='/studentcenter/class' render={(props)=>(
                      <Studentclass {...props} color="1"/> //传props
                    )}/>
                </Switch>
            </Content>
            <Footer style={{background:'#E6E6E6'}}>Footer</Footer>
            </Layout>
           </div>
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