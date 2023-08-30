#IMPORTS
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib as plt
import seaborn as sbn
import os
import sys
  

# Leer la tabla HTML y convertirla en un DataFrame
tabla_df = pd.read_html(os.path.join(sys.path[0], 'Scouted_shortlist.html'), encoding='utf8', skiprows=0)[0]


df = pd.DataFrame(tabla_df)

#print(tabla_df.head())


#Función para convertir valores con guión a valores calculados en los atributos no ojeados del todo y obtener un valor aproximado
def attr_fix(value):
    if '-' in value:
        parts = value.split('-')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            left_part = int(parts[0])
            right_part = int(parts[1])
            result = (left_part + right_part) // 2
            return result
        else:
            return 0
    else:
        return int(value)



info = df.columns[3:8]
df_info = df[info]

attributes = df.columns[10:57]
df_attributes = df[attributes]

name = df['Nombre']

df = pd.concat([df_info, df_attributes], axis=1)

#DNA jugadores
df['dna_score'] = df['Agr'].apply(attr_fix).astype(int) + df['Det'].apply(attr_fix).astype(int) + df['JEq'].apply(attr_fix).astype(int) + df['Sac'].apply(attr_fix).astype(int)

dna = df[['Nombre', 'Edad', 'Agr', 'Det', 'JEq', 'Sac', 'dna_score']]
sorted_dna = dna.sort_values(by='dna_score', ascending=False)
#print(sorted_dna)


#PORTEROS

#Portero
df['Portero'] = df['Aér'].apply(attr_fix).astype(int) + df['Blo'].apply(attr_fix).astype(int) + df['Com'].apply(attr_fix).astype(int) + df['Mdo'].apply(attr_fix).astype(int) + df['Ref'].apply(attr_fix).astype(int) + df['Saq'].apply(attr_fix).astype(int) + df['Pue'].apply(attr_fix).astype(int) + df['1v1'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['Cnc'].apply(attr_fix).astype(int) + df['Dec'].apply(attr_fix).astype(int) + df['Agi'].apply(attr_fix).astype(int)
portero = df[['Nombre', 'Edad', 'Aér', 'Blo', 'Com', 'Mdo', 'Ref', 'Saq', 'Pue', '1v1', 'Ant', 'Col', 'Cnc', 'Dec', 'Agi', 'Portero']]
sorted_portero = portero.sort_values(by='Portero', ascending=False)
#print(sorted_portero)

#Portero cierre
df['Portero_cierre'] = df['Aér'].apply(attr_fix).astype(int) + df['Blo'].apply(attr_fix).astype(int) + df['Com'].apply(attr_fix).astype(int) + df['Mdo'].apply(attr_fix).astype(int) + df['Ref'].apply(attr_fix).astype(int) + df['Saq'].apply(attr_fix).astype(int) + df['Pue'].apply(attr_fix).astype(int) + df['1v1'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['Cnc'].apply(attr_fix).astype(int) + df['Dec'].apply(attr_fix).astype(int) + df['Agi'].apply(attr_fix).astype(int) + df['Ctr'].apply(attr_fix).astype(int) + df['Pas'].apply(attr_fix).astype(int) + df['Sal'].apply(attr_fix).astype(int) + df['Ser'].apply(attr_fix).astype(int) + df['Vis'].apply(attr_fix).astype(int) + df['Ace'].apply(attr_fix).astype(int)
portero_cierre = df[['Nombre', 'Edad', 'Ctr', 'Pas', 'Sal', 'Ser', 'Vis', 'Ace', 'Aér', 'Blo', 'Com', 'Mdo', 'Ref', 'Saq', 'Pue', '1v1', 'Ant', 'Col', 'Cnc', 'Dec', 'Agi', 'Portero_cierre']]
sorted_portero_cierre = portero_cierre.sort_values(by='Portero_cierre', ascending=False)
#print(sorted_portero_cierre)


#DEFENSAS

#Carrilero
df['Carrilero'] = df['Cen'].apply(attr_fix).astype(int) + df['Reg'].apply(attr_fix).astype(int) + df['Ctr'].apply(attr_fix).astype(int) + df['Mar'].apply(attr_fix).astype(int) + df['Pas'].apply(attr_fix).astype(int) + df['Ent'].apply(attr_fix).astype(int) + df['Téc'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Cnc'].apply(attr_fix).astype(int) + df['Dec'].apply(attr_fix).astype(int) + df['Tal'].apply(attr_fix).astype(int) + df['Dmq'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['JEq'].apply(attr_fix).astype(int) + df['Sac'].apply(attr_fix).astype(int) + df['Ace'].apply(attr_fix).astype(int) + df['Agi'].apply(attr_fix).astype(int) + df['Vel'].apply(attr_fix).astype(int) + df['Res'].apply(attr_fix).astype(int)
carrilero =  df[['Nombre', 'Edad', 'Cen', 'Reg', 'Ctr', 'Mar', 'Pas', 'Ent', 'Téc', 'Ant', 'Cnc', 'Dec', 'Tal', 'Dmq', 'Col', 'JEq', 'Sac', 'Ace', 'Agi', 'Vel', 'Res', 'Carrilero']]
sorted_carrilero = carrilero.sort_values(by='Carrilero', ascending=False)
#print(sorted_carrilero)

#Carrilero completo
df['Carr comp'] = df['Cen'].apply(attr_fix).astype(int) + df['Reg'].apply(attr_fix).astype(int) + df['Ctr'].apply(attr_fix).astype(int) + df['Ser'].apply(attr_fix).astype(int) + df['Pas'].apply(attr_fix).astype(int) + df['Ent'].apply(attr_fix).astype(int) + df['Téc'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Equ'].apply(attr_fix).astype(int) + df['Dec'].apply(attr_fix).astype(int) + df['Tal'].apply(attr_fix).astype(int) + df['Dmq'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['JEq'].apply(attr_fix).astype(int) + df['Sac'].apply(attr_fix).astype(int) + df['Ace'].apply(attr_fix).astype(int) + df['Agi'].apply(attr_fix).astype(int) + df['Vel'].apply(attr_fix).astype(int) + df['Res'].apply(attr_fix).astype(int)
carr_comp =  df[['Nombre', 'Edad', 'Cen', 'Reg', 'Ctr', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Dec', 'Tal', 'Dmq', 'Col', 'JEq', 'Sac', 'Ace', 'Agi', 'Equ', 'Vel', 'Res', 'Carr comp']]
sorted_carr_comp = carr_comp.sort_values(by='Carr comp', ascending=False)
#print(sorted_carr_comp)

#Carrilero inverso
df['Carr inv'] = df['Reg'].apply(attr_fix).astype(int) + df['Ctr'].apply(attr_fix).astype(int) + df['Mar'].apply(attr_fix).astype(int) + df['Pas'].apply(attr_fix).astype(int) + df['Ent'].apply(attr_fix).astype(int) + df['Téc'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Ser'].apply(attr_fix).astype(int) + df['Cnc'].apply(attr_fix).astype(int) + df['Dec'].apply(attr_fix).astype(int) + df['Dmq'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['JEq'].apply(attr_fix).astype(int) + df['Sac'].apply(attr_fix).astype(int) + df['Ace'].apply(attr_fix).astype(int) + df['Agi'].apply(attr_fix).astype(int) + df['Res'].apply(attr_fix).astype(int)
carr_inv =  df[['Nombre', 'Edad', 'Reg', 'Ctr', 'Mar', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Cnc', 'Dec', 'Dmq', 'Col', 'JEq', 'Sac', 'Ace', 'Agi', 'Res', 'Carr inv']]
sorted_carr_inv = carr_inv.sort_values(by='Carr inv', ascending=False)
#print(sorted_carr_inv)

#Central lateral
df['Central lat'] =df['Cen'].apply(attr_fix).astype(int) + df['Reg'].apply(attr_fix).astype(int) + df['Cab'].apply(attr_fix).astype(int) + df['Mar'].apply(attr_fix).astype(int) + df['Ent'].apply(attr_fix).astype(int) + df['Agr'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Val'].apply(attr_fix).astype(int) + df['Ser'].apply(attr_fix).astype(int) + df['Cnc'].apply(attr_fix).astype(int) + df['Dec'].apply(attr_fix).astype(int) + df['Dmq'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['Sac'].apply(attr_fix).astype(int) + df['Sal'].apply(attr_fix).astype(int) + df['Vel'].apply(attr_fix).astype(int) + df['Res'].apply(attr_fix).astype(int) + df['Fue'].apply(attr_fix).astype(int)
central_lat =  df[['Nombre', 'Edad','Cen' 'Reg', 'Cab', 'Mar', 'Ent', 'Agr', 'Ant', 'Val', 'Ser', 'Cnc', 'Dec', 'Dmq', 'Col', 'Sac', 'Sal', 'Vel', 'Fue', 'Res', 'Central lat']]
sorted_central_lat = carr_inv.sort_values(by='Central lat', ascending=False)

#Central práctico
df['Central practico'] = df['Cab'].apply(attr_fix).astype(int) + df['Mar'].apply(attr_fix).astype(int) + df['Ent'].apply(attr_fix).astype(int) + df['Agr'].apply(attr_fix).astype(int) + df['Ant'].apply(attr_fix).astype(int) + df['Val'].apply(attr_fix).astype(int) + df['Cnc'].apply(attr_fix).astype(int) + df['Col'].apply(attr_fix).astype(int) + df['Sal'].apply(attr_fix).astype(int) + df['Vel'].apply(attr_fix).astype(int) + df['Fue'].apply(attr_fix).astype(int)
central_practico = df[['Nombre', 'Edad', 'Cab', 'Mar', 'Ent', 'Agr', 'Ant', 'Val', 'Cnc', 'Col', 'Sal', 'Vel', 'Fue', 'Central practico']]
sorted_central_practico = central_practico.sort_values(by='Central practico', ascending=False)
#print(sorted_central_practico)

#Central con toque
df['Central con toque'] = (
    df['Ctr'].apply(attr_fix).astype(int)
    + df['Cab'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

central_con_toque = df[
    ['Nombre', 'Edad', 'Ctr', 'Cab', 'Mar', 'Pas', 'Ent', 'Téc', 'Agr', 'Ant', 'Val', 'Ser', 'Cnc', 'Vis', 'Dec', 'Col', 'Sal', 'Vel', 'Fue', 'Central con toque']
]

sorted_central_con_toque = central_con_toque.sort_values(by='Central con toque', ascending=False)
#print(sorted_central_con_toque)

#Defensa central
df['Defensa central'] = (
    df['Cab'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

defensa_central = df[
    ['Nombre', 'Edad', 'Cab', 'Mar', 'Ent', 'Agr', 'Ant', 'Val', 'Ser', 'Cnc', 'Dec', 'Col', 'Sal', 'Fue', 'Defensa central']
]

sorted_defensa_central = defensa_central.sort_values(by='Defensa central', ascending=False)
#print(sorted_defensa_central)

# Libero
df['Libero'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Cab'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

libero = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Cab', 'Mar', 'Pas', 'Ent', 'Téc', 'Ant', 'Val', 'Ser', 'Cnc', 'Vis', 'Dec', 'Tal', 'Col', 'JEq', 'Agi', 'Equ', 'Sal', 'Vel', 'Res', 'Fue', 'Libero']
]

sorted_libero = libero.sort_values(by='Libero', ascending=False)
#print(sorted_libero)


# Lateral
df['Lateral'] = (
    df['Cen'].apply(attr_fix).astype(int)
    + df['Reg'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

lateral = df[
    ['Nombre', 'Edad', 'Cen', 'Reg', 'Mar', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Cnc', 'Dec', 'Col', 'JEq', 'Sac', 'Vel', 'Res', 'Lateral']
]

sorted_lateral = lateral.sort_values(by='Lateral', ascending=False)
#print(sorted_lateral)


# Lateral práctico
df['Lateral práctico'] = (
    df['Cab'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

lateral_practico = df[
    ['Nombre', 'Edad', 'Cab', 'Mar', 'Ent', 'Agr', 'Ant', 'Val', 'Cnc', 'Col', 'JEq', 'Fue', 'Lateral práctico']
]

sorted_lateral_practico = lateral_practico.sort_values(by='Lateral práctico', ascending=False)
#print(sorted_lateral_practico)



#MEDIOCAMPISTAS

# Buscador espacios
df['Buscador espacios'] = (
    df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

buscador_espacios = df[
    ['Nombre', 'Edad', 'Rem', 'Ctr', 'Téc', 'Ant', 'Ser', 'Cnc', 'Dec', 'Dmq', 'Sac', 'Ace', 'Equ', 'Res', 'Buscador espacios']
]

sorted_buscador_espacios = buscador_espacios.sort_values(by='Buscador espacios', ascending=False)
# print(sorted_buscador_espacios)


# Centrocampista
df['Centrocampista'] = (
    df['Ctr'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

centrocampista = df[
    ['Nombre', 'Edad', 'Ctr', 'Mar', 'Pas', 'Ent', 'Téc', 'Agr', 'Ant', 'Ser', 'Cnc', 'Dmq', 'Col', 'JEq', 'Sac', 'Res', 'Centrocampista']
]

sorted_centrocampista = centrocampista.sort_values(by='Centrocampista', ascending=False)
# print(sorted_centrocampista)


# Centrocampista banda
df['Centrocampista banda'] = (
    df['Cen'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

centrocampista_banda = df[
    ['Nombre', 'Edad', 'Cen', 'Ctr', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Cnc', 'Vis', 'Dec', 'Dmq', 'Col', 'JEq', 'Sac', 'Res', 'Centrocampista banda']
]

sorted_centrocampista_banda = centrocampista_banda.sort_values(by='Centrocampista banda', ascending=False)
# print(sorted_centrocampista_banda)


# Centrocampista recuperador
df['Centrocampista recuperador'] = (
    df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

centrocampista_recuperador = df[
    ['Nombre', 'Edad', 'Mar', 'Pas', 'Ent', 'Agr', 'Ant', 'Val', 'Cnc', 'JEq', 'Sac', 'Agi', 'Vel', 'Res', 'Fue', 'Centrocampista recuperador']
]

sorted_centrocampista_recuperador = centrocampista_recuperador.sort_values(by='Centrocampista recuperador', ascending=False)
# print(sorted_centrocampista_recuperador)


# Centrocampista todoterreno
df['Centrocampista todoterreno'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

centrocampista_todoterreno = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Lej', 'Pas', 'Ent', 'Téc', 'Agr', 'Ant', 'Ser', 'Dec', 'Dmq', 'Col', 'JEq', 'Sac', 'Ace', 'Equ', 'Vel', 'Res', 'Fue', 'Centrocampista todoterreno']
]

sorted_centrocampista_todoterreno = centrocampista_todoterreno.sort_values(by='Centrocampista todoterreno', ascending=False)
# print(sorted_centrocampista_todoterreno)


# Delantero interior
df['Delantero interior'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
)

delantero_interior = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Lej', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Tal', 'Dmq', 'Ace', 'Agi', 'Equ', 'Vel', 'Delantero interior']
]

sorted_delantero_interior = delantero_interior.sort_values(by='Delantero interior', ascending=False)
# print(sorted_delantero_interior)


# Delantero objetivo escorado
df['Delantero objetivo escorado'] = (
    df['Cen'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Cab'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

delantero_objetivo_escorado = df[
    ['Nombre', 'Edad', 'Cen', 'Ctr', 'Cab', 'Ant', 'Val', 'Dmq', 'JEq', 'Sac', 'Equ', 'Sal', 'Res', 'Fue', 'Delantero objetivo escorado']
]

sorted_delantero_objetivo_escorado = delantero_objetivo_escorado.sort_values(by='Delantero objetivo escorado', ascending=False)
# print(sorted_delantero_objetivo_escorado)


# Delantero sorpresa
df['Delantero sorpresa'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

delantero_sorpresa = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Cnc', 'Dec', 'Dmq', 'Sac', 'Ace', 'Agi', 'Equ', 'Vel', 'Res', 'Delantero sorpresa']
]

sorted_delantero_sorpresa = delantero_sorpresa.sort_values(by='Delantero sorpresa', ascending=False)
# print(sorted_delantero_sorpresa)


# enganche
df['Enganche'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
)

enganche = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Tal', 'Dmq', 'JEq', 'Agi', 'Enganche']
]

sorted_enganche = enganche.sort_values(by='Enganche', ascending=False)
#print(sorted_enganche)

# extremo
df['Extremo'] = (
    df['Cen'].apply(attr_fix).astype(int)
    + df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

extremo = df[
    ['Nombre', 'Edad', 'Cen', 'Reg', 'Ctr', 'Pas', 'Téc', 'Dmq', 'Sac', 'Ace', 'Agi', 'Vel', 'Res', 'Extremo']
]

sorted_extremo = extremo.sort_values(by='Extremo', ascending=False)
#print(sorted_extremo)

# extremo defensivo
df['Extremo defensivo'] = (
    df['Cen'].apply(attr_fix).astype(int)
    + df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

extremo_defensivo = df[
    ['Nombre', 'Edad', 'Cen', 'Reg', 'Ctr', 'Mar', 'Pas', 'Ent', 'Téc', 'Agr', 'Ant', 'Ser', 'Cnc', 'Dec', 'Dmq', 'Col', 'JEq', 'Sac', 'Ace', 'Res', 'Extremo defensivo']
]

sorted_extremo_defensivo = extremo_defensivo.sort_values(by='Extremo defensivo', ascending=False)
#print(sorted_extremo_defensivo)

# extremo inverso
df['Extremo inverso'] = (
    df['Cen'].apply(attr_fix).astype(int)
    + df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

extremo_inverso = df[
    ['Nombre', 'Edad', 'Cen', 'Reg', 'Ctr', 'Lej', 'Pas', 'Téc', 'Ser', 'Vis', 'Dec', 'Dmq', 'Sac', 'Ace', 'Agi', 'Vel', 'Res', 'Extremo inverso']
]

sorted_extremo_inverso = extremo_inverso.sort_values(by='Extremo inverso', ascending=False)
#print(sorted_extremo_inverso)

# Interior mixto
df['Interior mixto'] = (
    df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

interior_mixto = df[
    ['Nombre', 'Edad', 'Ctr', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Cnc', 'Vis', 'Dec', 'Dmq', 'Col', 'JEq', 'Sac', 'Res', 'Interior mixto']
]

sorted_interior_mixto = interior_mixto.sort_values(by='Interior mixto', ascending=False)
#print(sorted_interior_mixto)


# Mediapunta
df['Mediapunta'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
)

mediapunta = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Lej', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Tal', 'Dmq', 'Agi', 'Mediapunta']
]

sorted_mediapunta = mediapunta.sort_values(by='Mediapunta', ascending=False)
#print(sorted_mediapunta)


# Medio cierre
df['Medio cierre'] = (
    df['Ctr'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

medio_cierre = df[
    ['Nombre', 'Edad', 'Ctr', 'Mar', 'Pas', 'Ent', 'Agr', 'Ant', 'Ser', 'Cnc', 'Dec', 'Col', 'JEq', 'Sac', 'Val', 'Res', 'Sal', 'Fue', 'Medio cierre']
]

sorted_medio_cierre = medio_cierre.sort_values(by='Medio cierre', ascending=False)
#print(sorted_medio_cierre)


# Mediocentro
df['Mediocentro'] = (
    df['Ctr'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

mediocentro = df[
    ['Nombre', 'Edad', 'Ctr', 'Mar', 'Pas', 'Ent', 'Agr', 'Ant', 'Ser', 'Cnc', 'Dec', 'Col', 'JEq', 'Sac', 'Res', 'Fue', 'Mediocentro']
]

sorted_mediocentro = mediocentro.sort_values(by='Mediocentro', ascending=False)
#print(sorted_mediocentro)


# Mezzala
df['Mezzala'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

mezzala = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Lej', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Dmq', 'Sac', 'Ace', 'Equ', 'Res', 'Mezzala']
]

sorted_mezzala = mezzala.sort_values(by='Mezzala', ascending=False)
#print(sorted_mezzala)


# Organizador adelantado
df['Organizador adelantado'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
)

organizador_adelantado = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Tal', 'Vis', 'Dec', 'Dmq', 'JEq', 'Agi', 'Organizador adelantado']
]

sorted_organizador_adelantado = organizador_adelantado.sort_values(by='Organizador adelantado', ascending=False)
#print(sorted_organizador_adelantado)


# Organizador banda
df['Organizador banda'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
)

organizador_banda = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Pas', 'Téc', 'Ser', 'Vis', 'Dec', 'Dmq', 'JEq', 'Agi', 'Organizador banda']
]

sorted_organizador_banda = organizador_banda.sort_values(by='Organizador banda', ascending=False)
#print(sorted_organizador_banda)


# Organizador itinerante
df['Organizador itinerante'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

organizador_itinerante = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Lej', 'Pas', 'Téc', 'Ant', 'Ser', 'Cnc', 'Vis', 'Dec', 'Dmq', 'Col', 'JEq', 'Sac', 'Ace', 'Agi', 'Equ', 'Vel', 'Res', 'Fue', 'Organizador itinerante']
]

sorted_organizador_itinerante = organizador_itinerante.sort_values(by='Organizador itinerante', ascending=False)
#print(sorted_organizador_itinerante)


# Pivote Defensivo
df['Pivote Defensivo'] = (
    df['Mar'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

pivote_defensivo = df[
    ['Nombre', 'Edad', 'Mar', 'Ent', 'Ant', 'Ser', 'Cnc', 'Dec', 'Col', 'JEq', 'Fue', 'Pivote Defensivo']
]

sorted_pivote_defensivo = pivote_defensivo.sort_values(by='Pivote Defensivo', ascending=False)
#print(sorted_pivote_defensivo)


# Pivote Organizador
df['Pivote Organizador'] = (
    df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
)

pivote_organizador = df[
    ['Nombre', 'Edad', 'Ctr', 'Pas', 'Ent', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Dmq', 'Col', 'JEq', 'Equ', 'Pivote Organizador']
]

sorted_pivote_organizador = pivote_organizador.sort_values(by='Pivote Organizador', ascending=False)
#print(sorted_pivote_organizador)


# Regista
df['Regista'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
)

regista = df[
    ['Nombre', 'Edad', 'Reg', 'Ctr', 'Lej', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Tal', 'Dmq', 'JEq', 'Equ', 'Regista']
]

sorted_regista = regista.sort_values(by='Regista', ascending=False)
#print(sorted_regista)


# Segundo Volante
df['Segundo Volante'] = (
    df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Mar'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Ent'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Col'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

segundo_volante = df[
    ['Nombre', 'Edad', 'Rem', 'Ctr', 'Lej', 'Mar', 'Pas', 'Ent', 'Ant', 'Ser', 'Cnc', 'Dec', 'Dmq', 'Col', 'Sac', 'Ace', 'Equ', 'Vel', 'Res', 'Fue', 'Segundo Volante']
]

sorted_segundo_volante = segundo_volante.sort_values(by='Segundo Volante', ascending=False)
#print(sorted_segundo_volante)



#DELANTEROS

# Ariete
df['Ariete'] = (
    df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Cab'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
)

ariete = df[
    ['Nombre', 'Edad', 'Rem', 'Ctr', 'Cab', 'Téc', 'Ant', 'Ser', 'Dec', 'Dmq', 'Ace', 'Ariete']
]

sorted_ariete = ariete.sort_values(by='Ariete', ascending=False)
#print(sorted_ariete)


# Delantero avanzado
df['Delantero avanzado'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
)

delantero_avanzado = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Dec', 'Dmq', 'Sac', 'Ace', 'Agi', 'Equ', 'Vel', 'Res', 'Delantero avanzado']
]

sorted_delantero_avanzado = delantero_avanzado.sort_values(by='Delantero avanzado', ascending=False)
#print(sorted_delantero_avanzado)


# Delantero completo
df['Delantero completo'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Cab'].apply(attr_fix).astype(int)
    + df['Lej'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

delantero_completo = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Cab', 'Lej', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Dmq', 'JEq', 'Sac', 'Ace', 'Agi', 'Equ', 'Sal', 'Vel', 'Res', 'Fue', 'Delantero completo']
]

sorted_delantero_completo = delantero_completo.sort_values(by='Delantero completo', ascending=False)
#print(sorted_delantero_completo)


# Delantero objetivo
df['Delantero objetivo'] = (
    df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Cab'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Sal'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

delantero_objetivo = df[
    ['Nombre', 'Edad', 'Rem', 'Ctr', 'Cab', 'Agr', 'Ant', 'Val', 'Ser', 'Dec', 'Dmq', 'JEq', 'Equ', 'Sal', 'Fue', 'Delantero objetivo']
]

sorted_delantero_objetivo = delantero_objetivo.sort_values(by='Delantero objetivo', ascending=False)
#print(sorted_delantero_objetivo)


# Delantero presionante
df['Delantero presionante'] = (
    df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Agr'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Val'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Cnc'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Sac'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Vel'].apply(attr_fix).astype(int)
    + df['Res'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

delantero_presionante = df[
    ['Nombre', 'Edad', 'Rem', 'Ctr', 'Pas', 'Agr', 'Ant', 'Val', 'Ser', 'Cnc', 'Dec', 'Dmq', 'JEq', 'Sac', 'Ace', 'Agi', 'Equ', 'Vel', 'Res', 'Fue', 'Delantero presionante']
]

sorted_delantero_presionante = delantero_presionante.sort_values(by='Delantero presionante', ascending=False)
#print(sorted_delantero_presionante)


# Falso nueve
df['Falso nueve'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
)

falso_nueve = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Tal', 'Dmq', 'JEq', 'Ace', 'Agi', 'Equ', 'Falso nueve']
]

sorted_falso_nueve = falso_nueve.sort_values(by='Falso nueve', ascending=False)
#print(sorted_falso_nueve)


# Segundo delantero
df['Segundo delantero'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['JEq'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
    + df['Fue'].apply(attr_fix).astype(int)
)

segundo_delantero = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Tal', 'Dmq', 'JEq', 'Equ', 'Fue', 'Segundo delantero']
]

sorted_segundo_delantero = segundo_delantero.sort_values(by='Segundo delantero', ascending=False)
#print(sorted_segundo_delantero)


# Trequartista
df['Trequartista'] = (
    df['Reg'].apply(attr_fix).astype(int)
    + df['Rem'].apply(attr_fix).astype(int)
    + df['Ctr'].apply(attr_fix).astype(int)
    + df['Pas'].apply(attr_fix).astype(int)
    + df['Téc'].apply(attr_fix).astype(int)
    + df['Ant'].apply(attr_fix).astype(int)
    + df['Ser'].apply(attr_fix).astype(int)
    + df['Vis'].apply(attr_fix).astype(int)
    + df['Dec'].apply(attr_fix).astype(int)
    + df['Tal'].apply(attr_fix).astype(int)
    + df['Dmq'].apply(attr_fix).astype(int)
    + df['Ace'].apply(attr_fix).astype(int)
    + df['Agi'].apply(attr_fix).astype(int)
    + df['Equ'].apply(attr_fix).astype(int)
)

trequartista = df[
    ['Nombre', 'Edad', 'Reg', 'Rem', 'Ctr', 'Pas', 'Téc', 'Ant', 'Ser', 'Vis', 'Dec', 'Tal', 'Dmq', 'Ace', 'Agi', 'Equ', 'Trequartista']
]

sorted_trequartista = trequartista.sort_values(by='Trequartista', ascending=False)
#print(sorted_trequartista)




#print(df)
#print(df_attributes.head())