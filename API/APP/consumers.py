import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import User, Message, Reservation, Course

class CommunityConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        content = data['content']

        try:
            member = User.objects.get(id=user_id)
            message = Message.objects.create(
                member=member,
                content=content
            )
            await self.send(text_data=json.dumps({
                'message': 'Message created successfully',
                'message_id': message.id
            }))
        except User.DoesNotExist:
            await self.send(text_data=json.dumps({
                'error': 'Member not found'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'error': str(e)
            }))

class ReservationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['user_id']
        course_id = data['course_id']
        reservation_date = data['reservation_date']

        try:
            User = User.objects.get(id=user_id)
            course = Course.objects.get(id=course_id)
            reservation = Reservation.objects.create(
                User=User,
                course=course,
                reservation_date=reservation_date
            )
            await self.send(text_data=json.dumps({
                'message': 'Reservation created successfully',
                'reservation_id': reservation.id
            }))
        except User.DoesNotExist:
            await self.send(text_data=json.dumps({
                'error': 'Member not found'
            }))
        except Course.DoesNotExist:
            await self.send(text_data.json.dumps({
                'error': 'Course not found'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'error': str(e)
            }))
