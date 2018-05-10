import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import {Modal,Button,Input,Tag,Form,Tooltip,Icon,Cascader,Select,Row,Col,Checkbox,AutoComplete}from'antd'
const FormItem = Form.Item;
var User={username:'',gender:'',usertype:'',password:'',wechat:'',bupt_id:'',class_number:'',email:'',phone:''};
class Register extends React.Component{
     constructor(props){
         super(props);
         this.state={
             visible:false,
             User:this.props.User,
         }
        this.showModal=this.showModal.bind(this);
        this.handleOk=this.handleOk.bind(this);
        this.handleCancel=this.handleCancel.bind(this);
     }
    showModal = () => {
        this.setState({
          visible: true,
        });
    }
    handleOk(e){
        this.setState({visible: false});
    }
    handleCancel(e){
        this.setState({visible: false});
    }

     render(){
         return(
             <div>
             <Button type="primary" className="register" onClick={this.showModal} size="large">注册</Button>
             <Modal
                    title="用户注册"
                    visible={this.state.visible}
                    onOk={this.handleOk}
                    onCancel={this.handleCancel}
                    footer={[
                        <Button onClick={this.handleCancel}>取消</Button>,
                        <Button type="primary" onClick={this.handleOk}>确认</Button>,
                      ]}
            >
            </Modal>
             </div>
         )
     }
}

class Topfield extends React.Component
{   
    constructor(props){
        super(props);
        this.state={
            User:User,
        }
    }
    render()
    {
        return (
            <div>
            <Register User={this.state.User}/>
            <div className="logo">
                Homework+
            </div>
            </div>
        );
        
    }
}
ReactDOM.render(<Topfield />, document.getElementById('root'));
registerServiceWorker();
