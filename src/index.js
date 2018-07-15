import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import {Modal,Button,Input,Tag,Form,Tooltip,Icon,Cascader,Select,Row,Col,Checkbox,AutoComplete,Radio}from'antd'
import axios from 'axios';
const FormItem = Form.Item;
const Option = Select.Option;
const AutoCompleteOption = AutoComplete.Option;
const RadioGroup = Radio.Group;

var User={name:'',username:'',gender:'male',usertype:'student',password:'',wechat:'',bupt_id:'',class_number:'',email:'',phone:''};
var vaildEmail=/^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/;
var validPhone=/^1\d{10}$/;
var validPassword =/^\w{6,20}$/;
var postUser=axios.create({
  url:"http://108.160.130.164:8082/data/users/",
  headers:{"content-type":"application/json"},
  method:'post',
  data:User,
  timeout:1000,
});

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
          User.phone=values.手机号;
          User.email=values.邮箱;
          console.log(User);
          postUser().then(function(response){
            console.log(response);
          })
          .catch(function(error){
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
      if(value&&!vaildEmail.test(value)){
        callback('您的邮箱格式不正确!');
      }
      callback();
    }
    checkVaildPhone=(rule,value,callback)=>{
      const form=this.props.form;
      if(value&&!validPhone.test(value)){
        callback('您的手机号格式不正确!');
      }
      callback();
    }
    handleWebsiteChange = (value) => {
        let autoCompleteResult;
        if (!value) {
          autoCompleteResult = [];
        } else {
          autoCompleteResult = ['.com', '.org', '.net'].map(domain => `${value}${domain}`);
        }
        this.setState({ autoCompleteResult });
    }
    checkStudent=(e)=>{
      if(e.target.value==="student"){
        this.setState({studentRequired:true});
      }else{
        this.setState({studentRequired:false});
      }
    }

     render(){
         //console.log(User);
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
              required: true, message: '请输入你的名字!',
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
              required: true, message: '请输入你的用户名!',
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
                <Radio value={"assistent"}>助教</Radio>
                </RadioGroup>
            )}
            </FormItem>
            <FormItem
             {...formItemLayout}
             label="密码"
            >
            {getFieldDecorator('密码', {
             rules: [{
              required: true, message: '请输入你的密码!',
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
              required: true, message: '请确认你的密码!',
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
              required: true, message: '请输入你的微信号!',
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
              required: this.state.studentRequired, message: '请输入你的学号!',
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
              required: this.state.studentRequired, message: '请输入你的班级号!',
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
              required: true, message: '请输入你的手机号!',
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
              required: true, message: '请输入邮箱地址!',
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

class Topfield extends React.Component
{   
    render()
    {
        return (
            <div>
            <WrappedRegister/>
            <div className="logo">
                Homework+
            </div>
            </div>
        );
        
    }
}
ReactDOM.render(<Topfield />, document.getElementById('root'));
registerServiceWorker();
