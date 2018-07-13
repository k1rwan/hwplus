import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import {Modal,Button,Input,Tag,Form,Tooltip,Icon,Cascader,Select,Row,Col,Checkbox,AutoComplete,Radio}from'antd'
const FormItem = Form.Item;
const Option = Select.Option;
const AutoCompleteOption = AutoComplete.Option;
const RadioGroup = Radio.Group;

var User={username:'',gender:'male',usertype:'student',password:'',wechat:'',bupt_id:'',class_number:'',email:'',phone:''};
var vaildEmail=/^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/;

class Register extends React.Component{
     constructor(props){
         super(props);
         this.state={
             visible:false,
             confirmDirty: false,
             autoCompleteResult: [],
         }
        this.showModal=this.showModal.bind(this);
        this.handleCancel=this.handleCancel.bind(this);
        this.handleSubmit=this.handleSubmit.bind(this);
     }
    showModal = () => {
        this.setState({
          visible: true,
        });
    }
    handleSubmit(e){
      e.preventDefault();
      this.props.form.validateFieldsAndScroll((err, values) => {
        if (!err) {
          //console.log('Received values of form: ', values);
          User.username=values.姓名;
          User.gender=values.性别;
          User.usertype=values.身份;
          User.password=values.密码;
          User.wechat=values.微信号;
          User.bupt_id=values.学号;
          User.class_number=values.班级号;
          User.phone=values.手机号;
          User.email=values.邮箱;
          this.setState({visible: false});
        }
      });
      
    } 
    handleCancel(e){
        this.setState({visible: false});
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
        callback();
    }
    checkVaildEmail=(rule,value,callback)=>{
      const form=this.props.form;
      if(value&&!vaildEmail.test(value)){
        callback('您的邮箱格式不正确!');
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

     render(){
         console.log(User);
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
             label="姓名"
            >
            {getFieldDecorator('姓名', {
            rules: [{
              required: true, message: '请输入你的名字!',
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
                <RadioGroup >
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
              required: false, message: '请输入你的学号!',
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
              required: false, message: '请输入你的班级号!',
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
            }],
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
             </div>
         )
     }
}

const WrappedRegister = Form.create()(Register);

class Topfield extends React.Component
{   
    constructor(props){
        super(props);
    }
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
