import React from 'react';
import ReactDOM from 'react-dom';
import './studentcenter.css';
import { Upload, Icon, message,Row,Col,Button,Modal,Form,Input } from 'antd';
import axios from 'axios';

var pass={old_pass:"",new_pass:""};
const FormItem = Form.Item;
var validPassword =/^\w{6,20}$/;
function getBase64(img, callback) {
    const reader = new FileReader();
    reader.addEventListener('load', () => callback(reader.result));
    reader.readAsDataURL(img);
}

function beforeUpload(file) {
    const isJPG = file.type === 'image/jpeg';
    if (!isJPG) {
      message.error('你只能上传jpg格式的头像!');
    }
    const isLt2M = file.size / 1024 / 1024 < 2;
    if (!isLt2M) {
      message.error('图片大小不得大于2MB!');
    }
    return isJPG && isLt2M;
}

class UploadAvatar extends React.Component {
    constructor(props){
      super(props)
      this.state={
        loading: false,
      }
    }
  　　　
    handleChange = (info) => {
      if (info.file.status === 'uploading') {
        this.setState({ loading: true });
        return;
      }
      if (info.file.status === 'done') {
        getBase64(info.file.originFileObj, imageUrl => this.setState({
          imageUrl,
          loading: false,
        }));
      }
    }
  
    render() {
      const uploadButton = (
        <div>
          <Icon type={this.state.loading ? "loading" : "plus" }/>
          <div>添加头像</div>
        </div>
      );
      const imageUrl = this.state.imageUrl;
      return (
        //upload的data应该是一个参数对象或者是返回参数对象的方法
        <Upload
          name="avatar"
          listType="picture-card"
          className="avatar-uploader"
          showUploadList={false}
          action="http://106.14.148.208:8080/data/avatars/"
          data={{"user":this.props.userinformation["id"]}}
          headers={{"content-type":"application/json","token":localStorage.getItem('token')}}
          beforeUpload={beforeUpload}
          onChange={this.handleChange}
        >
          {imageUrl ? <img src={imageUrl} alt="头像" /> : uploadButton}
        </Upload>
      );
    }
  }

class Studentcenter extends React.Component{
    constructor(props){
      super(props);
      this.state={
        visible1:false,
        visible2:false,
        confirmDirty:false,
      }
    }
    
    showModal1=()=>{
      this.setState({visible1:true});
    }

    showModal2=()=>{
      this.setState({visible2:true});
    }

    handleCancel1=()=>{
      this.setState({visible1:false});
    }

    handleCancel2=()=>{
      this.setState({visible2:false});
    }

    handleConfirmBlur = (e) => {
      const value = e.target.value;
      this.setState({ confirmDirty: this.state.confirmDirty || !!value });
    }
    compareToFirstPassword = (rule, value, callback) => {
      const form = this.props.form;
      if (value && value !== form.getFieldValue('新的密码')) {
        callback('您输入的两个密码不一致!');
      } else {
        callback();
      }
    }
    validateToNextPassword = (rule, value, callback) => {
      const form = this.props.form;
      if (value && this.state.confirmDirty) {
        form.validateFields(['再次确认'], { force: true });
      }
      if(value&&!validPassword.test(value)){
        callback("密码格式不正确(密码必须为6-20位的字母或数字组合)");
      }
      callback();
   }

     handleSubmit1=(e)=>{
       e.preventDefault();
       this.props.form.validateFieldsAndScroll((err,values)=>{
          if(!err){
              pass.old_pass=values.原密码;
              pass.new_pass=values.新的密码;
              var changePass=axios.create({
                url:"http://106.14.148.208:8080/account/change_password/",
                headers:{"content-type":"application/json","token":localStorage.getItem('token')},
                method:'post',
                data:pass,
                timeout:1000,
              })
              changePass().then(function(response){
                message.success('密码修改成功!',3);
              })
              .catch(function(error){
                message.error('密码修改失败，可能是由于您的原密码不符',3);
              })
              this.setState({visible1:false});
          }
       });
     }

    render(){
      const { getFieldDecorator } = this.props.form;
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
            //背景以后会有专门的壁纸
            <div>
            <div style={{ textAlign: 'center' }}>
              <Row>
                <Col xs={24} sm={6}>
                   <div className='uploadavatar'>
                   <UploadAvatar userinformation={this.props.userinformation} />
                   </div>
                </Col>
                <Col xs={24} sm={6}>
                   <div style={{"font-size":"16px","margin-top":"30px",position:"relative"}}>
                   用户名
                   <span style={{ "margin-left":"20px","border-style":"solid","border-width":"thin","padding-left":30,"padding-right":30,"border-color":"#AAAAAA"}}>
                   {this.props.userinformation.username}
                   </span>
                   </div>
                   <div style={{"font-size":"16px","margin-top":"30px",position:"relative"}}>
                   班级
                   <span style={{ "margin-left":"20px","border-style":"solid","border-width":"thin","padding-left":30,"padding-right":30,"border-color":"#AAAAAA"}}>
                   {this.props.userinformation.class_number}
                   </span>
                   </div>
                </Col>
                <Col xs={24} sm={6}>
                   <div style={{"font-size":"16px","margin-top":"30px",position:"relative"}}>
                   学号
                   <span style={{ "margin-left":"20px","border-style":"solid","border-width":"thin","padding-left":30,"padding-right":30,"border-color":"#AAAAAA"}}>
                   {this.props.userinformation.bupt_id}
                   </span>
                   </div>
                   <div style={{"font-size":"16px","margin-top":"30px",position:"relative"}}>
                   邮箱
                   <span style={{ "margin-left":"20px","border-style":"solid","border-width":"thin","padding-left":30,"padding-right":30,"border-color":"#AAAAAA"}}>
                   {this.props.userinformation.email}
                   </span>
                   </div>
                   <div style={{"font-size":"16px","margin-top":"30px",position:"relative"}}>
                   手机号
                   <span style={{ "margin-left":"20px","border-style":"solid","border-width":"thin","padding-left":30,"padding-right":30,"border-color":"#AAAAAA"}}>
                   {this.props.userinformation.phone}
                   </span>
                   </div>
                </Col>
                <Col xs={24} sm={6}>
                   <Button style={{"margin-top":"30px"}} onClick={this.showModal1}>修改密码?</Button>
                   <br/>
                   <Button style={{"margin-top":"15px"}} onClick={this.showModal2}>变更信息</Button>
                </Col>
              </Row>
            </div>
            <Modal
              title="修改密码"
              visible={this.state.visible1}
              footer={null}
              onCancel={this.handleCancel1}
              destroyOnClose={true}
            >
              <Form onSubmit={this.handleSubmit1}>
                <FormItem
                  {...formItemLayout}
                  label="原密码"
                >
                {getFieldDecorator('原密码', {
                rules: [{required: true, message: '请输入密码!',whitespace:true}],
                 })(
                <Input type="password" />
                )}
                </FormItem>
                <FormItem
                  {...formItemLayout}
                  label="新的密码"
                >
                {getFieldDecorator('新的密码', {
                rules: [{
                  required: true, message: '请输入密码!',whitespace:true
                },{
                  validator:this.validateToNextPassword,
                }],
                 })(
                <Input type="password" />
                )}
                </FormItem>
                <FormItem
                  {...formItemLayout}
                  label="再次确认"
                >
                {getFieldDecorator('再次确认', {
                rules: [{
                  required: true, message: '请输入密码!',whitespace:true
                },{
                  validator:this.compareToFirstPassword,
                }],
                 })(
                <Input type="password" onBlur={this.handleConfirmBlur} />
                )}
                </FormItem>
                <FormItem {...tailFormItemLayout}>
                   <Button type="primary" htmlType="submit" className="submit2" >确认</Button>
                </FormItem>
              </Form>
            </Modal>
            </div>
        )
    }
}
const WrappedStudentcenter=Form.create()(Studentcenter);
export default WrappedStudentcenter
