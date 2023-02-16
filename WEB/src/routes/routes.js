import routesAdmin from './routes.admin';
import routesCliente from "./routes.cliente";
import {Error404} from '../Pages';
import {BasicLayout} from '../Layouts';



const routes =[...routesAdmin, ...routesCliente, {
    layout: BasicLayout,
    component: Error404
}];
export default routes;