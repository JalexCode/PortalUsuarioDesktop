# CONSTANTES
from data.DataEU import DataEU
import os

VERSION = "b1.0"
APP_NAME = "PortalUsuario Desktop"
APP_ID = "_".join(APP_NAME.lower().split())
APP_WOS_NAME = "".join(APP_NAME.split()) # app 'without spaces' name
AUTHOR = "Javier Alejandro González Casellas"
TELEGRAM_CHANNEL = "https://t.me/portalusuario"
TELEGRAM_GROUP_SUPPORT = "https://t.me/portalusuarioBT"
DEVELOPER_TELEGRAM = "https://t.me/jalexcode"
DEVELOPER_TELEGRAM_CHANNEL = "https://t.me/jalexcodesolutions"
USER_PATH = os.path.expanduser('~')
APP_DATA = os.path.join(USER_PATH, "AppData", "Local", APP_ID)
APK_PACKAGE = "com.marlon.portalusuario"
# CONEXION
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"

NATIONAL_SITES_LIST = [DataEU(0, "www.cubarte.cult.cu", "Cuenta con un Repositorio de información de la cultura cubana (se almacenan películas, imágenes, audio, texto, libros, etc.)\nEl usuario interesado lo podrá visualizar en tiempo real y descargar."),
DataEU(1, "www.lapapeleta.cult.cu", "Información sobre la cartelera cultural del país."),
DataEU(2, "www.bellasartes.cult.cu", "Sitio de promoción del Museo Nacional de Bellas Artes."),
DataEU(3, "www.sitiosculturales.cult.cu", "Directorio web de la cultura cubana:\nPortal Cubarte\nCartelera “La papeleta”\nSitios de interés\nPara descargar\nPublicaciones digitales\nPortales temáticos\nPortales territoriales"),
DataEU(4, "www.premioslucas.icrt.cu", "Portal del video clip cubano."),
DataEU(5, "www.cubacine.cult.cu", "Portal del cine cubano. ICAIC (Instituto Cubano de Arte e Industria Cinematográfica)"),
DataEU(6, "www.casa.cult.cu", "Divulga e informa todos los contenidos de la Casa de las Américas en sus diferentes áreas de trabajo y proyecciones."),
DataEU(7, "www.tvcubana.icrt.cu", "Portal de la TV Cubana. Cartelera de los canales de televisión"),
DataEU(8, "www.mujeres.co.cu", "Divulga temáticas relacionadas con el papel de la mujer en la defensa de la Revolución. También aborda las complejidades del proceso de transformación de roles, estereotipos y juicios de valor signado por la cultura tradicional, y contribuye a la formación de la mujer. "),
DataEU(9, "www.juventudtecnica.cu", "Publicación cubana sobre el quehacer de los jóvenes y el desarrollo de la ciencia, la tecnología y el medio ambiente.  "),
DataEU(10, "www.videojuego.cu", "Portal de videojuegos cubanos desarrollado por los Estudios de Animación ICAIC y la Universidad de la Ciencias Informáticas (UCI). "),
DataEU(11, "www.fac.cu", "Sitio de la Fábrica de Arte Cubano donde podrá conocer su programación y otras informaciones."),
DataEU(12, "www.jit.cu", "Actualidad del deporte cubano."),
DataEU(13, "www.circonacionaldecuba.cu", "Programación, eventos y otras informaciones sobre el Circo Nacional de Cuba."),
DataEU(14, "www.somosjovenes.cu", "Revista digital con informaciones de interés para la juventud cubana."),
DataEU(15, "www.cubadebate.cu", "Información diaria y debate sobre temas de interés del país.\nEs el sitio donde enterarse de las noticias de actualidad en Cuba. "),
DataEU(16, "www.granma.cu", "Principal diario del país.\nPromueve la obra de la Revolución y sus principios, las conquistas alcanzadas por nuestro pueblo y la integridad y cohesión de todo nuestro pueblo junto al Partido y a Fidel. "),
DataEU(17, "www.juventudrebelde.cu", "Diario de la juventud cubana que igual interesa a los demás. "),
DataEU(18, "www.trabajadores.cu", "Diario de la CTC con informaciones del sector laboral y otras noticias de interés general. "),
DataEU(19, "www.cubasi.cu", "Portal Cuba sí con informaciones de Cuba y el mundo "),
DataEU(20, "www.prensa-latina.cu", "Agencia informativa latinoamericana "),
DataEU(21, "www.etecsa.cu", "Informaciones de sus productos y servicios, así como las ofertas o promociones que existan en ese momento. "),
DataEU(22, "www.pamarillas.cu", "Directorio telefónico donde podrá encontrar información comercial, clasificada por categorías de productos y servicios."),
DataEU(23, "www.redcuba.cu", "Es una plataforma que integra los servicios web disponibles en la red cubana.\nFacilita la búsqueda de contenidos en varios formatos digitales (páginas web, imágenes y documentos) "),
DataEU(24, "www.aduana.gob.cu", "Mantiene informados a los usuarios acerca de las disposiciones y procedimientos vigentes de la ADUANA y los cambios que puedan surgir."),
DataEU(25, "www.correos.cu", "Información sobre las oficinas de correos, sus códigos postales y los servicios de su organización."),
DataEU(26, "www.segurmatica.cu", "Descargar Antivirus y actualizaciones. "),
DataEU(10, "www.ofertas.cu", "Clasificados en Cuba\nPueden publicar su publicidad (ventas, compras y rentas) "),
DataEU(27, "www.andariego.cu", "Navegador cubano  de  Mapas y  gestor de Destinos. "),
DataEU(28, "www.bc.gob.cu", "Información bancaria de gran utilidad para la población cubana: Tipos de cambios oficiales, nuevas denominaciones de billetes y monedas para la identificación de las medidas de seguridad, legislación bancaria, sistema bancario y política monetaria."),
DataEU(29, "www.entumovil.cu", "Brinda una gama de servicios de valor agregado mediante SMS y aplicaciones para móviles. "),
DataEU(30, "www.cubahora.cu", "Primera revista digital con temas de la actualidad nacional e internacional."),
DataEU(31, "www.insmet.cu", "Información meteorológica y climática sobre el estado y comportamiento futuro de la atmósfera. "),
DataEU(32, "www.cubaeduca.cu", " Programa completo de las asignaturas, desde el primer hasta el duodécimo grado, incluyendo la preparación para las pruebas de ingreso.\nEs una opción de búsqueda, de facilitación del proceso de enseñanza – aprendizaje. "),
DataEU(33, "www.repasador.cubaeduca.cu", "Servicio atendido por profesionales de la educación, que responderán y ayudarán a resolver tareas a los estudiantes que lo necesiten de las asignaturas fundamentales de nuestra enseñanza. "),
DataEU(34, "www.ecured.cu", "Su principal contribución es la digitalización de varios documentos e información de temas históricos, culturales y artísticos, tanto de interés global como local.\nEn el sitio está disponible para descargar EcuRed Portátil y EcuMóvil (versión portable para los teléfonos móviles con sistema Android que funciona sin conexión a Internet) "),
DataEU(35, "www.infomed.sld.cu", "Dirigido a los profesionales de la salud pues cuenta con información relacionada con esta temática. "),
DataEU(36, "www.medioambiente.cu", "Propicia una mayor difusión  de la información ambiental cubana y a la vez, muestra los logros del país en este importante tema. "),
DataEU(37, "www.redciencia.cu", "Ofrece contenidos y servicios de información concebidos como un espacio de colaboración e interacción con instituciones, científicos y otros profesionales de Cuba y el resto del mundo, así como lectores en general interesados en estos temas, entre los que se destacan algunos de renovada importancia como: Ornitología, Energía, Ciencias Sociales, Ciencias Meteorológicas, entre otros."),
DataEU(38, "www.eduniv.mes.edu.cu", "Repositorio institucional del Ministerio de Educación Superior (MES).\nContiene libros publicados por la Editorial Universitaria, tesis de doctorado aprobadas por la Comisión Nacional de Grados Científicos de Cuba, artículos y revistas."),
DataEU(38, "www.uci.cu", "Portal de la Universidad de Ciencias Informáticas.")]

MUNICIPALITIES = {"Pinar del Río": ["Consolación del Sur", "Guane", "La Palma", "Los Palacios", "Mantua", "Minas de Matahambre", "Pinar del Río", "San Juan y Martínez", "San Luis", "Sandino", "Viñales"], "Artemisa": ["Alquízar", "Artemisa", "Bauta", "Caimito", "Guanajay", "Güira de Melena", "Mariel", "San Antonio de los Baños", "Bahía Honda", "San Cristóbal", "Candelaria"], "Mayabeque": ["Batabanó", "Bejucal", "Güines", "Jaruco", "Madruga", "Melena del Sur", "Nueva Paz", "Quivicán", "San José de las Lajas", "San Nicolás de Bari", "Santa Cruz del Norte"], "La Habana": ["Arroyo Naranjo", "Boyeros", "Centro Habana", "El Cerro", "Cotorro", "Diez de Octubre", "Guanabacoa", "Habana del Este", "Habana Vieja", "La Lisa", "Marianao", "Playa", "Plaza", "Regla", "San Miguel del Padrón"], "Matanzas": ["Calimete", "Cárdenas", "Ciénaga de Zapata", "Colón", "Jagüey Grande", "Jovellanos", "Limonar", "Los Arabos", "Martí", "Matanzas", "Pedro Betancourt", "Perico", "Unión de Reyes"], "Villa Clara": ["Caibarién", "Camajuaní", "Cifuentes", "Corralillo", "Encrucijada", "Manicaragua", "Placetas", "Quemado de Güines", "Ranchuelo", "Remedios", "Sagua la Grande", "Santa Clara", "Santo Domingo"], "Cienfuegos": ["Abreus", "Aguada de Pasajeros", "Cienfuegos", "Cruces", "Cumanayagua", "Palmira", "Rodas", "Lajas"], "Sancti Spíritus": ["Cabaiguan", "Fomento", "Jatibonico", "La Sierpe", "Sancti Spíritus", "Taguasco", "Trinidad", "Yaguajay"], "Ciego de Ávila": ["Ciro Redondo", "Baraguá", "Bolivia", "Chambas", "Ciego de Ávila", "Florencia", "Majagua", "Morón", "Primero de Enero", "Venezuela"], "Camagüey": ["Camagüey", "Carlos Manuel de Céspedes", "Esmeralda", "Florida", "Guaimaro", "Jimagüayú", "Minas", "Najasa", "Nuevitas", "Santa Cruz del Sur", "Sibanicú", "Sierra de Cubitas", "Vertientes"], "Las Tunas": ["Amancio Rodríguez", "Colombia", "Jesús Menéndez", "Jobabo", "Las Tunas", "Majibacoa", "Manatí", "Puerto Padre"], "Holguín": ["Antilla", "Báguanos", "Banes", "Cacocum", "Calixto García", "Cueto", "Frank País", "Gibara", "Holguín", "Mayarí", "Moa", "Rafael Freyre", "Sagua de Tánamo", "Urbano Noris"], "Granma": ["Bartolomé Masó", "Bayamo", "Buey Arriba", "Campechuela", "Cauto Cristo", "Guisa", "Jiguaní", "Manzanillo", "Media Luna", "Niquero", "Pilón", "Río Cauto", "Yara"], "Santiago de Cuba": ["Contramaestre", "Guamá", "Julio Antonio Mella", "Palma Soriano", "San Luis", "Santiago de Cuba", "Segundo Frente", "Songo la Maya", "Tercer Frente"], "Guantánamo": ["Baracoa", "Caimanera", "El Salvador", "Guantánamo", "Imías", "Maisí", "Manuel Tames", "Niceto Pérez", "San Antonio del Sur", "Yateras"], "Municipo Especial": ["Isla de la Juventud"]}

PROGRESS_BAR_STYLE = """QProgressBar {
    border: 1px solid #76797C;
    border-radius: 5px;
    text-align: center;
	color:white;
	font: bold 8pt "Segoe UI";
	background-color: rgb(35, 35, 35);
}

QProgressBar::chunk {
    background-color: #05B8CC;
}"""