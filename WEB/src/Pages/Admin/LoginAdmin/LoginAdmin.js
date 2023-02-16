import React from 'react';
import './LoginAdmin.scss';
import { Loginform } from '../../../Componentes/Admin';
import {Header,Footer} from '../../../Componentes/Cliente'
export function LoginAdmin(props) {
    return (  
    <div>
     <Header/>
        <div className='login-admin'>
          <div className='login-admin__content'>
          Inicio de Sesion
            <Loginform/>
            
          </div>
          
        </div>
        <Footer/>


    </div>
  )
}
