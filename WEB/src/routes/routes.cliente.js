import { ClienteLayout } from '../Layouts'
import { Home, PedirTramite  } from '../Pages/Cliente'

const routesCliente = [
    {
        path:"/",
        layout : ClienteLayout,
        component: Home,
    },

    {
        path:"/pedidoTramite",
        layout : ClienteLayout,
        component: PedirTramite,
    },
];

export default routesCliente;   