from ztec.zdb import DB
db=DB()
db('usuarios').campo('nombres',db.str)
db('usuarios').campo('appelidos',db.str)
db('usuarios').campo('correo',db.email)
db('usuarios').campo('password',db.str)
db('usuarios').campo('foto',db.file)
db('usuarios').campo('imgs',db.list)
db('msj_chat').campo('emisor',db.object)
db('msj_chat').campo('receptores',db.list)
db('msj_chat').campo('mensaje',db.str)
db('msj_chat').campo('hora',db.time)
db('msj_correo').campo('emisor',db.object)
db('msj_correo').campo('receptores',db.list)
db('msj_correo').campo('mensaje',db.str)
db('msj_correo').campo('hora',db.time)
db('apps').campo('nombre',db.str)
db('apps').campo('autores',db.list)
db('apps').campo('organizaciones',db.list)
db('apps').campo('versión',db.float)
db('apps').campo('estabilidad',db.str)
db('apps').campo('alias',db.str)
db('apps').campo('parentProjects',db.list)
db('apps').campo('technologyLevel',db.str)
db('apps').campo('icono',db.url)
db('apps').campo('web',db.url)
db('apps').campo('licencia',db.str)
db('posts').campo('publisher',db.object)
db('posts').campo('destinatarios',db.list)
db('posts').campo('img',db.url)
db('posts').campo('lectores',db.list)
db('posts').campo('interacciones',db.list)
db('posts').campo('comentarios',db.list)
db('usuarios').insertar('jesus', 'zerpa', 'jesus26abraham1996@gmaill.com', '123456', 'https://localhost/AsenZor/apps/default/user/static/imgs/icono_perfil.jpg', [])