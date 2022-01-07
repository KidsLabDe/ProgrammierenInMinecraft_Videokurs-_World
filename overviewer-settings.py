import os

worlds['Leer'] = '/opt/mscs/backups/Leer/Leer-original' if os.path.exists('/opt/mscs/backups/Leer/Leer-original') else '/opt/mscs/backups/Leer/Leer'

renders['overworld-render'] = {
  'world': 'Leer',
  'title': 'Overworld',
  'dimension': 'overworld',
  'rendermode': 'normal'
}

renders['overworld-caves-render'] = {
  'world': 'Leer',
  'title': 'Caves',
  'dimension': 'overworld',
  'rendermode': 'cave'
}

renders['nether-render'] = {
  'world': 'Leer',
  'title': 'Nether',
  'dimension': 'nether',
  'rendermode': 'nether'
}

renders['end-render'] = {
  'world': 'Leer',
  'title': 'End',
  'dimension': 'end',
  'rendermode': 'normal'
}

processes = 2
outputdir = '/opt/mscs/maps/Leer'
