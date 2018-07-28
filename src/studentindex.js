import React from 'react';
import ReactDOM from 'react-dom';
import './studentindex.css';
import {Modal,Button,Input,Tag,Icon,Layout,Menu,Breadcrumb,Avatar,Badge,Row,Col}from'antd';
import axios from 'axios';
import {Route,Switch,Link,HashRouter,BrowserRouter,Redirect} from 'react-router-dom';

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;

class Studentcenter extends React.Component{
    render(){
        return(
          <Layout>
          <Header  className="header" style={{'margin-left':'200px',zindex:1,position:'fixed',width:'100%',background:'#fff'}}>
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
             <a><Badge count={5} ><Avatar shape="circle" icon="user" /></Badge></a>
             <Tag className="username">用户名</Tag>
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
                defaultSelectedKeys={['1']}
                style={{ height: '100%'}}
              >
                  <Menu.Item key="1"><span><Icon type="user" />我的</span></Menu.Item>
                  <Menu.Item key="2"><span><Icon type="usergroup-add" />课程组</span></Menu.Item>
                  <Menu.Item key="3"><span><Icon type="form" />我的作业</span></Menu.Item>
                  <Menu.Item key="4"><span><Icon type="info-circle" />消息</span></Menu.Item>
                  <Menu.Item key="5" className="aboutus"><span className="aboutus2" >关于Homework+</span></Menu.Item>
              </Menu>
            </Sider>
            <Layout style={{ background:'#CCCCCC'}}>
              <Content style={{ background: '#CCCCCC', "padding-left": 200,"padding-top":64, margin: 0, minHeight: 280 }}>
              <div style={{ background: '#E7F8A0', textAlign: 'center' }}>
          ...
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
        </div>
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

const StudentIndex=()=>(
    <main>
        <Switch>
           <Route exact path='/studentcenter/' component={Studentcenter}/>
        </Switch>
    </main>    
)

export default StudentIndex;