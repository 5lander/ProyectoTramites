import { AdminLayout } from "../Layouts"
import { HomeAdmin } from "../Pages/Admin/"
const routesAdmin=[
    {
        path: '/admin',
        layout: AdminLayout,
        components: HomeAdmin,
        exac: true,
    },
];
export default routesAdmin;