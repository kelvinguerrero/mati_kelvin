__author__ = 'kelvin Guerrero'
# coding=utf-8
import os


# Metodo encargado de cargar la base de datos con la información inicial
def populate():

    #Carga de Mestrias
    maestrias = ["MATI", "MBC", "MBIT", "MESI", "MISIS", "MISO"]

    print "carga de maestrias"
    for maestria in maestrias:
        print maestria
        obj_maestria = add_master(name=maestria)
        obj_pensum = add_pensum(name=maestria, active=True, master=obj_maestria)

#Carga de estudiantes
    print "carga de estudiantes"
    estudiantes = {
                    199024632: {"master":"MISO","name": "JAIRO", "lastname": "CASALLAS BORRAS", "email": "j.casallas10@uniandes.edu.co"},
                    199922880: {"master":"MISO","name": "MANUEL ALFREDO", "lastname": "FIGUEREDO MEDINA", "email": "ma.figueredo74@uniandes.edu.co"},
                    200012581: {"master":"MISO","name": "DIEGO ANDRES", "lastname": "GONZALEZ MORENO", "email": "da.gonzalez13@uniandes.edu.co"},
                    200022105: {"master":"MISO","name": "CHRISTIAN", "lastname": "KRAUS MUÑOZ", "email": "c.kraus@uniandes.edu.co"},
                    200110321: {"master":"MISO","name": "ANDRES AUGUSTO", "lastname": "DEL RIO HERRERA", "email": "aa.del10@uniandes.edu.co"},
                    200124062: {"master":"MISO","name": "LEON CAMILO", "lastname": "SUAREZ LOPEZ", "email": "lc.suarez11@uniandes.edu.co"},
                    200125103: {"master":"MISO","name": "WILLIAM", "lastname": "ALTUZARRA NORIEGA", "email": "an.william10@uniandes.edu.co"},
                    200220825: {"master":"MISO","name": "CARLOS ALBERTO", "lastname": "ENRIQUEZ ARCOS", "email": "ca.enriquez10@uniandes.edu.co"},
                    200310723: {"master":"MISO","name": "JUAN PEDRO", "lastname": "MENDOZA RAMIREZ", "email": "jp.mendoza10@uniandes.edu.co"},
                    200319205: {"master":"MISO","name": "EDGAR ARTURO", "lastname": "COBOS GUEVARA", "email": "ea.cobos10@uniandes.edu.co"},
                    200327268: {"master":"MISO","name": "GERMAN ANDRES", "lastname": "MEZA GALLARDO", "email": "gmeza@uniandes.edu.co"},
                    200330301: {"master":"MISO","name": "ALVARO HERNANDO DEL NIÑO JESUS", "lastname": "LOPEZ MOGOLLON", "email": "ah.lopez10@uniandes.edu.co"},
                    200410809: {"master":"MISO","name": "JOHANA MARCELA", "lastname": "GUTIERREZ DIAZ", "email": "jm.gutierrez11@uniandes.edu.co"},
                    200413432: {"master":"MATI","name": "OSCAR MAURICIO", "lastname": "VILLATE VARELA", "email": "o-villat@uniandes.edu.co"},
                    200418549: {"master":"MATI","name": "VLADIMIR", "lastname": "GUZMAN PAEZ", "email": "v.guzman10@uniandes.edu.co"},
                    200418566: {"master":"MATI","name": "JOHN MARLON", "lastname": "ESPITIA MALAGON", "email": "jm.espitia10@uniandes.edu.co"},
                    200421617: {"master":"MATI","name": "JUAN CAMILO", "lastname": "DE ARGAEZ YEPES", "email": "jcdeargaez@uniandes.edu.co"},
                    200439183: {"master":"MATI","name": "ALEJANDRO", "lastname": "TRONCOSO SAAVEDRA", "email": "a.troncoso10@uniandes.edu.co"},
                    200510901: {"master":"MATI","name": "DIEGO MIGUEL", "lastname": "GAMBOA SALCEDO", "email": "di-gambo@uniandes.edu.co"},
                    200510973: {"master":"MATI","name": "MONICA ALEJANDRA", "lastname": "GUZMAN ANGEL", "email": "ga.monica10@uniandes.edu.co"},
                    200513702: {"master":"MATI","name": "JORGE FABIAN", "lastname": "VELANDIA FRAIJA", "email": "jf.velandia11@uniandes.edu.co"},
                    200521479: {"master":"MATI","name": "MANUEL EDUARDO", "lastname": "VIEDA SALOMON", "email": "me.vieda372@uniandes.edu.co"},
                    200522411: {"master":"MATI","name": "JUAN SEBASTIAN", "lastname": "PULIDO MOJICA", "email": "js.pulido126@uniandes.edu.co"},
                    200611000: {"master":"MATI","name": "JUAN FELIPE", "lastname": "HERNANDEZ GONZALEZ", "email": "jf.hernandez37@uniandes.edu.co"},
                    200611595: {"master":"MATI","name": "DIANA MARCELA", "lastname": "JIMENEZ ROJAS", "email": "dm.jimenez63@uniandes.edu.co"},
                    200614286: {"master":"MATI","name": "CAMILO", "lastname": "TELLEZ SANCHEZ", "email": "c.tellez124@uniandes.edu.co"},
                    200614410: {"master":"MATI","name": "CAMILO ALEJANDRO", "lastname": "BARRETO CADENA", "email": "ca.barreto20@uniandes.edu.co"},
                    200625245: {"master":"MBIT","name": "BETSY KATINA", "lastname": "LANCHERO BARRIOS", "email": "bk.lanchero10@uniandes.edu.co"},
                    200625363: {"master":"MBIT","name": "RAUL ANDRES", "lastname": "GUANA OLARTE", "email": "r-guana@uniandes.edu.co"},
                    200711511: {"master":"MBIT","name": "SEBASTIAN RICARDO", "lastname": "ROJAS DIAZ", "email": "rd.sebastian10@uniandes.edu.co"},
                    200713056: {"master":"MBIT","name": "SANTIAGO", "lastname": "TOVAR TALERO", "email": "s.tovar41@uniandes.edu.co"},
                    200716035: {"master":"MBIT","name": "YOLIMA DEL CARMEN", "lastname": "NAVARRO RINCONES", "email": "ydc.navarro10@uniandes.edu.co"},
                    200717407: {"master":"MBIT","name": "CARLOS ANDRES", "lastname": "LOPEZ OSPINA", "email": "ca.lopez10@uniandes.edu.co"},
                    200717752: {"master":"MBIT","name": "WILSON", "lastname": "HERNANDEZ FUENTES", "email": "w.hernandez10@uniandes.edu.co"},
                    200725144: {"master":"MBIT","name": "RICHARD FELIPE", "lastname": "BOLAÑOS VICTORIA", "email": "rf.bolanos10@uniandes.edu.co"},
                    200810450: {"master":"MBIT","name": "HELLEN JOAN", "lastname": "ACOSTA PINTO", "email": "hj.acosta10@uniandes.edu.co"},
                    200813697: {"master":"MBIT","name": "JULIAN", "lastname": "VIVEROS VILLAMIL", "email": "j.viveros72@uniandes.edu.co"},
                    200817124: {"master":"MBIT","name": "MAURICIO ANDRES", "lastname": "GIRALDO MURILLO", "email": "gm.mauricio10@uniandes.edu.co"},
                    200817981: {"master":"MBIT","name": "RONALD ARBEY", "lastname": "PLAZAS RUIZ", "email": "ra.plazas42@uniandes.edu.co"},
                    200818257: {"master":"MBIT","name": "JOSE DANIEL", "lastname": "GARCIA LOPEZ", "email": "jd.garcia248@uniandes.edu.co"},
                    200822925: {"master":"MBIT","name": "MICHEL ABRAHAM", "lastname": "KUPERMAN GUERRA", "email": "ma.kuperman576@uniandes.edu.co"},
                    200823240: {"master":"MBIT","name": "ANGELICA", "lastname": "HERNANDEZ PUENTES", "email": "a.hernandez101@uniandes.edu.co"},
                    200824698: {"master":"MBIT","name": "OSCAR DAVID", "lastname": "OSORIO VARGAS", "email": "od.osorio10@uniandes.edu.co"},
                    200910400: {"master":"MBIT","name": "JOHAR IGNACIO", "lastname": "MANTILLA BAUTISTA", "email": "ji.mantilla28@uniandes.edu.co"},
                    200911387: {"master":"MBIT","name": "LINA GISETH", "lastname": "CASAS SALAS", "email": "lg.casas766@uniandes.edu.co"},
                    200912940: {"master":"MBIT","name": "MAYERLI", "lastname": "ROMERO DIAZ", "email": "m.romero1573@uniandes.edu.co"},
                    200917638: {"master":"MBIT","name": "CAMILO ANDRES", "lastname": "PINEDA RODRIGUEZ", "email": "ca.pineda982@uniandes.edu.co"},
                    200917640: {"master":"MBIT","name": "CRISTIAN", "lastname": "QUINTERO OSORIO", "email": "c.quintero983@uniandes.edu.co"},
                    200917652: {"master":"MBIT","name": "FIDEL ANDRES", "lastname": "VARGAS LONDOÑO", "email": "fa.vargas36@uniandes.edu.co"},
                    200918283: {"master":"MBIT","name": "JOSE MANUEL", "lastname": "RODRIGUEZ VALBUENA", "email": "jm.rodriguez12@uniandes.edu.co"},
                    200918340: {"master":"MBIT","name": "ANDRES MAURICIO", "lastname": "RAMOS BONILLA", "email": "am.ramos260@uniandes.edu.co"},
                    200925365: {"master":"MBIT","name": "CARLOS EDUARDO", "lastname": "ROA VELASQUEZ", "email": "ce.roa400@uniandes.edu.co"},
                    200925616: {"master":"MBIT","name": "JUAN CARLOS", "lastname": "LOPERA MARQUEZ", "email": "jc.lopera141@uniandes.edu.co"},
                    201011963: {"master":"MBIT","name": "JOSE GILBERTO", "lastname": "GARCIA SALGADO", "email": "jg.garcia84@uniandes.edu.co"},
                    201018119: {"master":"MISIS","name": "HAIVER HERNANDO", "lastname": "PAEZ BORRAEZ", "email": "hh.paez95@uniandes.edu.co"},
                    201110330: {"master":"MISIS","name": "JAMIL FARIT", "lastname": "MURCIA GARZON", "email": "jf.murcia53@uniandes.edu.co"},
                    201110565: {"master":"MISIS","name": "EDWIN HUMBERTO", "lastname": "MUÑOZ RAMIREZ", "email": "eh.munoz55@uniandes.edu.co"},
                    201110587: {"master":"MISIS","name": "DIEGO MAURICIO", "lastname": "ROJAS CASTILLO", "email": "dm.rojas10@uniandes.edu.co"},
                    201110598: {"master":"MISIS","name": "JORGE LUIS", "lastname": "TOVAR LOPEZ", "email": "jl.tovar78@uniandes.edu.co"},
                    201110876: {"master":"MISIS","name": "HECTOR DANILO", "lastname": "HURTADO OLAYA", "email": "hd.hurtado68@uniandes.edu.co"},
                    201110886: {"master":"MISIS","name": "DANIEL ANDRES", "lastname": "PELAEZ LOPEZ", "email": "da.pelaez70@uniandes.edu.co"},
                    201110953: {"master":"MISIS","name": "CAMILO ANDRES", "lastname": "HERNANDEZ MARIN", "email": "ca.hernandez964@uniandes.edu.co"},
                    201110963: {"master":"MISIS","name": "VICTOR HERNAN", "lastname": "RODRIGUEZ ZAMBRANO", "email": "vh.rodriguez73@uniandes.edu.co"},
                    201117825: {"master":"MISIS","name": "MAX FRANK", "lastname": "RODRIGUEZ HUERTAS", "email": "mfrh.rodriguez10@uniandes.edu.co"},
                    201117838: {"master":"MISIS","name": "ERNESTO FABIAN", "lastname": "VARGAS MADRID", "email": "ef.vargas85@uniandes.edu.co"},
                    201122755: {"master":"MISIS","name": "YESID ALONSO", "lastname": "RAMOS MARRUGO", "email": "ya.ramos65@uniandes.edu.co"},
                    201124139: {"master":"MISIS","name": "DIEGO FERNANDO", "lastname": "RODRIGUEZ VARGAS", "email": "df.rodriguez15@uniandes.edu.co"},
                    201210022: {"master":"MISIS","name": "JUAN CAMILO", "lastname": "GUERRERO PINILLA", "email": "jc.guerrero10@uniandes.edu.co"},
                    201221355: {"master":"MISIS","name": "JEIMMY JASBLEYDI", "lastname": "PARRA PLAZAS", "email": "j.parra10@uniandes.edu.co"},
                    201221454: {"master":"MISIS","name": "DIANA MARIA", "lastname": "GOMEZ GALVIS", "email": "dm.gomez10@uniandes.edu.co"},
                    201221456: {"master":"MISIS","name": "MIGUEL ANGEL", "lastname": "LOPEZ GARAVITO", "email": "ma.lopez11@uniandes.edu.co"},
                    201221512: {"master":"MISIS","name": "DIANA CAROLINA", "lastname": "RAMIREZ GUTIERREZ", "email": "dc.ramirez10@uniandes.edu.co"},
                    201221521: {"master":"MISIS","name": "JOHNY GERMAN", "lastname": "BLANCO CALDERON", "email": "jg.blanco10@uniandes.edu.co"},
                    201221547: {"master":"MISIS","name": "MIGUEL ANGEL", "lastname": "RODRIGUEZ DUARTE", "email": "ma.rodriguez12@uniandes.edu.co"},
                    201221549: {"master":"MESI","name": "OSCAR CAMILO", "lastname": "ROZO HERNANDEZ", "email": "oc.rozo10@uniandes.edu.co"},
                    201221550: {"master":"MESI","name": "FABIO ANDRES", "lastname": "SANCHEZ BAPTISTE", "email": "fa.sanchez10@uniandes.edu.co"},
                    201221597: {"master":"MESI","name": "ANDRES FELIPE", "lastname": "RODRIGUEZ ARIAS", "email": "af.rodriguez11@uniandes.edu.co"},
                    201221610: {"master":"MESI","name": "NICOLAS", "lastname": "GARCIA QUIROZ", "email": "n.garcia10@uniandes.edu.co"},
                    201221619: {"master":"MESI","name": "OMAR DARIO", "lastname": "MENDOZA GONZALEZ", "email": "od.mendoza10@uniandes.edu.co"},
                    201221623: {"master":"MESI","name": "CARLOS ANDRES", "lastname": "NIÑO ALARCON", "email": "na.carlos10@uniandes.edu.co"},
                    201221624: {"master":"MESI","name": "SERGIO ALBERTO", "lastname": "NUÑEZ ALVIRA", "email": "snunez@uniandes.edu.co"},
                    201221640: {"master":"MESI","name": "CARLOS", "lastname": "SANABRIA BUITRAGO", "email": "c.sanabria10@uniandes.edu.co"},
                    201221670: {"master":"MESI","name": "HUGO ALBERTO", "lastname": "AMAYA ACERO", "email": "ha.amaya10@uniandes.edu.co"},
                    201221682: {"master":"MESI","name": "BAYRON EDUARDO", "lastname": "YELA MARTINEZ", "email": "be.yela10@uniandes.edu.co"},
                    201221721: {"master":"MESI","name": "DANIEL", "lastname": "BARRERA BUSTOS", "email": "d.barrera11@uniandes.edu.co"},
                    201221733: {"master":"MESI","name": "JULIAN FELIPE", "lastname": "BUENO IZQUIERDO", "email": "jf.bueno10@uniandes.edu.co"},
                    201221771: {"master":"MESI","name": "SERGIO ESTEFANO", "lastname": "LINARES GUERRERO", "email": "se.linares10@uniandes.edu.co"},
                    201221782: {"master":"MESI","name": "JUAN SEBASTIAN", "lastname": "MARULANDA MEZA", "email": "js.marulanda10@uniandes.edu.co"},
                    201221785: {"master":"MESI","name": "MIGUEL ENRIQUE", "lastname": "MENDOZA GONZALEZ", "email": "me.mendoza10@uniandes.edu.co"},
                    201221786: {"master":"MESI","name": "JULIAN HERNAN", "lastname": "MICOLTA HURTADO", "email": "jh.micolta10@uniandes.edu.co"},
                    201221794: {"master":"MESI","name": "ADRIANA", "lastname": "NOGUERA ROJAS", "email": "a.noguera10@uniandes.edu.co"},
                    201221821: {"master":"MESI","name": "GIOVANNY RICARDO", "lastname": "RODRIGUEZ CHITIVA", "email": "gr.rodriguez10@uniandes.edu.co"},
                    201221826: {"master":"MESI","name": "WILMER MOISES", "lastname": "ROMERO PRIETO", "email": "wm.romero10@uniandes.edu.co"},
                    201221834: {"master":"MESI","name": "CARLOS FEDERICO", "lastname": "SUAREZ URIBE", "email": "cf.suarez10@uniandes.edu.co"},
                    201310189: {"master":"MESI","name": "CAMILO ANDRES", "lastname": "ALMANZA BERNAL", "email": "ca.almanza10@uniandes.edu.co"},
                    201310193: {"master":"MESI","name": "MAURICIO", "lastname": "AMAYA RIOS", "email": "m.amaya11@uniandes.edu.co"},
                    201310198: {"master":"MATI","name": "FELIX ALBERTO", "lastname": "ARIZA NIÑO", "email": "fa.ariza10@uniandes.edu.co"},
                    201310231: {"master":"MISO","name": "JUAN JOSE", "lastname": "BUZON SILVERA", "email": "bs.juan10@uniandes.edu.co"},
                    201310243: {"master":"MISO","name": "STEVE XAVIER", "lastname": "CARDENAS OSPINA", "email": "sx.cardenas10@uniandes.edu.co"},
                    201310263: {"master":"MISO","name": "RAFAEL ANDRES", "lastname": "CHAPARRO PARDO", "email": "cp.rafael10@uniandes.edu.co"},
                    201310274: {"master":"MISO","name": "RAUL ALEXANDER", "lastname": "CRUZ VALLEJO", "email": "ra.cruz11@uniandes.edu.co"},
                    201310289: {"master":"MISO","name": "OSCAR IVAN", "lastname": "ESTRADA GONZALEZ", "email": "oi.estrada@uniandes.edu.co"},
                    201310290: {"master":"MISO","name": "JUAN PABLO", "lastname": "ESTUPIÑAN SUAREZ", "email": "jp.estupinan10@uniandes.edu.co"},
                    201310296: {"master":"MISO","name": "IVAN FELIPE", "lastname": "FLOREZ BECERRA", "email": "if.florez10@uniandes.edu.co"},
                    201310300: {"master":"MISO","name": "CRISTIAN DAVID", "lastname": "FORESTIERI ROJAS", "email": "cd.forestieri10@uniandes.edu.co"},
                    201310302: {"master":"MISO","name": "LADY PAOLA", "lastname": "FUERTES CEBALLOS", "email": "lp.fuertes10@uniandes.edu.co"},
                    201310306: {"master":"MISO","name": "OSCAR JAVIER", "lastname": "GARZON MACIAS", "email": "oj.garzon10@uniandes.edu.co"},
                    201310309: {"master":"MISO","name": "BRIGITTE MARCELA", "lastname": "GOMEZ MORA", "email": "bm.gomez10@uniandes.edu.co"},
                    201310312: {"master":"MISO","name": "DIEGO ANDRES", "lastname": "GOMEZ SUAREZ", "email": "da.gomez17@uniandes.edu.co"},
                    201310348: {"master":"MISO","name": "CAMILO ANDRES", "lastname": "LEMUS BERNAL", "email": "ca.lemus10@uniandes.edu.co"},
                    201310355: {"master":"MISO","name": "NICOLAS ANDRES", "lastname": "LORENZO ROZO", "email": "na.lorenzo10@uniandes.edu.co"},
                    201310361: {"master":"MISO","name": "EDGAR ANDRES", "lastname": "MARIN VEGA", "email": "ea.marin10@uniandes.edu.co"},
                    201310362: {"master":"MISO","name": "CLEWIN DAVID", "lastname": "MARQUEZ CANTILLO", "email": "cd.marquez10@uniandes.edu.co"},
                    201310366: {"master":"MISO","name": "MAGDIEL WILDER", "lastname": "MARTINEZ ANGULO", "email": "mw.martinez10@uniandes.edu.co"},
                    201310369: {"master":"MISO","name": "MARIA LUCIA", "lastname": "MARTINEZ IDARRAGA", "email": "ml.martinez10@uniandes.edu.co"},
                    201310374: {"master":"MISO","name": "FELIX", "lastname": "MEDINA BATANERO", "email": "f.medina10@uniandes.edu.co"},
                    201310382: {"master":"MISO","name": "CAMILO ANDRES", "lastname": "MILLAN MORENO", "email": "ca.millan10@uniandes.edu.co"},
                    201310390: {"master":"MISO","name": "FREDDY ALBERTO", "lastname": "MORENO LOPEZ", "email": "fa.moreno10@uniandes.edu.co"},
                    201310404: {"master":"MISO","name": "GEIDER HERNAN", "lastname": "NIVIA MUÑOZ", "email": "gh.nivia10@uniandes.edu.co"},
                    201310405: {"master":"MISO","name": "JAVIER JOSE", "lastname": "NOREÑA MOLINA", "email": "jj.norena10@uniandes.edu.co"},
                    201310410: {"master":"MISO","name": "DIEGO IVAN", "lastname": "OLIVEROS ACOSTA", "email": "di.oliveros10@uniandes.edu.co"},
                    201310411: {"master":"MISO","name": "GINA ALEJANDRA", "lastname": "ORDOÑEZ PIÑEROS", "email": "op.gina10@uniandes.edu.co"},
                    201310422: {"master":"MISO","name": "FREDDY ARLEY", "lastname": "PARRA BONILLA", "email": "fa.parra10@uniandes.edu.co"},
                    201310428: {"master":"MISO","name": "YESID FERNANDO", "lastname": "PEREZ BARRIOS", "email": "yf.perez10@uniandes.edu.co"},
                    201310487: {"master":"MISO","name": "DANIEL JOSE", "lastname": "ROMERO MARTINEZ", "email": "dj.romero10@uniandes.edu.co"},
                    201310490: {"master":"MISO","name": "MONICA JAZMIN", "lastname": "RUGE GIL", "email": "mj.ruge10@uniandes.edu.co"},
                    201310505: {"master":"MISO","name": "FREDY ORLANDO", "lastname": "SANDOVAL LAGOS", "email": "fo.sandoval10@uniandes.edu.co"},
                    201310510: {"master":"MATI","name": "NATHALY", "lastname": "SEGURA SANCHEZ", "email": "n.segura10@uniandes.edu.co"},
                    201310513: {"master":"MATI","name": "GAMALIEL ANDRES", "lastname": "SILVA ORTIZ", "email": "ga.silva11@uniandes.edu.co"},
                    201310514: {"master":"MATI","name": "JULIANA", "lastname": "SOLANILLA OSSA", "email": "j.solanilla10@uniandes.edu.co"},
                    201310543: {"master":"MATI","name": "ANGEE JULIETH", "lastname": "ZAMBRANO GOMEZ", "email": "aj.zambrano10@uniandes.edu.co"},
                    201310548: {"master":"MATI","name": "LUIS EDUARDO", "lastname": "TORRES BELTRAN", "email": "le.torres10@uniandes.edu.co"},
                    201310676: {"master":"MATI","name": "FEDERICO", "lastname": "BONILLA GOMEZ", "email": "bg.federico10@uniandes.edu.co"},
                    201319384: {"master":"MATI","name": "JULIAN EDUARDO", "lastname": "QUINTERO", "email": "q.julian10@uniandes.edu.co"},
                    201321404: {"master":"MATI","name": "LUIS FERNANDO", "lastname": "BRACHO HOYOS", "email": "bh.luis10@uniandes.edu.co"},
                    201321436: {"master":"MATI","name": "HERNAN DARIO", "lastname": "TENJO MATEUS", "email": "tm.hernan10@uniandes.edu.co"},
                    201321710: {"master":"MATI","name": "YURLY MAYERLI", "lastname": "SOSA CARVAJAL", "email": "sc.yurly10@uniandes.edu.co"},
                    201323770: {"master":"MATI","name": "MARY FRANCES", "lastname": "ZUCCHET CALDERON", "email": "zc.mary10@uniandes.edu.co"},
                    201323971: {"master":"MATI","name": "WILMAR ALBERTO", "lastname": "FUQUEN", "email": "f.wilmar10@uniandes.edu.co"},
                    201323999: {"master":"MATI","name": "MAURICIO", "lastname": "ACOSTA ARISTIZABAL", "email": "aa.mauricio10@uniandes.edu.co"},
                    201324087: {"master":"MATI","name": "HERNAN GEOVANNI", "lastname": "TAIMAL NARVAEZ", "email": "tn.hernan10@uniandes.edu.co"},
                    201324182: {"master":"MATI","name": "RICARDO", "lastname": "NOREÑA JIMENEZ", "email": "nj.ricardo10@uniandes.edu.co"},
                    201324537: {"master":"MATI","name": "LEYDI VIVIANA", "lastname": "CRISTANCHO", "email": "c.leydi10@uniandes.edu.co"},
                    201324547: {"master":"MISIS","name": "ARLEY JULIAN", "lastname": "GUTIERREZ BARRERA", "email": "gb.arley10@uniandes.edu.co"},
                    201324560: {"master":"MISIS","name": "FRANCISCO LUIS", "lastname": "RODRIGUEZ VILLABONA", "email": "rv.francisco10@uniandes.edu.co"},
                    201324619: {"master":"MISIS","name": "MIGUEL ANGEL", "lastname": "GARZON TRIANA", "email": "gt.miguel10@uniandes.edu.co"},
                    201324623: {"master":"MISIS","name": "ANDRES", "lastname": "ARCINIEGAS MEDINA", "email": "am.andres11@uniandes.edu.co"},
                    201324624: {"master":"MISIS","name": "CESAR UBALDO", "lastname": "BAEZ BAEZ", "email": "bb.cesar10@uniandes.edu.co"},
                    201324644: {"master":"MISIS","name": "JAIME GIOVANNY", "lastname": "GARZON GOMEZ", "email": "gg.jaime10@uniandes.edu.co"},
                    201324657: {"master":"MISIS","name": "CARLOS EDUARDO", "lastname": "MARTINEZ CAMELO", "email": "mc.carlos10@uniandes.edu.co"},
                    201324660: {"master":"MISIS","name": "JENNYFER ANDREA", "lastname": "MOGOLLON MANTILLA", "email": "mm.jennyfer10@uniandes.edu.co"},
                    201324674: {"master":"MISIS","name": "IVAN DAVID", "lastname": "RINCON VIVAS", "email": "rv.ivan10@uniandes.edu.co"},
                    201324681: {"master":"MISIS","name": "DIEGO EDUARDO", "lastname": "ROZO CASTAÑEDA", "email": "rc.diego10@uniandes.edu.co"},
                    201324692: {"master":"MISIS","name": "JAVIER FERNANDO", "lastname": "VERA TORRES", "email": "vt.javier10@uniandes.edu.co"},
                    201324693: {"master":"MISIS","name": "OSCAR ALEJANDRO", "lastname": "VILLAMIL RUIZ", "email": "vr.oscar10@uniandes.edu.co"},
                    201324695: {"master":"MISIS","name": "ANGELA MARIA", "lastname": "VIVEROS EGAS", "email": "ve.angela10@uniandes.edu.co"},
                    201324711: {"master":"MISIS","name": "JHON FREDY", "lastname": "GUTIERREZ QUICENO", "email": "jf.gutierrez20@uniandes.edu.co"},
                    201410135: {"master":"MISIS","name": "DIEGO ARMANDO", "lastname": "CABALLERO ANDRADE", "email": "da.caballero11@uniandes.edu.co"},
                    201410156: {"master":"MISIS","name": "MANUEL ARMANDO", "lastname": "DE LA TORRE PRADA", "email": "ma.de11@uniandes.edu.co"},
                    201410230: {"master":"MISIS","name": "JOHANNA", "lastname": "REYES ROJAS", "email": "j.reyes12@uniandes.edu.co"},
                    201410474: {"master":"MISIS","name": "PAULO ANDRES", "lastname": "GIL RAMIREZ", "email": "pa.gil10@uniandes.edu.co"},
                    201410480: {"master":"MISIS","name": "GERMAN", "lastname": "GONZALEZ MONTERO", "email": "g.gonzalez10@uniandes.edu.co"},
                    201410490: {"master":"MISIS","name": "JUAN DAVID", "lastname": "LEON CASTILLO", "email": "jd.leon10@uniandes.edu.co"},
                    201410525: {"master":"MISIS","name": "JUAN CARLOS", "lastname": "RUBIANO PANADERO", "email": "jc.rubiano11@uniandes.edu.co"},
                    201410756: {"master":"MISIS","name": "JAIMIR ALEXIS", "lastname": "GUERRERO", "email": "ja.guerrero11@uniandes.edu.co"},
                    201410760: {"master":"MISIS","name": "OSBERT ANTONIO", "lastname": "LINERO CUETO", "email": "oa.linero10@uniandes.edu.co"},
                    201410769: {"master":"MBC","name": "OSCAR ARMANDO", "lastname": "ORTIZ SOTO", "email": "oa.ortiz10@uniandes.edu.co"},
                    201410770: {"master":"MBC","name": "DIEGO CAMILO", "lastname": "PALACIOS FLECHAS", "email": "dc.palacios11@uniandes.edu.co"},
                    201411123: {"master":"MBC","name": "FERNANDO", "lastname": "GUTIERREZ BAUTISTA", "email": "f.gutierrez11@uniandes.edu.co"},
                    201411125: {"master":"MBC","name": "VANESA LUCIA", "lastname": "HERNANDEZ RODRIGUEZ", "email": "vl.hernandez10@uniandes.edu.co"},
                    201411137: {"master":"MBC","name": "ANDERSON AUGUSTO", "lastname": "MIRANDA LUNA", "email": "aa.miranda10@uniandes.edu.co"},
                    201411149: {"master":"MBC","name": "WALTER ENRIQUE", "lastname": "RODRIGUEZ RODRIGUEZ", "email": "we.rodriguez10@uniandes.edu.co"},
                    201411150: {"master":"MBC","name": "JOHN JAIRO", "lastname": "ROJAS SABOGAL", "email": "jj.rojas11@uniandes.edu.co"},
                    201411439: {"master":"MBC","name": "JUAN PABLO", "lastname": "BONILLA MONTERO", "email": "jp.bonilla10@uniandes.edu.co"},
                    201411451: {"master":"MBC","name": "LAURA CONSUELO", "lastname": "DOMINGUEZ CHITIVA", "email": "lc.dominguez10@uniandes.edu.co"},
                    201411453: {"master":"MBC","name": "OMAR GUILLERMO", "lastname": "ERAZO CRUZ", "email": "og.erazo10@uniandes.edu.co"},
                    201411458: {"master":"MBC","name": "OSCAR RAUL", "lastname": "GARAVITO ROJAS", "email": "or.garavito10@uniandes.edu.co"},
                    201411464: {"master":"MBC","name": "MILTON ALEXIS", "lastname": "JIMENEZ ACERO", "email": "ma.jimenez12@uniandes.edu.co"},
                    201411469: {"master":"MBC","name": "FABIAN MAURICIO", "lastname": "MELO GARZON", "email": "fm.melo10@uniandes.edu.co"},
                    201411472: {"master":"MBC","name": "PEDRO ALEXANDER", "lastname": "MORENO CORREA", "email": "pa.moreno13@uniandes.edu.co"},
                    201411486: {"master":"MBC","name": "RODRIGO RAFAEL", "lastname": "RODRIGUEZ CORTEZ", "email": "rr.rodriguez10@uniandes.edu.co"},
                    201411519: {"master":"MBC","name": "STEVEN", "lastname": "JAIMES PICO", "email": "s.jaimes10@uniandes.edu.co"},
                    201411522: {"master":"MBC","name": "RICARDO JOSE", "lastname": "SILVA GOMEZ", "email": "rj.silva10@uniandes.edu.co"},
                    200315085: {"master":"MBC","name": "DIEGO ARMANDO", "lastname": "BAUTISTA LAGOS", "email": "da.bautista30@uniandes.edu.co"},
                    200813688: {"master":"MBC","name": "SANTIAGO", "lastname": "VILLAVECES PARDO", "email": "s.villaveces62@uniandes.edu.co"},
                    200820761: {"master":"MBC","name": "JOSE ALEJANDRO", "lastname": "NIÑO MORA", "email": "ja.nino905@uniandes.edu.co"},
                    201110544: {"master":"MBC","name": "WILLIAN ALEJANDRO", "lastname": "IDROBO LUNA", "email": "wa.idrobo223@uniandes.edu.co"},
                    201221724: {"master":"MBC","name": "VIVIANA ANGELY", "lastname": "BASTIDAS MELO", "email": "va.bastidas10@uniandes.edu.co"},
                    201321401: {"master":"MBC","name": "PABLO ANDRES", "lastname": "BARON RUEDA", "email": "br.pablo10@uniandes.edu.co"},
                    201321402: {"master":"MBC","name": "ANDRES FABIAN", "lastname": "BARRERA SALINAS", "email": "bs.andres10@uniandes.edu.co"},
                    199827642: {"master":"MBC","name": "ALVARO", "lastname": "ECHEVERRY SALCEDO", "email": "a.echeverry10@uniandes.edu.co"},
                    200611055: {"master":"MBC","name": "CRISTIAN YESID", "lastname": "ALFONSO SILVA", "email": "cy.alfonso10@uniandes.edu.co"},
                    201310277: {"master":"MBC","name": "YANERYS IRINA", "lastname": "DE LA HOZ MAESTRE", "email": "yi.de10@uniandes.edu.co"},
                    201310424: {"master":"MBC","name": "RHONY FRANCISCO", "lastname": "PEDRAZA BUSTAMANTE", "email": "rf.pedraza10@uniandes.edu.co"},
                    201310486: {"master":"MBC","name": "EDWIN ARTURO", "lastname": "ROMERO GONZALEZ", "email": "ea.romero11@uniandes.edu.co"},
                    200210734: {"master":"MBC","name": "JULIO CESAR", "lastname": "RODRIGUEZ MARIN", "email": "julioc-r@uniandes.edu.co"}
                    }

    for estudiante in estudiantes:
        obj_student = add_student(code=estudiante,
                                   email=estudiantes[estudiante]["email"],
                                   lastname=estudiantes[estudiante]["lastname"],
                                   name=estudiantes[estudiante]["name"],
                                   master=Master.objects.get(name=estudiantes[estudiante]["master"]))

    #Carga de profesores
    print "carga de profesores"
    profesores = {
                    200017271: {"name": "JORGE HUMBERTO", "lastname": "ARIAS BEDOYA", "email": "jor-aria@uniandes.edu.co"},
                    198714604: {"name": "GREGORIO IVAN ERNESTO", "lastname": "BECERRA RODRIGUEZ", "email": "gie.becerra10@uniandes.edu.co"},
                    79505041: {"name": "DARIO ERNESTO", "lastname": "CORREAL", "email": "dcorreal@uniandes.edu.co"},
                    199617196: {"name": "MARIA DEL PILAR", "lastname": "VILLAMIL GIRALDO", "email": "mavillam@uniandes.edu.co"},
                    79419382: {"name": "HAROLD ENRIQUE", "lastname": "CASTRO BARRERA", "email": "hcastro@uniandes.edu.co"},
                    85462189: {"name": "YESID", "lastname": "DONOSO", "email": "ydonoso@uniandes.edu.co"},
                    79232014: {"name": "JORGE ALBERTO", "lastname": "VILLALOBOS SALCEDO", "email": "jvillalo@uniandes.edu.co"},
                    198016691: {"name": "EDUARDO", "lastname": "GONGORA MORENO", "email": "egongora@uniandes.edu.co"},
                    197810037: {"name": "RAFAEL ENRIQUE", "lastname": "GOMEZ DIAZ", "email": "ragomez@uniandes.edu.co"},
                    194814117: {"name": "FRANCISCO", "lastname": "RUEDA FAJARDO", "email": "frueda@uniandes.edu.co"},
                    199427762: {"name": "SANDRA JULIETA", "lastname": "RUEDA RODRIGUEZ", "email": "sarueda@uniandes.edu.co"},
                    000000001: {"name": "Kelly", "lastname": "Garcés Pernett", "email": "kj.garces971@uniandes.edu.co"},
                    000000002: {"name": "MIGUEL", "lastname": "NAVARRO SANINT", "email": "mi-navar@uniandes.edu.co"},
                    000000003: {"name": "Rubby", "lastname": "Casallas Gutierrez", "email": "rcasalla@uniandes.edu.co"},
                    000000004: {"name": "Juan Pablo", "lastname": "Fernandez Ramirez", "email": "jp.fernandez29@uniandes.edu.co"},
                    000000005: {"name": "Milton", "lastname": "Quiroga Becerra", "email": "mquiroga@uniandes.edu.co"},
                    000000006: {"name": "Juan Diego", "lastname": "Jiménez", "email": "jujimene@uniandes.edu.co"},
                    000000007: {"name": "RICARDO", "lastname": "GOMEZ DIAZ", "email": "ricgomez@uniandes.edu.co"},
                    800000000: {"name": "Victor", "lastname": "Toro Córdoba", "email": "vm.toro815@uniandes.edu.co"},
                    900000000: {"name": "Oscar", "lastname": "González Rojas", "email": "o-gonza1@uniandes.edu.co"},
                    110000000: {"name": "Oscar", "lastname": "Ávila Cifuentes", "email": "oj.avila@uniandes.edu.co"},
                    120000000: {"name": "Ana Lucia", "lastname": "Duque Salazar", "email": "al.duque58@uniandes.edu.co"},
                    130000000: {"name": "Jorge Arias", "lastname": "Bedoya", "email": "bedoya@uniandes.edu.co"},
                    140000000: {"name": "María Esther", "lastname": "Ordóñez", "email": "mordonez2013@uniandes.edu.co"},
                    0: {"name": "Sin asignar", "lastname": "ninguno", "email": "no-reply@uniandes.edu.co"},
                    200021872: {"name": "MARIO EDUARDO", "lastname": "SANCHEZ PUCCINI", "email": "mar-san1@uniandes.edu.co"}}

    for profesor in profesores:
        obj_profesor = add_teacher(profesor, profesores[profesor]["email"],
                                   profesores[profesor]["lastname"],
                                   profesores[profesor]["name"])


#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MATI
    print "carga de cursos de MATI"

    cursosMati = {
        "ARTI4101": {"name": "Gerencia de Proyectos para Arquitectos", "credits": 4, "summer": False},
        "ARTI4102": {"name": "Comunicación Efectiva para Arquitectos", "credits": 4, "summer": False},
        "ARTI4103": {"name": "Arquitectura de Negocios y Estrategia de TI", "credits": 4, "summer": False},
        "ARTI4104": {"name": "Fundamentos para Arquitectos", "credits": 4, "summer": False},
        "ARTI4201": {"name": "Arquitectura de Solución", "credits": 4, "summer": False},
        "ARTI4202": {"name": "Arquitectura de Información", "credits": 4, "summer": False},
        "ARTI4203": {"name": "Arquitectura de Infraestructura de TI", "credits": 4, "summer": False},
        "ARTI4204": {"name": "Arquitectura de Seguridad", "credits": 4, "summer": False},
        "ARTI4205": {"name": "Arquitectura de Procesos de Negocio", "credits": 4, "summer": False},
        "ARTI4301": {"name": "Proyecto final", "credits": 4, "summer": False},
        "ARTI4106": {"name": "Arquitectura Empresarial", "credits": 4, "summer": False}}

    for codigo in cursosMati:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MATI"),
            code=codigo,
            credits=cursosMati[codigo]["credits"],
            name=cursosMati[codigo]["name"],
            summer=cursosMati[codigo]["summer"])

    print "carga de secciones de MATI"
    seccionesMati = {
        13183: {"course": "ARTI4101", "capacity": {"MATI": 34, "pregrado": 3, "otros": 3}, "name": "1", "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        13579: {"course": "ARTI4102", "capacity": {"MATI": 32, "pregrado": 2, "otros": 6}, "name": "2", "semester": 1, "year": 2015, "teacher": 120000000, "status": 0},
        12663: {"course": "ARTI4103", "capacity": {"MATI": 40, "MBIT": 40, "MESI": 10}, "name": "1", "semester": 1, "year": 2015, "teacher": 79232014, "status": 0},
        13981: {"course": "ARTI4104", "capacity": {"MATI": 34, "pregrado": 2, "otros": 4}, "name": "2", "semester": 1, "year": 2015, "teacher": 198714604, "status": 0},
        13982: {"course": "ARTI4106", "capacity": {"MATI": 60, "MBIT": 40}, "name": "1", "semester": 1, "year": 2015, "teacher": 130000000, "status": 0},
        12664: {"course": "ARTI4201", "capacity": {"MATI": 35, "otros": 5}, "name": "1", "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        12667: {"course": "ARTI4202", "capacity": {"MATI": 34, "pregrado": 2, "otros": 4}, "name": "1", "semester": 1, "year": 2015, "teacher": 140000000, "status": 0},
        12665: {"course": "ARTI4203", "capacity": {"MATI": 20, "MESI": 20}, "name": "1", "semester": 1, "year": 2015, "teacher": 79419382, "status": 0},
        13185: {"course": "ARTI4204", "capacity": {"MATI": 32, "pregrado": 4, "otros": 4}, "name": "1", "semester": 1, "year": 2015, "teacher": 85462189, "status": 0},
        13285: {"course": "ARTI4205", "capacity": {"MATI": 34, "pregrado": 2, "otros": 4}, "name": "1", "semester": 1, "year": 2015, "teacher": 200021872, "status": 0},
        13582: {"course": "ARTI4301", "capacity": {"MATI": 99}, "name": "1", "semester": 1, "year": 2015, "teacher": 79505041, "status": 0}}

    for seccion in seccionesMati:
        add_section(
            crn=seccion,
            name=seccionesMati[seccion]["name"],
            semester=seccionesMati[seccion]["semester"],
            year=seccionesMati[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMati[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMati[seccion]["course"]),
            capacity=seccionesMati[seccion]["capacity"],
            status=seccionesMati[seccion]["status"]
        )
#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MBC
    print "carga de cursos de MBC"
    cursosMbc = {
        "1": {"name": "Bioinformática", "credits": 4, "summer": False},
        "2": {"name": "Algoritmos en Biología Computacional", "credits": 4, "summer": False},
        "3": {"name": "Fundamentos en programación para ciencias biológicas", "credits": 4, "summer": False},
        "4": {"name": "Biología Molecular Avanzada", "credits": 4, "summer": False},
        "5": {"name": "Biología Cuantitativa", "credits": 4, "summer": False},
        "6": {"name": "Procesamiento de datos biológicos", "credits": 4, "summer": False},
        "7": {"name": "Computación de alto desempeño para ciencias biológicas", "credits": 4, "summer": False},
        "8": {"name": "Computación visual para ciencias biológicas", "credits": 4, "summer": False},
        "9": {"name": "Modelamiento de redes", "credits": 4, "summer": False},
        "0": {"name": "Analisis de secuencias", "credits": 4, "summer": False},
        "10": {"name": "Biología de sistemas", "credits": 4, "summer": False},
        "11": {"name": "Biología sintética", "credits": 4, "summer": False},
        "12": {"name": "Introducción a la ingeniería de proteinas", "credits": 4, "summer": False},
        "13": {"name": "Modelamientos matemáticos en biología", "credits": 4, "summer": False}}

    for codigo in cursosMbc:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBC"),
            code=codigo,
            credits=cursosMbc[codigo]["credits"],
            name=cursosMbc[codigo]["name"],
            summer=cursosMbc[codigo]["summer"])

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MBIT
    print "carga de cursos de MBIT"
    cursosMbit = {
        "MBIT4101": {"name": "Habilidades Gerenciales en TI", "credits": 4, "summer": False},
        "MBIT4201": {"name": "Emprendimiento y Negocios Electrónicos", "credits": 4, "summer": False},
        "MBIT4202": {"name": "Gobierno de TI", "credits": 4, "summer": False},
        "MBIT4203": {"name": "Business Analytics", "credits": 4, "summer": False},
        "MBIT4204": {"name": "Gestión de Servicios de TI", "credits": 4, "summer": False},
        "MBIT4301": {"name": "PROYECTO FINAL", "credits": 4, "summer": False},
        "MBIT4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MBIT4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MBIT4205": {"name": "Fundamentos de Gerencia de TI", "credits": 4, "summer": False}}

    for codigo in cursosMbit:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBIT"),
            code=codigo,
            credits=cursosMbit[codigo]["credits"],
            name=cursosMbit[codigo]["name"],
            summer=cursosMbit[codigo]["summer"])


    #Secciones de MBIT
    print "carga de secciones de MBIT"
    seccionesMesi = {
        16852: {"course": "MBIT4101", "name": "1", "capacity": {"MBIT": 40, "MESI": 10, "otros": 10}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        15804: {"course": "MBIT4101", "name": "2", "capacity": {"MBIT": 40, "MESI": 10, "otros": 10}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        13984: {"course": "MBIT4201", "name": "1", "capacity": {"MBIT": 40, "MISO": 26, "pregrado": 8, "otros": 6}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        16853: {"course": "MBIT4201", "name": "2", "capacity": {"MBIT": 40, "MISO": 26, "pregrado": 8, "otros": 6}, "semester": 1, "year": 2015, "teacher": 194814117, "status": 0},
        13985: {"course": "MBIT4202", "name": "1", "capacity": {"MBIT": 30, "MESI": 10, "otros": 5}, "semester": 1, "year": 2015, "teacher": 900000000, "status": 0},
        14598: {"course": "MBIT4203", "name": "1", "capacity": {"MBIT": 35, "otros": 5}, "semester": 1, "year": 2015, "teacher": 199617196, "status": 0},
        14599: {"course": "MBIT4204", "name": "1", "capacity": {"MBIT": 35, "otros": 5}, "semester": 1, "year": 2015, "teacher": 110000000, "status": 0},
        14600: {"course": "MBIT4205", "name": "1", "capacity": {"MBIT": 30, "MESI": 5, "otros": 5}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        17118: {"course": "MBIT4301", "name": "1", "capacity": {"MBIT": 99}, "semester": 1, "year": 2015, "teacher": 0, "status": 0},
        17119: {"course": "MBIT4302", "name": "1", "capacity": {"MBIT": 99}, "semester": 1, "year": 2015, "teacher": 0, "status": 0},
        17120: {"course": "MBIT4303", "name": "1", "capacity": {"MBIT": 99}, "semester": 1, "year": 2015, "teacher": 0, "status": 0}}

    for seccion in seccionesMesi:
        add_section(
            crn=seccion,
            name=seccionesMesi[seccion]["name"],
            semester=seccionesMesi[seccion]["semester"],
            year=seccionesMesi[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMesi[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMesi[seccion]["course"]),
            capacity=seccionesMesi[seccion]["capacity"],
            status=seccionesMesi[seccion]["status"]
        )

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MESI
    print "carga de cursos de MESI"
    cursosMbit = {
        "MSIN4201": {"name": "Modelos de Seguridad – Aplicaciones y Análisis de Estándares", "credits": 4,"summer": False},
        "MSIN4203": {"name": "Gerencia de CSIRTs y Manejo de Incidentes", "credits": 4, "summer": False},
        "MSIN4301": {"name": "PROYECTO FINAL", "credits": 4, "summer": False},
        "MSIN4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MSIN4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MSIN4101": {"name": "Ingeniería Criptográfica y su Aplicación en TI", "credits": 4, "summer": False}}

    for codigo in cursosMbit:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBIT"),
            code=codigo,
            credits=cursosMbit[codigo]["credits"],
            name=cursosMbit[codigo]["name"],
            summer=cursosMbit[codigo]["summer"])

    #Secciones de MESI
    print "carga de secciones de MESI"
    seccionesMesi = {
        15850: {"course": "MSIN4101", "name": "1", "capacity": {"MESI": 33, "pregrado": 4, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000005, "status": 0},
        14607: {"course": "MSIN4201", "name": "1", "capacity": {"MESI": 33, "pregrado": 4, "otros": 3}, "semester": 1, "year": 2015, "teacher": 199427762, "status": 0},
        15851: {"course": "MSIN4203", "name": "1", "capacity": {"MESI": 33, "pregrado": 4, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000006, "status": 0},
        14609: {"course": "MSIN4302", "name": "1", "capacity": {"MESI": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0},
        14608: {"course": "MSIN4301", "name": "1", "capacity": {"MESI": 99}, "semester": 1, "year": 2015, "teacher": 000000007, "status": 0},
        16217: {"course": "MSIN4303", "name": "1", "capacity": {"MESI": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0}}

    for seccion in seccionesMesi:
        add_section(
            crn=seccion,
            name=seccionesMesi[seccion]["name"],
            semester=seccionesMesi[seccion]["semester"],
            year=seccionesMesi[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMesi[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMesi[seccion]["course"]),
            capacity=seccionesMesi[seccion]["capacity"],
            status=seccionesMesi[seccion]["status"]
        )

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MISIS
    print "carga de cursos de MISIS"
    cursosIsis = {
        "ISIS-4422": {"name": "Servicios móviles y redes de próxima generación", "credits": 4, "summer": False},
        "ISIS-4518": {"name": "Sistemas de Recomendación", "credits": 4, "summer": False},
        "ISIS-4820": {"name": "Ambientes interactivos 3D", "credits": 4, "summer": False},
        "ISIS-4216": {"name": "Inteligencia artificial y representación de conocimiento", "credits": 4,
                      "summer": False}}

    for codigo in cursosIsis:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MISIS"),
            code=codigo,
            credits=cursosIsis[codigo]["credits"],
            name=cursosIsis[codigo]["name"],
            summer=cursosIsis[codigo]["summer"])

#-----------------------------------------------------------------------------------------------------------------------
    #Cursos de MISO
    print "carga de cursos de MISO"
    cursosMiso = {
        "MISO4202": {"name": "Mejoramiento de la productividad: Automatización", "credits": 4, "summer": False},
        "MISO4204": {"name": "Fábricas de software y líneas de producto", "credits": 4, "summer": False},
        "MISO4205": {"name": "Mejoramiento de la experiencia del usuario", "credits": 4, "summer": False},
        "MISO4301": {"name": "Proyecto Integrador", "credits": 4, "summer": False},
        "MISO4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MISO4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MISO4205": {"name": "Mejoramiento de la experiencia del usuario", "credits": 4, "summer": False},
        "MISO4101": {"name": "Procesos de Desarrollo Ágiles", "credits": 4, "summer": False}}

    for codigo in cursosMiso:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MISIS"),
            code=codigo,
            credits=cursosMiso[codigo]["credits"],
            name=cursosMiso[codigo]["name"],
            summer=cursosMiso[codigo]["summer"])

    #Secciones de MISO
    print "carga de secciones de MISO"
    seccionesMiso = {
        14446: {"course": "MISO4101", "name": "1", "capacity": {"MISO": 35, "pregrado": 3, "otros": 2}, "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        13986: {"course": "MISO4202", "name": "1", "capacity": {"MISO": 35, "pregrado": 2, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000001, "status": 0},
        14604: {"course": "MISO4204", "name": "1", "capacity": {"MISO": 35, "pregrado": 3, "otros": 2}, "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        16210: {"course": "MISO4205", "name": "1", "capacity": {"MISO": 33, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000002, "status": 0},
        16211: {"course": "MISO4301", "name": "1", "capacity": {"MISO": 99}, "semester": 1, "year": 2015, "teacher": 000000003, "status": 0},
        15251: {"course": "MISO4302", "name": "1", "capacity": {"MISO": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0},
        16212: {"course": "MISO4303", "name": "1", "capacity": {"MISO": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0}}

    for seccion in seccionesMiso:
        add_section(
            crn=seccion,
            name=seccionesMiso[seccion]["name"],
            semester=seccionesMiso[seccion]["semester"],
            year=seccionesMiso[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMiso[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMiso[seccion]["course"]),
            capacity=seccionesMiso[seccion]["capacity"],
            status=seccionesMiso[seccion]["status"]
        )

#-----------------------------------------------------------------------------------------------------------------------
    #Creación de plan de estudio
    print "Plan de estudio de estudiante"
    planEstudio = {
                    199024632: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    199922880: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    200012581: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    200022105: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    200110321: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    200124062: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    200125103: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" },
                    200220825: {"course_1": "MISO4101", "course_2": "MISO4202", "course_3": "MISO4204", "course_4": "MISO4205" }}

    for course in planEstudio:
        obj_scheme = add_scheme("plan"+str(course))
        add_couse_scheme(obj_scheme, planEstudio, course)

    notasEstudiantes = {
                        199024632: {14446: 5, 13986: 4, 14604: 2.5, 16210: 3},
                        199922880: {14446: 4, 13986: 4, 14604: 2.5, 16210: 3},
                        200012581: {14446: 5, 13986: 3, 14604: 2.5, 16210: 3},
                        200022105: {14446: 2, 13986: 3.4, 14604: 2.5, 16210: 3},
                        200110321: {14446: 1, 13986: 5, 14604: 2.5, 16210: 3},
                        200124062: {14446: 3, 13986: 4, 14604: 2.5, 16210: 3},
                        200125103: {14446: 2.4, 13986: 4, 14604: 2.5, 16210: 3},
                        200220825: {14446: 3.1, 13986: 4, 14604: 2.5, 16210: 3}}

    for estudiante in notasEstudiantes:
        for section in notasEstudiantes[estudiante]:
            add_course_grade(section, estudiante, notasEstudiantes[estudiante][section])


#-----------------------------------------------------------------------------------------------------------------------
#Metodo encargado de crear un plan de estudio del estudiante
def add_course_grade(section, student, grade):
    sect_obj = Section.objects.get(crn=section)
    stud_obj = Student.objects.get(code=student)
    student_status = False
    if grade >= 3:
        student_status = True
    subj_obj = Subject.objects.get_or_create(grade=grade,
                                             section=sect_obj,
                                             student=stud_obj,
                                             student_status=student_status)
    return subj_obj


#Metodo encargado de crear un plan de estudio del estudiante
def add_couse_scheme(scheme, planEstudio, course):
        for cursos in planEstudio[course]:
            curso_obj = Course.objects.get(code=planEstudio[course][cursos])
            scheme.courses.add(curso_obj)
            student_obj = Student.objects.get(code=course)
            student_obj.scheme = scheme
            student_obj.save()


#Metodo encargado de crear un plan de estudio del estudiante
def add_scheme(name):
    obj_scheme = Scheme.objects.get_or_create(name=name)[0]
    return obj_scheme


#Metodo encargado de crear o dar un profesor
# params:   code => el codigo del profesor,
#           email => email del profesor, lastname => Apellido del profesor,
#           name => Nombre del profesor
def add_teacher(code, email, lastname, name):
    obj_teacher = Teacher.objects.get_or_create(code=code, email=email, lastname=lastname, name=name)[0]
    return obj_teacher


#Metodo encargado de crear una maestria
# params: name => nombre de la maestria
def add_master(name):
    p = Master.objects.get_or_create(name=name)[0]
    return p


#Metodo encargado de crear un estudiante
# params: code => codigo del estudiante, email => email del estudiante, lastname => apellido del estudiante,
#         name => Nombre del estudiante, master
def add_student(code, email, lastname, name, master):
    p = Student.objects.get_or_create(code=code, email=email, lastname=lastname, name=name, master=master)[0]
    return p


#Metodo encargado crear un curso
def add_course(pensum, code, credits, name, summer):
    obj_course = Course.objects.get_or_create(code=code,
                                              credits=credits,
                                              name=name,
                                              summer=summer,
                                              pensum=pensum)[0]
    return obj_course


#Metodo encargado crear una sección
def add_section(crn, name, semester, year, teacher, course, capacity, status):
    obj_section = Section.objects.get_or_create(crn=crn,
                                                name=name,
                                                semester=semester,
                                                year=year,
                                                teacher=teacher,
                                                course=course,
                                                status=status)[0]
    for capacidad in capacity:
        Capacity.objects.create(name=capacidad, capacity=capacity[capacidad], section=obj_section)
    return obj_section


#Metodo encargado en definir la creacion de un pensum
def add_pensum(name, active, master):
    if master != None:
        obj_pensum = Pensum.objects.get_or_create(name="Pensum_" + name,
                                                  active=active,
                                                  master=master)[0]
    return obj_pensum


# Start execution here!
if __name__ == '__main__':
    print "Iniciando población de datos base"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mati.settings')
    from map.models import Master, Pensum, Course, Teacher, Section, Capacity, Student, Scheme,Subject

    populate()

    # add_page(cat=python_cat,
    #     title="How to Think like a Computer Scientist",
    #     url="http://www.greenteapress.com/thinkpython/")
    #
    # add_page(cat=python_cat,
    #     title="Learn Python in 10 Minutes",
    #     url="http://www.korokithakis.net/tutorials/python/")
    #
    # django_cat = add_cat("Django")
    #
    # add_page(cat=django_cat,
    #     title="Official Django Tutorial",
    #     url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    #
    # add_page(cat=django_cat,
    #     title="Django Rocks",
    #     url="http://www.djangorocks.com/")
    #
    # add_page(cat=django_cat,
    #     title="How to Tango with Django",
    #     url="http://www.tangowithdjango.com/")
    #
    # frame_cat = add_cat("Other Frameworks")
    #
    # add_page(cat=frame_cat,
    #     title="Bottle",
    #     url="http://bottlepy.org/docs/dev/")
    #
    # add_page(cat=frame_cat,
    #     title="Flask",
    #     url="http://flask.pocoo.org")

    # # Print out what we have added to the user.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))