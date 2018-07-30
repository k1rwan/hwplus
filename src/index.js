import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import {Modal,Button,Input,Tag,Form,Tooltip,Icon,Cascader,Select,Row,Col,Checkbox,AutoComplete,Radio}from'antd';
import axios from 'axios';
import {Route,Switch,Link,HashRouter,BrowserRouter,Redirect} from 'react-router-dom';
import ValidateEmail from './validateEmail.js'
import WrappedModifyPassword from './modifyPassword.js'
import StudentIndex from './studentindex.js'
const FormItem = Form.Item;
const Option = Select.Option;
const RadioGroup = Radio.Group;

var User={name:'',username:'',gender:'',usertype:'',password:'',wechat:'',bupt_id:'',class_number:'',email:'',phone:''};
var Userlogin={type:'',content:''};
var Userlogin2={username:'',password:''};
var userinformation={username:''};
var loginhref='';
var checkLogin=0;//判断是否在正确的入口登录
var vaildEmail=/^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/;
var validPhone=/^1\d{10}$/;
var validPassword =/^\w{6,20}$/;
var postUser=axios.create({
  url:"http://106.14.148.208:8080/data/users/",
  headers:{"content-type":"application/json"},
  method:'post',
  data:User,
  timeout:1000,
});

var loginUser=axios.create({
  url:"http://106.14.148.208:8080/data/is_repeated/",
  headers:{"content-type":"application/json"},
  method:'post',
  data:Userlogin,
  timeout:1000,
})

var takeToken=axios.create({
  url:"http://106.14.148.208:8080/login/",
  headers:{"content-type":"application/json"},
  method:'post',
  data:Userlogin2,
  timeout:1000,
})

var forgetPassword=axios.create({
  url:"http://106.14.148.208:8088/account/forget_password/",
  headers:{"content-type":"application/json"},
  method:'post',
  data:userinformation,
  timeout:1000,
})

class Login extends React.Component{
  constructor(props){
    super(props);
    this.state={
      entry:false,
      redirect:false,
      loginTitle:"学生登录",
      visible3:false,
    }
  }

  showModal=(e)=>{
    if(e.target.innerText==="学生入口"){
      this.setState({loginTitle:"学生登录"});
    }else if(e.target.innerText==="教师入口"){
      this.setState({loginTitle:"教师登录"});
    }else if(e.target.innerText==="助教入口"){
      this.setState({loginTitle:"助教登录"});
    }
    this.setState({entry:true,redirect:false});
  }

  handleCancel=()=>{
    this.setState({entry:false,redirect:false});
  }

  handleSubmit=(e)=>{
    checkLogin=0;
    e.preventDefault();
    this.props.form.validateFieldsAndScroll((err, values) => {
    if(!err){
    Userlogin2.username=values.用户名;
    Userlogin2.password=values.密码;
    var that=this;
    takeToken().then(function(response){
      localStorage.setItem("token",response.headers.token);
      localStorage.setItem("type",response.data.data.usertype);
      localStorage.setItem("userloginKey",response.data.data.id);
      if(localStorage.getItem("type")==='student'&&that.state.loginTitle==="学生登录"){
        checkLogin=1;
        loginhref="/studentcenter";
      }else if (localStorage.getItem("type")==='teacher'&&that.state.loginTitle==="教师登录"){
        checkLogin=1;
        loginhref="/teachercenter";
      }else if(localStorage.getItem("type")==='assistant'&&that.state.loginTitle==="助教登录"){
        checkLogin=1;
        loginhref="/assistantcenter";
      }
      if(!(localStorage.getItem("token")==="None")){
      that.setState({entry:false,redirect:true});
      }
    })
    .catch(function(error){
      console.log(error);
    });
  }
  });
}

   handleEnter=()=>{
     this.setState({entry:false,visible3:true});
   }

   handleCancel2=()=>{
     this.setState({visible3:false});
   }

   handleOk=()=>{
     userinformation.username=document.getElementById("information").value;
     console.log(userinformation.username);
     this.setState({visible3:false});
     forgetPassword().then(function(response){
       const modal = Modal.success({
        title:"修改密码的网址已发到您的邮箱里，请及时查收",
        okText:"确认",
      });
     })
     .catch(function(error){
       console.log(error);
     })
   }
  render(){
    const { getFieldDecorator } = this.props.form;
    const { autoCompleteResult } = this.state;
    const formItemLayout = {
      labelCol: {
        xs: { span: 24 },
        sm: { span: 8 },
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 },
      },
    };
    const tailFormItemLayout = {
      wrapperCol: {
        xs: {
          span: 24,
          offset: 0,
        },
        sm: {
          span: 16,
          offset: 8,
        },
      },
    };
    if(this.state.redirect&&checkLogin){
      return <Redirect exact push to={loginhref}/>
    }
    return(
      <div>
      <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
      <Row>
      <Col xs={24} sm={{span:8,offset:8}}>
      <div className="mainlogo">
                Homework+
      </div>
      </Col>
      </Row>
      <br/><br/><br/><br/><br/>
      <Row>
      <Col xs={24} sm={8}>
      <Button  className="studententry" onClick={this.showModal} size="large" >学生入口</Button>
      </Col>
      <Col xs={24} sm={8}>
      <Button  className="teacherentry" onClick={this.showModal} size="large" >教师入口</Button>
      </Col>
      <Col xs={24} sm={8}>
      <Button  className="assistantentry" onClick={this.showModal} size="large" >助教入口</Button>
      </Col>
      </Row>
      <Modal
                    title={this.state.loginTitle}
                    visible={this.state.entry}
                    footer={null}
                    onCancel={this.handleCancel}
                    destroyOnClose={true}
            >
      <Form onSubmit={this.handleSubmit}>
      <FormItem
      {...formItemLayout}
      label="用户名"
      >
      {getFieldDecorator('用户名', {
      rules: [{required: true, message: '请输入用户名!',whitespace:true}],
      })(
        <Input placeholder="可以是用户名、手机号或学号" />
      )}
      </FormItem>
      <FormItem
      {...formItemLayout}
      label="密码"
      >
      {getFieldDecorator('密码', {
      rules: [{required: true, message: '请输入密码!',whitespace:true}],
      })(
        <Input type="password" />
      )}
      </FormItem>
      <FormItem {...tailFormItemLayout}>
        <Button className="forgetpassword" onClick={this.handleEnter}>忘记密码？</Button>
      </FormItem>
      <FormItem {...tailFormItemLayout}>
        <Button type="primary" htmlType="submit" className="submit2" >确认</Button>
      </FormItem>
      </Form>
      </Modal>
      <Modal
              title="忘记密码"
              visible={this.state.visible3}
              footer={[
                <Button key="cancel" onClick={this.handleCancel2}>取消</Button>,
                <Button key="submit" type="primary" onClick={this.handleOk}>确认</Button>
              ]}
              onCancel={this.handleCancel2}
              destroyOnClose={true}
            >
      <Input addonBefore="输入用户信息" placeholder="可以是邮箱、学号、用户名、手机号" id="information"/>
      </Modal>
      </div>
    )
  }
}

class Register extends React.Component{
     constructor(props){
         super(props);
         this.state={
             studentRequired:false,
             visible:false,
             visible2:false,
             confirmDirty: false,
             autoCompleteResult: [],
         }
     }
    showModal = () => {
        this.setState({
          visible: true,studentRequired:false,
        });
    }
    handleSubmit=(e)=>{
      e.preventDefault();
      this.props.form.validateFieldsAndScroll((err, values) => {
        if (!err) {
          User["name"]=values.真实姓名;
          User.username=values.用户名;
          User.gender=values.性别;
          User.usertype=values.身份;
          User.password=values.密码;
          User.wechat=values.微信号;
          User.bupt_id=values.学号;
          User.class_number=values.班级号;
          if(User.usertype==="teacher"||User.usertype==="assistant"){
            delete User.bupt_id;
            delete User.class_number;
          }
          User.phone=values.手机号;
          User.email=values.邮箱;
          postUser().catch(function(error){
            console.log(error);
          });
          this.setState({visible:false,visible2:true,});
        }
      });
      
    } 
    handleCancel=()=>{
        this.setState({visible: false});
    }
    handleCancel2 = () => {
        this.setState({visible2:false});
    }
    handleConfirmBlur = (e) => {
        const value = e.target.value;
        this.setState({ confirmDirty: this.state.confirmDirty || !!value });
    }
    validateUsername=(rule,value,callback)=>{
      const form=this.props.form;
      Userlogin.type="username";
      Userlogin.content=form.getFieldValue('用户名');
      loginUser().then(function(response){
        if(value&&response.data.data.repeat){
          callback('该用户名已被注册!');
        }else{
          callback();
        }
      })
      .catch(function(error){
        console.log(error);
      });
    }
    compareToFirstPassword = (rule, value, callback) => {
        const form = this.props.form;
        if (value && value !== form.getFieldValue('密码')) {
          callback('您输入的两个密码不一致!');
        } else {
          callback();
        }
      }
    validateToNextPassword = (rule, value, callback) => {
        const form = this.props.form;
        if (value && this.state.confirmDirty) {
          form.validateFields(['确认密码'], { force: true });
        }
        if(value&&!validPassword.test(value)){
          callback("密码格式不正确(密码必须为6-20位的字母或数字组合)");
        }
        callback();
    }
    checkVaildEmail=(rule,value,callback)=>{
      const form=this.props.form;
      Userlogin.type="email";
      Userlogin.content=form.getFieldValue('邮箱');
      if(value&&!vaildEmail.test(value)){
        callback('您的邮箱格式不正确!');
      }
      loginUser().then(function(response){
        if(value&&response.data.data.repeat){
          callback('该邮箱已被注册!');
        }else{
          callback();
        }
      })      
      .catch(function(error){
        console.log(error);
      });
    }
    checkVaildPhone=(rule,value,callback)=>{
      const form=this.props.form;
      Userlogin.type="phone";
      Userlogin.content=form.getFieldValue('手机号');
      if(value&&!validPhone.test(value)){
        callback('您的手机号格式不正确!');
      }
      loginUser().then(function(response){
        if(value&&response.data.data.repeat){
          callback('该手机号已被注册!');
        }else{
          callback();
        }
      })      
      .catch(function(error){
        console.log(error);
      });
    }
    checkVaildbuptid=(rule,value,callback)=>{
      const form=this.props.form;
      Userlogin.type="bupt_id";
      Userlogin.content=form.getFieldValue('学号');
      if(Userlogin.content!==undefined){
      loginUser().then(function(response){
        if(value&&response.data.data.repeat){
          callback('该学号已被注册!');
        }else{
          callback();
        }
      })      
      .catch(function(error){
        console.log(error);
      });
    }
     if(Userlogin.content===undefined){
     callback();
     }
    }
    checkVaildWechat=(rule,value,callback)=>{
      const form=this.props.form;
      Userlogin.type="wechat";
      Userlogin.content=form.getFieldValue('微信号');
      loginUser().then(function(response){
        if(value&&response.data.data.repeat){
          callback('该微信号已被注册!');
        }else{
          callback();
        }
      })      
      .catch(function(error){
        console.log(error);
      });
    }
    checkStudent=(e)=>{
      if(e.target.value==="student"){
        this.setState({
          studentRequired:true
        },()=>{
          this.props.form.validateFields(['学号'], { force: true });
          this.props.form.validateFields(['班级号'], { force: true });
        });
      }else{
        this.setState({
          studentRequired:false
        },()=>{
          this.props.form.validateFields(['学号'], { force: true });
          this.props.form.validateFields(['班级号'], { force: true });
        });
      }
    }

     render(){
         const { getFieldDecorator } = this.props.form;
         const { autoCompleteResult } = this.state;
         const formItemLayout = {
           labelCol: {
             xs: { span: 24 },
             sm: { span: 8 },
           },
           wrapperCol: {
             xs: { span: 24 },
             sm: { span: 16 },
           },
         };
         const tailFormItemLayout = {
           wrapperCol: {
             xs: {
               span: 24,
               offset: 0,
             },
             sm: {
               span: 16,
               offset: 8,
             },
           },
         };
         return(
             <div>
             <Button type="primary" className="register" onClick={this.showModal} size="large">注册</Button>
             <Modal
                    title="用户注册"
                    visible={this.state.visible}
                    footer={null}
                    onCancel={this.handleCancel}
                    destroyOnClose={true}
            >
            <Form onSubmit={this.handleSubmit}>
            <FormItem
             {...formItemLayout}
             label="真实姓名"
            >
            {getFieldDecorator('真实姓名', {
            rules: [{
              required: true, message: '请输入你的名字!',whitespace:true
            }],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="用户名"
            >
            {getFieldDecorator('用户名', {
            rules: [{
              required: true, message: '请输入你的用户名!',whitespace:true
            }, {
              validator: this.validateUsername,
            }],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="性别"
            >
            {getFieldDecorator('性别', {
            rules: [{
              required: true, message: '请选择性别!',
            }],
            })(
                <RadioGroup >
                <Radio value={"male"}>男</Radio>
                <Radio value={"female"}>女</Radio>
                </RadioGroup>
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="身份"
            >
            {getFieldDecorator('身份', {
            rules: [{
              required: true, message: '请选择你的身份!',
            }],
            })(
                <RadioGroup onChange={this.checkStudent} >
                <Radio value={"student"}>学生</Radio>
                <Radio value={"teacher"}>老师</Radio>
                <Radio value={"assistant"}>助教</Radio>
                </RadioGroup>
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="密码"
            >
            {getFieldDecorator('密码', {
             rules: [{
              required: true, message: '请输入你的密码!',whitespace:true
            }, {
              validator: this.validateToNextPassword,
            }],
             })(
            <Input type="password" />
             )}
             </FormItem>
            <FormItem
             {...formItemLayout}
             label="再次确认密码"
            >
            {getFieldDecorator('确认密码', {
            rules: [{
              required: true, message: '请确认你的密码!',whitespace:true
            }, {
              validator: this.compareToFirstPassword,
            }],
             })(
            <Input type="password" onBlur={this.handleConfirmBlur} />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="微信号"
            >
            {getFieldDecorator('微信号', {
            rules: [{
              required: false, message: '请输入你的微信号!',whitespace:true
            }, {
              validator: this.checkVaildWechat,
            }],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="学号(如是学生请填)"
            >
            {getFieldDecorator('学号', {
            rules: [{
              required: this.state.studentRequired, message: '请输入你的学号!',whitespace:true
            }, {
              validator: this.checkVaildbuptid,
            }],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="班级号(如是学生请填)"
            >
            {getFieldDecorator('班级号', {
            rules: [{
              required: this.state.studentRequired, message: '请输入你的班级号!',whitespace:true
            }],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="手机号码"
            >
            {getFieldDecorator('手机号', {
            rules: [{
              required: true, message: '请输入你的手机号!',whitespace:true
            },{
              validator: this.checkVaildPhone,
            }
          ],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="邮箱"
            >
            {getFieldDecorator('邮箱', {
            rules: [{
              required: true, message: '请输入邮箱地址!',whitespace:true
            },{
              validator: this.checkVaildEmail,
            }
          ],
            })(
            <Input />
            )}
            </FormItem>
            <FormItem {...tailFormItemLayout}>
            <Button type="primary" htmlType="submit" className="submit">注册</Button>
            </FormItem>
            </Form>
            </Modal>
            <Modal
                  title="邮箱验证"
                  visible={this.state.visible2}
                  footer={[<Button key="back" onClick={this.handleCancel2}>确认</Button>,]}
                  onCancel={this.handleCancel2}
            >
            <p>已发送验证邮件至邮箱，请及时查看确认注册</p>
            </Modal>
             </div>
         )
     }
}

const WrappedRegister = Form.create()(Register);
const WrappedLogin=Form.create()(Login);

class Topfield extends React.Component
{   

    render()
    {
        return (
            <div>
            <WrappedRegister/>
            <WrappedLogin/>
            </div>
        );
        
    }
}

const Main=()=>(
  <main>
    <Switch>
      <Route exact path='/' component={Topfield}/>
      <Route path='/emailcheck' component={ValidateEmail}/>
      <Route path='/forgetpassword' component={WrappedModifyPassword}/>
      <Route path='/studentcenter' component={StudentIndex}/>
    </Switch>
  </main>
)

ReactDOM.render((
<BrowserRouter>
<Main/>
</BrowserRouter>
),document.getElementById('root'));
registerServiceWorker();
