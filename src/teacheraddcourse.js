import React from 'react';
import ReactDOM from 'react-dom';
import './teacheraddcourse.css';
import {Row,Col,Button,Form,Input,Select} from 'antd';
import axios from 'axios';

const FormItem = Form.Item;
const Option=Select.Option;
const children=[];
var lastUpdateteachersusername=[];//最后更新时教师的名字列表

class SelectTeacher extends React.Component{
    constructor(props){
        super(props);
    }

    componentDidMount(){
      var getTeachersusername=axios.create({
        url:"http://homeworkplus.cn/graphql/",
        headers:{"content-type":"application/json","token":localStorage.getItem('token'),"Accept":"application/json"},
        method:'post',
        data:{
           "query":`query{
             getUsersByUsertype(usertype:"teacher")
             {
               username
             }
            }`      
        },
        timeout:1000,
      })
      getTeachersusername().then(function(response){
        if(JSON.stringify(lastUpdateteachersusername)!==JSON.stringify(response.data.data.getUsersByUsertype)){
         lastUpdateteachersusername=response.data.data.getUsersByUsertype;
         for(let i=0;i<response.data.data.getUsersByUsertype.length;i++){
          children.push(<Option key={response.data.data.getUsersByUsertype[i].username}>{response.data.data.getUsersByUsertype[i].username}</Option>);
         }
        }
      })
      .catch(function(error){
         console.log(error);
      })
    }

    render(){
        return(
          <Select
          mode="multiple"
          style={{ width: '100%' }}
          placeholder="请选择授课的教师，可以多选"
          defaultValue={this.props.defaultTeacher}
        >
          {children}
          </Select>
        )
    }
}

class Addcourse extends React.Component{

    handleSubmit=(e)=>{
        e.preventDefault();
        this.props.form.validateFieldsAndScroll(["课程名称","授课教师"],(err,values)=>{
            console.log(values);
        })
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
        return(
          <div>
            <div style={{fontSize:"28px",marginLeft:"20px",marginTop:"10px",marginBottom:"5px"}}>新建课程</div>
            <Form onSubmit={this.handleSubmit}>
            <Row gutter={200}>
             <Col xs={24} sm={11}>
               <FormItem 
                 {...formItemLayout}
                 label="课程名称"
               >
                {getFieldDecorator('课程名称', {
                rules: [{
                  required: true, message: '请输入想要创建课程的名称!',whitespace:true
                }],
                 })(
                <Input/>
                )} 
                </FormItem>
             </Col>
             <Col xs={24} sm={11}>
               <FormItem 
                 {...formItemLayout}
                 label="授课教师"
               >
                {getFieldDecorator('授课教师', {
                rules: [{
                  required: true, message: '请输入想要创建课程的名称!',whitespace:true
                }],
                 })(
                <SelectTeacher defaultTeacher={this.props.userinformation.username}/>
                )} 
                </FormItem>
             </Col>
            </Row>
               <FormItem
                 wrapperCol={{
                   xs: { span: 24, offset: 0 },
                   sm: { span: 16, offset: 8 },
                 }}
               >
                <Button type="primary" htmlType="submit">提交</Button>
               </FormItem>
            </Form>
          </div> 
        )
    }
}

const WrappedAddcourse=Form.create()(Addcourse);
export default WrappedAddcourse