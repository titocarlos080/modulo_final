import requests
from odoo import api
from odoo.http import request

class NotificacionController:

    @staticmethod
    def enviarNotificacion(notas):
        print("ESTAS SON LAS NOTAS QUE SE AGREGARON" ,notas)
        keyPadre = NotificacionController.obtenerKeyPadre(notas.get('student_id'))
        if keyPadre:
            codigo = notas.get('codigo')
            name = notas.get('name')
            descripcion = notas.get('descripcion')
            student_id = notas.get('student_id')
            materia_id = notas.get('materia_id')
            gestion = notas.get('gestion')
            nota = notas.get('nota')
           
            nota = notas.nota
            mensaje = f"Se subieron las notas del estudiante {name} para la materia {materia_id}. Nota: {nota}"
            NotificacionController.send_notification(keyPadre, 'Actualización de Notas', mensaje)

    @staticmethod
    def obtenerKeyPadre(student_id):
         # Lógica para obtener la key de notificación del padre según el ID del estudiante
         padre =  request.env['res.partner'].sudo().search([('padre_id', '=', student_id)], limit=1)
         return padre.keynotificaciones if padre else None

    @staticmethod
    def send_notification(device_token, title, body):
        print("Clave kkkkkkkksd sdd  ==========",device_token)
        server_key = 'AAAAM-ejTlM:APA91bEqdQRAjd_2_qXK23M9c7CbbDf7SVpjas789C9xMQXtEkUNSHeT4Gj9t3nTOG_Tk6JK9C4qDD1n1r0oZeRtI9otcoi-OhPJDsw93LypxhQpHRvi9ZG9eS_WmT_fHagLHSSZubtF'
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {
            'Authorization': 'key=' + server_key,
            'Content-Type': 'application/json',
        }
        data = {
            'to': device_token,
            'notification': {
                'title': title,
                'body': body,
            },
        }
        response = requests.post(url, headers=headers, json=data)
        return response.status_code
