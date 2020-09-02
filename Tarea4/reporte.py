import os
import json
import webbrowser



allatrib = ['nombre','edad','activo','saldo']

arreglodatos =[]

def openfile():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "registro.json")
    with open (path) as data: 
        tmpFile = json.loads(data.read())   
        for newData in tmpFile:              
            arreglodatos.append(newData)


codinicio = """<!DOCTYPE html>

<head>
<style>

body{
    background-image: url("fondo.jpg");
    background-size: cover ;
    font-family:  Helvetica;
    text-align: center;
}
.fondo {
    position: absolute;
	left:50%;
	top:50%;
	transform: translate(-50%,-50%);
    background-color: rgba(255, 255, 255, 0.9);
	border-radius:15px;
    padding:25px 80px;
    }

th, td {
    text-align: left;
    padding: 8px;
    }

    tr:nth-child(even) {background-color: #f2f2f2;}
    </style>
</head>

<body>
    <div class="fondo">
        <form>
        <table  >
                <tr>
                    <td>NOMBRE</td> 
                    <td>EDAD</td>
                    <td>ACTIVO</td>
                    <td>PROMEDIO</td>
                </tr>
                <tr>"""

 
final_hmtl = """                
                </tr>
        </table>
    </form>
    </div>
</body>
</html>"""

def crearReporte():
    openfile()
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "reporteTablas.html")
    with  open(path, 'w+') as file_reporte:
        file_reporte.write(codinicio)
        for data in arreglodatos:    
            file_reporte.write("<tr>")                                    
            for atributo in allatrib:
                file_reporte.write("<td>" + str(data.get(atributo)) + "</td>")
            
            file_reporte.write("</tr>")
        file_reporte.write(final_hmtl)
        file_reporte.close()
    webbrowser.open_new(path)



           
crearReporte()