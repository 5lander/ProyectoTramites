import React from 'react'
import { useEffect, useState } from 'react'
import './Tramites.scss'
import {Grid,Card,Icon} from 'semantic-ui-react'


export function Tramites() {

    const[data,setData]=useState([]);

    useEffect(()=>{
        fetch("http://127.0.0.1:8000/administrativo/api/tramites")
        .then((response)=>response.json())
        .then((data)=>{setData(data)})
        // .then((data)=>console.log(data))
    })
    return (
      <div className='contenedorTramites'>
        <Grid className='organizador' columns={4} divided >
              {data.map((item) => (
                <div key={item.id}>
                    <Card className='organizadortarjeta'>
                      <Card.Content>
                        <Card.Header>{item.nombreT}</Card.Header>
                        <Card.Meta>{item.descripcion}</Card.Meta>
                        <Card.Description className='descripcion'>
                          Cuantos dias demora:{item.tiempoestimado}
                        </Card.Description>
                        <Card.Description className='descripcion'>
                          El costo de este tramites es de:{item.costo}
                        </Card.Description>
                      </Card.Content>
                      <Card.Content extra>
                        <a href='/pedidoTramite'>
                        <button class="ui button">
                          <Icon name='triangle right' />
                          Pedir Tramite
                          </button>
                        </a>
                      </Card.Content>
                    </Card>
              </div>
                        ))}
        </Grid>
      </div>
    
       
        
      )
  }