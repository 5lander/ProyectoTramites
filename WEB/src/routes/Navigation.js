import React from 'react'
import {BrowserRouter as Router, Routes,Route} from 'react-router-dom'
import routes from './routes'
import {map} from 'loadsh'

export function Navigation() {
    console.log('salida',routes)
  return (
    <Router>
        <Routes>
            {
                map(routes,(route,index)=>(
                    <Route
                    key={index}
                    path={route.path}
                    element={
                        <route.layout>
                            <route.component/>
                        </route.layout>
                    }>

                    </Route>
                )
                )
            }
            
        </Routes>
    </Router>
  )
}
