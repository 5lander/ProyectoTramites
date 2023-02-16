import React from 'react'
import {Form, FormGroup, Label,Input} from 'reactstrap'
import { Button } from 'semantic-ui-react'
import './PedidoTramite.scss'
//onSubmit={this.props.Tramite ? this.editarTramite :this.crearTramite}
export class PedidoTramite extends React.Component {

  tramite={
    'nombres':'',
    'apellidos':'',
    'cedula':'',
    'celular':'',
    'nacionalidad':'',
    'correo':'',
    'edad ':'',
    'descripcion':''
  };
  componentePermanente(){
    if(this.props.tramite){
      const{nombres,apellidos,cedula,celular,
        nacionalidad,correo,edad,descripcion
    }=this.props.tramite
      this.settramite(
        {nombres,apellidos,cedula,celular,
          nacionalidad,correo,edad,descripcion}
      )
    }
  }
  onChange =e => {
    this.settramite({[e.target.name]: e.target.value });


  }

creartramite = e =>{
 //   e.preventDefault();
   // axios.put('http://127.0.0.1:8000/administrativo/api/Tramites'+ this.Tramite.id,this.Tramite)
  //  .then(()=>{})
}

  render(){ 
  return (
    <div>
        <Form className='formopciones'>
            <FormGroup>
                <Label for='nombres'>Ingrese sus nombres</Label>      
                <Input type="text" name="nombres" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='apellidos'>Ingrese sus apellidos</Label>      
                <Input type="text" name="apellidos" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='cedula'>Ingrese su cedula</Label>      
                <Input type="text" name="cedula" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='celular'>Ingrese su numero de celular</Label>      
                <Input type="text" name="celular" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='nacionalidad'>Que nacionalidad tiene</Label>      
                <Input type="text" name="nacionalidad" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='correo'>Ingrese su correo Personal</Label>      
                <Input type="text" name="correo" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='edad'>Que edad tiene</Label>      
                <Input type="text" name="edad" onChange={this.onChange}></Input>          
            </FormGroup>
            <FormGroup>
                <Label for='descripcion'>Para que necesita el tramite</Label>      
                <Input type="text" name="descripcion" onChange={this.onChange}></Input>          
            </FormGroup>
            <Button className="volver">
                <a href="javascript:history.back(-1)">
                  Regresar
                </a>
            </Button>
            <Button>Enviar Tramites</Button>
        </Form>
    </div>
  )
}
  }